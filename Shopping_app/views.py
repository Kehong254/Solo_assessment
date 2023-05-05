from .models import Volcano
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Volcano, Cart, CartItem
#ignore warning of query
import warnings
from django.core.paginator import UnorderedObjectListWarning

warnings.simplefilter('ignore', UnorderedObjectListWarning)

# Create your views here.

def store(request):
    query = request.GET.get('query')
    volcanoes = Volcano.objects.all()
    if query:
        volcanoes = volcanoes.filter(Q(Volcano_Name__icontains=query) | Q(Country__icontains=query) | Q(Volcano_Type__icontains=query)).order_by('-Volcano_ID')
    paginator = Paginator(volcanoes, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'store/store.html', context)

def volcano_detail(request, Volcano_ID):
    volcano = get_object_or_404(Volcano, Volcano_ID=Volcano_ID)
    context = {'volcano': volcano}
    return render(request, 'store/volcano_detail.html', context)

# @login_required(login_url='accounts:login_view')
def add_to_cart(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            price = float(request.POST['price'].replace(',', '.'))
            quantity = int(request.POST.get('quantity'))

            # volcano = get_object_or_404(Volcano, Volcano_Name=name, price=price)  # Change Product to Volcano
            cart,created = Cart.objects.get_or_create(name=name, price=price,quantity=quantity)

            print(name,price,quantity)
            print(cart)
            # if not created:
            #     cart.quantity += 1
            #     cart.save()
            #
            # cart=
            # if not created:
            #     cart_items = CartItem.objects.filter(cart=cart, volcano=volcano)  # Change product to volcano
            #     if cart_items.exists():
            #         cart_item = cart_items.first()
            #         cart_item.quantity += quantity
            #         cart_item.save()
            #     else:
            #         cart_item = CartItem.objects.create(cart=cart, volcano=volcano, quantity=quantity)  # Change product to volcano
            # else:
            #     cart_item = CartItem.objects.create(cart=cart, volcano=volcano, quantity=quantity)  # Change product to volcano

        except:
            error_message = "Failed to add item to cart. Please try again later."
            return render(request, 'store/cart.html', {'error_message': error_message})

        carts= Cart.objects.all()
        return render(request, 'store/cart.html', {'carts': carts, })  # Change new_product to new_volcano
    # else:
        # cart = get_object_or_404(Cart, name=request.user)
        # cart_items = CartItem.objects.filter(cart=cart)
        print(cart)
        # return render(request, 'store/cart.html', {'cart_items': cart_items})


@login_required()
def remove_from_cart(request, cart_item_id):
    try:
        cart_item_id = int(cart_item_id)
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
        cart_item.delete()
        return redirect('cart')
    except CartItem.DoesNotExist:
        error_message = "Failed to remove item from cart. Please try again later."
        return render(request, 'store/cart.html', {'error_message': error_message})
    except ValueError:
        error_message = "Invalid cart item ID."
        return render(request, 'store/cart.html', {'error_message': error_message})

