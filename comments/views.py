# comments/views.py
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from .forms import CommentForm
from django.utils import timezone

# Página principal
class IndexView(TemplateView):
    template_name = 'comments/index.html'

# Página de comentários
class CommentsView(LoginRequiredMixin, FormView):
    template_name = 'comments/comments.html'
    form_class = CommentForm
    success_url = '/comments/'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context

# Excluir comentário
class DeleteCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, user=request.user)
        comment.delete()
        return redirect('comments')

# Editar comentário
class EditCommentView(LoginRequiredMixin, FormView):
    template_name = 'comments/comments.html'
    form_class = CommentForm
    success_url = '/comments/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Comment, id=self.kwargs['comment_id'], user=self.request.user)
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.edited_at = timezone.now()
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        return context
