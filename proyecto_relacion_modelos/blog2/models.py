
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

# Create your models here.
