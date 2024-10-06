from django.shortcuts import render

from .models import Coche
from .models import Propietario

# Create your views here.

def coche_list(request):
    coches = Coche.objects.all()
    return render(request, 'blog/coche_list.html', {'coches_mostrar': coches})

def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(request, 'blog/propietario_list.html', {'propietarios_mostrar': propietarios})