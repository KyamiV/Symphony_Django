from django import forms # importando el módulo de formularios de Django
from .models import Producto # Importando el modelo Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  # Especificando el modelo a usar
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_stock']  # Campos del formulario