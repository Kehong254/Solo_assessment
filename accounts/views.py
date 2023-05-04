from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 != password2:
            error_message = 'Inconsistent passwords'
            return render(request, 'register.html', {'error_message': error_message})
        elif username == '':
            error_message = 'Username cannot be empty'
            return render(request, 'register.html', {'error_message': error_message})
        cuser = User.objects.create_user(username=username, password=password1, email=email)
        cuser.save()
        return redirect('store')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'successful login')
            return redirect('store')
        else:
            msg = 'Invalid login credentials'
            messages.error(request, msg)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('store'))

