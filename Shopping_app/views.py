from django.shortcuts import render
from .models import Volcano
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
#ignore warning of query
import warnings
from django.core.paginator import UnorderedObjectListWarning

warnings.simplefilter('ignore', UnorderedObjectListWarning)


def store(request):
    query = request.GET.get('query')
    volcanoes = Volcano.objects.all()
    if query:
        volcanoes = Volcano.objects.filter(Q(Volcano_Name__icontains=query) | Q(Country__icontains=query) | Q(Volcano_Type__icontains=query)).order_by('-Volcano_ID')
    paginator = Paginator(volcanoes, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
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

