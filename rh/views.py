from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Parceiros
from .forms import ContatoModelForm
from .models import Produtos
from .models import Adotados
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
    filtro_categoria = request.GET.getlist("categoria")  # pega categorias selecionadas
    products = Produtos.objects.filter(em_estoque=True)

    if filtro_categoria:
        products = products.filter(categoria__in=filtro_categoria)

    categorias = Produtos.objects.values_list("categoria", flat=True).distinct()

    context = {
        'products': products,
        'filtro_categoria': filtro_categoria,
        'categorias': categorias
    }
    return render(request, 'home.html', context)


def adotados(request):
    lista_adotados = Adotados.objects.filter(status=True)
    context = {
        'adotados': lista_adotados
    }
    return render(request, 'adotados.html', context)

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

def parceiros(request):
    parceiros = Parceiros.objects.filter(status=True)
    context = {
        'parceiros': parceiros
    }
    return render(request,'parceiros.html',context)

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