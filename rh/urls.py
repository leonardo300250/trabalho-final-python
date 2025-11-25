from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('',views.home, name='home'),
    path('adotados/',views.adotados, name='adotados'),
    path('clientes/',views.clientes, name='clientes'),
    path('parceiros/',views.parceiros, name='parceiros'),
    path('contatos/', views.contatos, name='contatos'),


   # A URL para a página do formulário
    # Ex: http://127.0.0.1:8000/contato/
    path('contato/', views.formulario_contato_view, name='contatos'),
    
    # A URL para onde o usuário é enviado após o sucesso
    # Ex: http://127.0.0.1:8000/contato/sucesso/
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]
    
