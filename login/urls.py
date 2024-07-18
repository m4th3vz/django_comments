# login/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página de registro
    path('register/', views.register_view, name='register'),
    # Página de login
    path('login/', views.login_view, name='login'),
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
