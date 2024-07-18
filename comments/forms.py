# comments/forms.py
from django import forms
from .models import Comment

# Definindo um formulário personalizado para comentários
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Deixe um comentário'}),
        }
