from django.urls import path  # Importa a função path do módulo django.urls
from . import views  # Importa as views definidas no diretório views.py
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django com um alias 'auth_views'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    # Página de comentários
    path('comments/', views.comments, name='comments'),
    # Página de registro
    path('register/', views.register_view, name='register'),  
    # Página de login
    path('login/', views.login_view, name='login'),
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
