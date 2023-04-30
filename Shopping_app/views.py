from django.shortcuts import render
from .models import Volcano
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
'''
def store(request):
    # 获取所有的 Volcano 对象
    volcanoes = Volcano.objects.all()
    # 将 volcanoes 对象传递到模板中
    context = {'volcanoes': volcanoes}
    return render(request, 'store/store.html', context)
'''

def store(request):
    # 获取所有的 Volcano 对象
    volcanoes = Volcano.objects.all()
    
    # 使用 Paginator 对象实现分页
    paginator = Paginator(volcanoes, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 将 page_obj 对象传递到模板中
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

