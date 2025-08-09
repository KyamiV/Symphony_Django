# productos/forms.py
from django import forms
from .models import Clases

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ['instrumento', 'profesor', 'horario', 'precio', 'cupos']
        widgets = {
            'instrumento': forms.Select(attrs={'class': 'form-control'}),
            'profesor': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
            'cupos': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 50,
                'placeholder': 'Cantidad de cupos disponibles',
                'required': 'required'
            }),
        }