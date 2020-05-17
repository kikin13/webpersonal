from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen", upload_to="proyects") 
    link = models.URLField(verbose_name="Dirección web",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated =models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
# Con la subclase meta aregamos metadatos.
    class Meta:
        verbose_name = "proyecto" # Cambiamos el nombre del pryecto 
        verbose_name_plural = "proyectos"
        ordering = ["-created"]    # Ordenamos los proyectos por fecha de creacion de mas nuevos a antiguos.

# Mostramos el titulo de nuestro proyecto
    def __str__(self):
        return self.title

