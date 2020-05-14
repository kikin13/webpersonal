from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200) # Campo de caracteres
    description = models.TextField()  # Campo de texto.
    image = models.ImageField()  # Campo de imagen.
    created = models.DateTimeField(auto_now_add=True) # Este campo de fecha se guarda automaticamente cuando se crea
    updated = models.DateTimeField(auto_now=True) # Se guarada cada ves que se modifica o actualiza