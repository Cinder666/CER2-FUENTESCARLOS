from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SolicitudForm
from .models import Solicitud

@login_required
def nueva_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.ciudadano = request.user
            solicitud.save()
            return redirect('lista_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/nueva_solicitud.html', {'form': form})

@login_required
def lista_solicitudes(request):
    solicitudes = Solicitud.objects.filter(ciudadano=request.user)
    return render(request, 'solicitudes/lista_solicitudes.html', {'solicitudes': solicitudes})


from django.db.models import Sum
from materiales.models import Material


def cantidad_por_material(request):
    # Agregamos la suma de 'cantidad' agrupada por cada material
    datos = (
        Solicitud.objects
        .values('material__codigo', 'material__nombre')
        .annotate(total_rec=Sum('cantidad'))
        .order_by('-total_rec')
    )
    
    
    return render(request, 'solicitudes/metrica.html', {'datos': datos})

