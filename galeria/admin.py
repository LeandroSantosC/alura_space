from django.contrib import admin
from galeria.models import Fotografia

class ListaFotografias(admin.ModelAdmin): ##herdando uma classe do django para criar uma lista para ser visualizada no admin
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome") ##definindo os itens que serão links
    search_fields = ("nome",) ##criando uma barra de busca
    list_filter = ("categoria",) #criando filtro de categoria
    list_editable = ("publicada",) #criando botao de publicada
    list_per_page = 10 #linhas por pagina
    

admin.site.register(Fotografia, ListaFotografias) ##registrando o DB no admin
