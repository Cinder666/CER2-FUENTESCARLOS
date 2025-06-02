from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registro pide todos los datos
    path('registro/', views.registro, name='registro'),

    # Login solo pide usuario y contraseña (usa AuthenticationForm por defecto)
    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),

    
    


    path('logout/', views.cerrar_sesion, name='logout'),
]
