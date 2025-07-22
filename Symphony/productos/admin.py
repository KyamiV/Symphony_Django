from django.contrib import admin
from productos.models import Clases

# Opcional: configuración personalizada para Clases
class ClasesAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'profesor', 'horario', 'fecha_ultima_modificacion')
    search_fields = ('instrumento', 'profesor')

# Registrar modelos en el panel de administración
admin.site.register(Clases, ClasesAdmin)

