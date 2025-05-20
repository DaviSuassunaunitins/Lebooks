from django.db import models

# Create your models here.
class Livros(models.Model):
    GENEROS = [
        ('ROM', 'Romance'),
        ('FIC', 'Ficção'),
        ('REL', 'Religioso'),
        ('INF', 'Infantil'),
        ('JUV', 'Juvenil'),
        ('NFC', 'Não Ficção'),
        ('SUS', 'Suspense'),
        ('TER', 'Terror'),
    ]

    título = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    páginas = models.IntegerField()
    ano = models.IntegerField()
    gênero_1 = models.CharField(max_length=3, choices=GENEROS)
    gênero_2 = models.CharField(max_length=3, choices=GENEROS)
    gênero_3 = models.CharField(max_length=3, choices=GENEROS)
    disponível = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.título