from .models import Volcano
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Volcano, cart
from django.contrib.auth.decorators import login_required


#ignore warning of query
import warnings
from django.core.paginator import UnorderedObjectListWarning

warnings.simplefilter('ignore', UnorderedObjectListWarning)


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

        
@login_required
def add_to_cart(request):
    try:
        if request.method == 'POST':
            Volcano_Name = request.POST['Volcano_Name']
            price = float(request.POST['price'])
            quantity = int(request.POST['quantity'])
            cart_item, created = cart.objects.get_or_create(
                Volcano_Name=Volcano_Name,
                price=price,
                defaults={'quantity': quantity },
            )
            if not created:
                cart_item.quantity = quantity
                cart_item.save()
            cart_items = cart.objects.all()
            total_price = sum([item.price * item.quantity for item in cart_items])
            print(f"cart_items: {cart_items}") 
            return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})
        else:
            cart_items = cart.objects.all()
            total_price = sum([item.price * item.quantity for item in cart_items])
            print(f"cart_items: {cart_items}")
            return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    except Exception as e:
        # Handle any exception that might occur
        return render(request, 'store/error.html', {'error': str(e)})




