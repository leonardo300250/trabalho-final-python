# contato/models.py
from django.db import models
from django.utils import timezone

# Create your models here.
class Produtos(models.Model):
    imagem = models.ImageField(null=True,blank=True)
    produto = models.CharField(max_length=100,null=True,blank=True)
    categoria = models.CharField(max_length=100,null=True,blank=True)
    descricao = models.TextField(max_length=100,null=True,blank=True)
    em_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos" # Define o nome plural correto
    def __str__(self):
        return self.produto
    
class Parceiros(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100,null=True,blank=True)
    data_parceria = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros" # Define o nome plural correto
    def __str__(self):
        return self.nome

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.IntegerField(max_length=20, verbose_name='Celular', blank=True, null=True)
    assunto = models.CharField(max_length=200)
    descricao = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

class Clientes(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField()
    contato = models.IntegerField(default=0, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes" # Define o nome plural correto
    def __str__(self):
        return self.nome
    
class Adotados(models.Model):
    foto = models.ImageField(null=True,blank=True)
    nome = models.CharField(max_length=100,null=True,blank=True)
    categoria = models.CharField(max_length=100,null=True,blank=True)
    descricao = models.TextField(max_length=100,null=True,blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Adotado"
        verbose_name_plural = "Adotados" # Define o nome plural correto
    def __str__(self):
        return self.adotado