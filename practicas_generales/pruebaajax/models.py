from django.db import models

# Create your models here.

class AgregarMateria(models.Model):
    materia = models.CharField('Materia', max_length = 50)
    creditos = models.IntegerField('creditos' ,max_length=2)
    