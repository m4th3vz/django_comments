# comments/urls.py
from django.urls import path
from .views import IndexView, CommentsView, DeleteCommentView, EditCommentView

urlpatterns = [
    # Página principal
    path('', IndexView.as_view(), name='index'),
    # Página de comentários
    path('comments/', CommentsView.as_view(), name='comments'),
    # Caminho de exclusão
    path('delete_comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),
    # Caminho de edição
    path('edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
]
