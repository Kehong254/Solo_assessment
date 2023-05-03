from django.urls import path
from . import views

urlpatterns = [
  path('', views.store, name="store"),
  path('volcano/<int:Volcano_ID>/', views.volcano_detail, name='volcano_detail'),
]
