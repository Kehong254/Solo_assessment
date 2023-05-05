from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Cart, CartItem, Volcano

@login_required
def store(request):
    query = request.GET.get('query')
    volcanoes = Volcano.objects.all()
    if query:
        volcanoes = volcanoes.filter(Q(Volcano_Name__icontains=query) | Q(Country__icontains=query) | Q(Volcano_Type__icontains=query)).order_by('-Volcano_ID')
    paginator = Paginator(volcanoes, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        volcano_id = request.POST.get('Volcano_ID')
        quantity = request.POST.get('quantity', 1)
        volcano = Volcano.objects.get(pk=volcano_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, volcano=volcano)
        cart_item.quantity += int(quantity)
        cart_item.save()
        return redirect('store')

    context = {'page_obj': page_obj}
    return render(request, 'store/store.html', context)

def volcano_detail(request, Volcano_ID):
    volcano = get_object_or_404(Volcano, Volcano_ID=Volcano_ID)
    context = {'volcano': volcano}
    return render(request, 'store/volcano_detail.html', context)

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    context = {'cart': cart, 'cart_items': cart_items}
    return render(request, 'store/cart.html', context)

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    total_price = cart.total_price
    context = {'cart': cart, 'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'store/checkout.html', context)
