from django.db import models
from atracoes.models import atracao
from comentarios.models import comentario
from avaliacoes.models import avaliacoes
from endereco.models import endereco

class pontoturistico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(atracao)
    comentario = models.ManyToManyField(comentario)
    avaliacoes = models.ManyToManyField(avaliacoes)
    endereco = models.ForeignKey(endereco, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.nome


# Create your models here.
