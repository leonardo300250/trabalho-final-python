from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Funcionarios
from .forms import ContatoModelForm
from .models import Produtos
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Vai para o login após criar conta
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def home(request):
    products = Produtos.objects.filter(em_estoque=True)
    return render(request, 'home.html', {'products': products})

def produtos(request):
    lista_produtos = Produtos.objects.filter(em_estoque=True)
    context = {
        'products': lista_produtos
    }
    return render(request, 'produtos.html', context)
def clientes(request):
    return render(request,'clientes.html')
def contatos(request):
    return render(request, 'contatos.html')
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

# A view principal do formulário
def formulario_contato_view(request):
    if request.method == 'POST':
        # Cria a instância do formulário com os dados vindos do request
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            # A MÁGICA DO MODELFORM:
            # form.save() cria e salva um novo objeto 'MensagemContato'
            # no banco de dados com os dados do formulário.
            form.save()
            
            # Redireciona para uma página de sucesso
            return redirect('contato_sucesso')
    
    else:
        # Se for um GET, apenas cria um formulário vazio
        form = ContatoModelForm()

    # Passa o formulário (vazio ou com erros) para o template
    return render(request, 'contato/contatos.html', {'form': form})


# Uma view simples para a página de "sucesso"
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')