'''from django.shortcuts import render


from .models import Volcano

# Create your views here.

def store(request):
  context = {}
  return render(request, 'store/store.html', context)

def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)'''


from django.shortcuts import render
from .models import Volcano
from django.shortcuts import render, get_object_or_404

def store(request):
    # 获取所有的 Volcano 对象
    volcanoes = Volcano.objects.all()
    # 将 volcanoes 对象传递到模板中
    context = {'volcanoes': volcanoes}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def volcano_detail(request, Volcano_ID):
    volcano = get_object_or_404(Volcano, Volcano_ID=Volcano_ID)
    context = {'volcano': volcano}
    return render(request, 'store/volcano_detail.html', context)
