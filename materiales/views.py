from django.shortcuts import render
from .models import Material

def lista_materiales(request):
   
    return render(request, 'materiales/lista_materiales.html',)

def lista_recomendaciones(request):
    return render(request, 'materiales/recomendaciones.html')
