from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):

    CATEGORIAS = [
        ('SHOW', 'Show'),
        ('FEIRA', 'Feira'),
        ('TEATRO', 'Teatro'),
        ('EXPOSICAO', 'Exposição'),
        ('RELIGIOSO', 'Religioso'),
        ('OUTRO', 'Outro')
    ]

    titulo = models.CharField(max_length=100)

    descricao = models.TextField()

    local = models.CharField(max_length=150)

    data = models.DateField()

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    imagem = models.ImageField(
        upload_to='eventos/',
        blank=True,
        null=True
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo