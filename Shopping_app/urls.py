from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('volcano/<int:Volcano_ID>/', views.volcano_detail, name='volcano_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]