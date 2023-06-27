from django.db import models

# Create your models here.
class Suscriptor(models.Model):
    email = models.EmailField(max_length = 50)
    nombre = models.CharField(max_length = 30, primary_key=True)
