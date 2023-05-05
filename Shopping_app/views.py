from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Cart, CartItem, Volcano, Address, Order, OrderItem
from django.utils import timezone




def volcano_list(request):
    volcanoes = Volcano.objects.all()
    paginator = Paginator(volcanoes, 25)  # 每页25个火山
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/volcano_list.html', {'page_obj': page_obj})




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
def create_empty_cart(request):
    # 获取当前用户的购物车，如果不存在则创建
    cart, created = Cart.objects.get_or_create(user=request.user)

    # 如果已经创建了购物车，那么跳转到 'store' 页面
    if not created:
        return redirect('store')

    # 渲染页面
    context = {}
    return render(request, 'store/create_empty_cart.html', context)


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




@login_required(login_url='login_view')
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    total_price = cart.total_price
    address = None  # initialize address to None

    if request.method == 'POST':
        # get address data from POST request
        line_1 = request.POST['line_1']
        line_2 = request.POST['line_2']
        country = request.POST['country']
        postal_code = request.POST['postal_code']
        phone_number = request.POST['phone_number']

        # create new address instance and associate it with current user
        address = Address.objects.create(user=request.user,
                                         line_1=line_1,
                                         line_2=line_2,
                                         country=country,
                                         postal_code=postal_code,
                                         phone_number=phone_number)

    context = {'cart': cart, 'cart_items': cart_items, 'total_price': total_price, 'address': address}
    return render(request, 'store/checkout.html', context)




@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    total_price = cart.total_price

    # Create a new order and order items for each item in the cart
    order = Order.objects.create(
        user_id=request.user.id,
        user_name=request.user.username,
        user_phone='0123456789', # replace with user's phone number from address model
        total_cost=total_price
    )
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            volcano=item.volcano,
            quantity=item.quantity
        )

    # Clear the cart
    cart.clear()

    # Render the order confirmation page with the order information
    order_items = order.order_items.all()
    context = {'order': order, 'order_items': order_items}
    return render(request, 'store/order_confirmation.html', context)