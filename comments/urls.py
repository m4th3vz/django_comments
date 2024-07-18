# comments/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import comments, delete_comment, edit_comment

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    # Página de comentários
    path('comments/', views.comments, name='comments'),
    # Caminho de exclusão
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    # Caminho de edição
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
]
