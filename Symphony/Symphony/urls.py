from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # 👈 importar vistas de autenticación
from productos import views
from productos.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('productos/', include('productos.urls')),
    path('clases/<int:pk>/', views.ver_clase, name='ver_clase'),
    path('clases/<int:pk>/inscribirse/', views.inscribirse, name='inscribirse'),

    # Rutas para login y logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

