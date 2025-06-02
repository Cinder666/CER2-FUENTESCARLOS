from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_solicitudes, name='lista_solicitudes'),
    path('nueva/', views.nueva_solicitud, name='nueva_solicitud'),
    path('metrica/', views.cantidad_por_material, name='metrica'),
]


