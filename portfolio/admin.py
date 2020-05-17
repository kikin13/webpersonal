from django.contrib import admin
from .models import Proyect

# Creamos una configuracion extemdida 
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Mostramos estos dos campos de solo lectura



# Register your models here.
admin.site.register(Proyect, ProyectAdmin) #Añadimos la configuracion extendido al model