from django.shortcuts import render
# Importar modelos creados
from .models import Proyect

# Create your views here.
def portfolio(request):
    projects = Proyect.objects.all()  #lisra todos los proyectos creados
    return render(request, "portfolio/portfolio.html", {'projects':projects})