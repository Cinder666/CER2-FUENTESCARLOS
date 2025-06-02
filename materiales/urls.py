
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_materiales, name='lista_materiales'),
    path('recomendaciones/', views.lista_recomendaciones, name='lista_recomendaciones'),
]
