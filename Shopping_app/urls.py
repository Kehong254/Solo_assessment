from django.urls import path
from . import views

urlpatterns = [
  path('', views.store, name="store"),
  path('cart/', views.cart, name="cart"),
  path('checkout/', views.checkout, name="checkout"),
  path('volcano/<int:Volcano_ID>/', views.volcano_detail, name='volcano_detail'),
]
