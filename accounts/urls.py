from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),  # Update view function name to user_login
    path('logout/', views.logout_view, name='logout_view'),  # Update view function name to user_logout
    path('register/', views.register, name='register'),  # Update view function name to user_register
]