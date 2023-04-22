from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() #Nos devuelve la lista de todos los proyectos
    return render(request, "portfolio/portfolio.html", {'projects':projects})





