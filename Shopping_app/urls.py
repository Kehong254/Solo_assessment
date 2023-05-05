from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('volcano_detail/<int:Volcano_ID>/', views.volcano_detail, name='volcano_detail'),
    path('cart/remove/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('place_order/', views.place_order, name='place_order'),
    path('create_empty_cart/', views.create_empty_cart, name='create_empty_cart'),
    path('volcano_list/', views.volcano_list, name='volcano_list'),

]