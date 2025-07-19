from django.contrib import admin # importa la clase admin de Django
from django.urls import path,include# importa las funciones path e include de Django
from productos.views import inicio # importa la vista inicio desde el módulo productos.views


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', inicio, name='inicio'), #ruta para la página de inicio
   path('productos/', include('productos.urls')),  # ruta para las vistas de productos
]

