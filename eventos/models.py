from django.db import models

class Evento(models.Model):

    CATEGORIAS = [
        ('cultura', 'Cultura'),
        ('esporte', 'Esporte'),
        ('educacao', 'Educação'),
        ('tecnologia', 'Tecnologia'),
        ('musica', 'Música'),
        ('teatro', 'Teatro'),
        ('gastronomia', 'Gastronomia'),
        ('outros', 'Outros'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=200)

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    imagem = models.ImageField(
        upload_to='eventos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo