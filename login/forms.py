from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Perfil con direccion/telefono

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    direccion = forms.CharField(max_length=200, required=True)
    telefono = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = [
            'username',    # nombre de usuario
            'email',       # correo
            'password1',   # contraseña
            'password2',   # confirmación contraseña
            'direccion',   # campo extra para Profile
            'telefono',    # campo extra para Profile
        ]

    def save(self, commit=True):
        # Guardamos primero el usuario
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Luego creamos el Profile asociado
            Profile.objects.create(
                user=user,
                direccion=self.cleaned_data['direccion'],
                telefono=self.cleaned_data['telefono']
            )
        return user
