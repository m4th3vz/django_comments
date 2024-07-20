# login/urls.py
from django.urls import path
from .views import RegisterView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página de registro
    path('register/', RegisterView.as_view(), name='register'),
    # Página de login
    path('login/', LoginView.as_view(), name='login'),
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
