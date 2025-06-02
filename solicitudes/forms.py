from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['material', 'cantidad', 'fecha_estimada']  
        widgets = {
            'material': forms.Select(attrs={'class': 'form-select'}), 
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'fecha_estimada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
