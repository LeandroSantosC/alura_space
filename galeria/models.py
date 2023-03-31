from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    opcoes_categorias = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categorias, default='') #criando uma nova categoria do DB, lembrar de dar makemigrations dnv
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) #criando uma imagefield
    publicada = models.BooleanField(default=False) #criando função de publicação
    data_pub = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
    

