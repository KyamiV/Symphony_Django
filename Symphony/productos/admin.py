from django.contrib import admin
from productos.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad_stock', 'fecha_creacion')
    search_fields = ('nombre',)

admin.site.register(Producto)
# Register your models here.
