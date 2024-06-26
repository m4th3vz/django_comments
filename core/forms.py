# Importando classes necessárias do Django
from django import forms
from .models import Comment # Importa a classe Comment de models.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importa formulários de autenticação do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

# Definindo um formulário personalizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

# Definindo um formulário personalizado para autenticação
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)  # widget para ocultar a senha durante a digitação

# Definindo um formulário personalizado para comentários
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicione um comentário...'}),
        }
