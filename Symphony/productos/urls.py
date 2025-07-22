from django.contrib.auth import views as auth_views
from django.urls import path
from. import views

app_name = "productos"  # Nombre del espacio de nombres de la aplicación

urlpatterns = [  # Definimos las rutas de la aplicación productos
    path('', views.inicio, name='inicio'),
    path('clases/', views.lista_productos, name='lista'),  # Ruta para la lista de productos
    path('nuevo/', views.create_product, name='nuevo'),  # Ruta para crear un nuevo producto
    path('editar/<int:pk>/', views.edit_product, name='editar'),  # Ruta para editar un producto existente
    path('eliminar/<int:pk>/', views.delete_product, name='eliminar'),  # Ruta para eliminar un producto
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]