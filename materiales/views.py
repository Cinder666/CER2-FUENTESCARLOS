from django.shortcuts import render
from .models import Material

def lista_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'materiales/lista_materiales.html', {'materiales': materiales})

def lista_recomendaciones(request):
    return render(request, 'materiales/recomendaciones.html')
