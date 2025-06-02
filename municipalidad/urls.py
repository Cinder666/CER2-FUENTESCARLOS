"""
URL configuration for municipalidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.home, name='home'),
    path('', include('login.urls')),
    path('materiales/', include('materiales.urls')),
    path('solicitudes/', include('solicitudes.urls')),
]
