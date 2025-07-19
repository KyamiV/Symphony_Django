from django.urls import path
from. import views

app_name = "productos"  # Nombre del espacio de nombres de la aplicación

urlpatterns = [  # Definimos las rutas de la aplicación productos
    path('', views.lista_productos, name='lista'),  # Ruta para la lista de productos
    path('nuevo/', views.create_product, name='nuevo'),  # Ruta para crear un nuevo producto
    path('editar/<int:pk>/', views.edit_product, name='editar'),  # Ruta para editar un producto existente
    path('eliminar/<int:pk>/', views.delete_product, name='eliminar'),  # Ruta para eliminar un producto
]