from django.contrib import admin
from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'), ## recebendo um ID do objeto clicado no index, e passando como parametro para o view buscar e devolver o template da pagina com as informações corretas do DB
    path("buscar", buscar, name="buscar"), #criando um novo path
]
