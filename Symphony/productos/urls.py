# productos/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clases/', views.lista_productos, name='lista'),
    path('clases/<int:pk>/', views.ver_clase, name='ver_clase'),
    path('clases/<int:pk>/inscribirse/', views.inscribirse, name='inscribirse'),
    path('clases/crear/', views.create_product, name='crear'),
    path('clases/editar/<int:pk>/', views.edit_product, name='editar'),
    path('clases/eliminar/<int:pk>/', views.delete_product, name='eliminar'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='productos:login'), name='logout'),
]