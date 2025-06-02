
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .forms import RegistroForm

def home(request):
    return render(request, 'login/home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asignar al grupo 'Ciudadano'
            grupo_ciudadano, _ = Group.objects.get_or_create(name='Ciudadano')
            user.groups.add(grupo_ciudadano)

            # Autologin tras registro para que la sesión se cambie al nuevo usuario
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            usuario_autenticado = authenticate(request, username=username, password=raw_password)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('home')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'login/registro.html', {'form': form})



def cerrar_sesion(request):
    logout(request)
    return redirect('login')

