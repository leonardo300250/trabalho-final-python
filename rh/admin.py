from django.contrib import admin
from .models import Parceiros, MensagemContato, Produtos, Clientes, Adotados

@admin.register(Parceiros)
class ParceirosAdmin(admin.ModelAdmin):
    # Quais colunas mostrar na lista de produtos
    list_display = ('nome','descricao', 'data_parceria','status',)
    # Por quais campos podemos buscar
    search_fields = ("nome",)
    # Quais campos podemos filtrar
    list_filter = ('status', 'data_parceria',)
    
# admin.site.register(Funcionarios)

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido',)
    list_filter = ('lido', 'data_envio',)
    search_fields = ('nome', 'email', 'assunto',)

@admin.register(Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('imagem','produto','categoria','descricao',)
    search_fields = ('produto', 'categoria',)

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','email','contato',)
    search_fields = ('nome','contato',)

@admin.register(Adotados)
class AdotadosAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria')
    search_fields = ('nome','categoria')
    