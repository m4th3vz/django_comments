# Importando classes necessárias do Django
from django import forms
from .models import Comment # Importa a classe Comment de models.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importa formulários de autenticação do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

# Definindo um formulário personalizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Define que o modelo utilizado é o User do Django
        fields = ('username', 'password1', 'password2')  # Define os campos do formulário: username, password1 (senha), password2 (confirmação de senha)

# Definindo um formulário personalizado para autenticação
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')  # Campo para inserir o nome de usuário com o rótulo 'Usuário'
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)  # Campo para inserir a senha com o rótulo 'Senha', usando widget para ocultar a senha durante a digitação

# Definindo um formulário personalizado para comentários
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adicione um comentário...'}),
        }
