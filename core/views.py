from django.shortcuts import render, redirect  # Importa funções utilitárias do Django para renderização de templates e redirecionamento
from django.contrib.auth import login, authenticate  # Importa funções de autenticação do Django
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CommentForm  # Importa os formulários personalizados definidos na sua aplicação
from django.contrib.auth.decorators import login_required  # Importa o decorator para exigir login
from .models import Comment

# Página principal
def index(request):
    return render(request, 'index.html')  # Renderiza o template 'index.html' ao receber uma requisição GET

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
    return render(request, 'comments.html', {'form': form, 'comments': comments})

# Página de registro
def register_view(request):
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        form = CustomUserCreationForm(request.POST)  # Instancia o formulário de criação de usuário personalizado com os dados da requisição
        if form.is_valid():  # Verifica se o formulário é válido
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Autentica o usuário recém-criado
            return redirect('index')  # Redireciona para a página principal ('index') após o registro bem-sucedido
    else:
        form = CustomUserCreationForm()  # Caso a requisição não seja POST, cria um novo formulário de registro vazio
    return render(request, 'register.html', {'form': form})  # Renderiza o template 'register.html' com o formulário de registro

# Página de login
def login_view(request):
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        form = CustomAuthenticationForm(request, data=request.POST)  # Instancia o formulário de autenticação personalizado com os dados da requisição
        if form.is_valid():  # Verifica se o formulário é válido
            username = form.cleaned_data.get('username')  # Obtém o nome de usuário do formulário validado
            password = form.cleaned_data.get('password')  # Obtém a senha do usuário do formulário validado
            user = authenticate(request, username=username, password=password)  # Autentica o usuário com base no nome de usuário e senha fornecidos
            if user is not None:  # Verifica se a autenticação foi bem-sucedida
                login(request, user)  # Realiza o login do usuário
                return redirect('index')  # Redireciona para a página principal ('index') após o login bem-sucedido
    else:
        form = CustomAuthenticationForm()  # Caso a requisição não seja POST, cria um novo formulário de login vazio
    return render(request, 'login.html', {'form': form})  # Renderiza o template 'login.html' com o formulário de login
