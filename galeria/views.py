from django.shortcuts import render, get_object_or_404 ## metodo nativo do DJANGO
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all() ## puxando todos os objetos do DB
    return render(request, 'galeria\index.html', {"cards": fotografias}) ## passando as informações puxadas para o navegador

def imagem(request, foto_id): ## recebendo ID que foi passado pelo urls e veio do index.html
    fotografia = get_object_or_404(Fotografia, pk=foto_id) ## usando esse ID que é PK, para puxar as informações do DB
    return render(request, 'galeria\imagem.html', {"fotografia": fotografia}) ## devolvendo as informações buscadas na DB para o navegador
