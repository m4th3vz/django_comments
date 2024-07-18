# comments/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from django.utils import timezone

# Página principal
def index(request):
    return render(request, 'comments/index.html')

# Página de comentários
@login_required
def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm()
    
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comments.html', {'form': form, 'comments': comments})

# Excluir comentário
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments')

# Editar comentário
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.edited_at = timezone.now()
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/comments.html', {'form': form, 'comments': Comment.objects.all().order_by('-created_at')})