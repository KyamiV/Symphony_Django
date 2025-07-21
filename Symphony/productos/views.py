from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
   productos_list = Producto.objects.all().order_by('-fecha_ultima_modificacion')
   paginator = Paginator(productos_list, 10)
   page = request.GET.get('page', 1)
   try:
       productos = paginator.page(page)
   except (PageNotAnInteger, EmptyPage):
       productos = paginator.page(1)
   return render(request, 'productos/product_list.html', {'productos': productos})

def create_product(request):
   form = ProductoForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})

def edit_product(request, pk):
   prod = get_object_or_404(Producto, pk=pk)
   form = ProductoForm(request.POST or None, instance=prod)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})

def delete_product(request, pk):
   prod = get_object_or_404(Producto, pk=pk)
   if request.method == 'POST':
       prod.delete()
       return redirect('productos:lista')
   return render(request, 'productos/product_confirm_delete.html', {'producto': prod})

def inicio(request):
   """Vista para la página de inicio de Symphony"""
   context = {
       'tienda': 'Symphony',
       'descripcion': '¡Somos una escuela de música que te ayuda a impulsar tu desarrollo musical!',
   }
   return render(request, 'base.html', context)

#al final de views.py, se define la vista inicio que renderiza la plantilla base.html con un contexto que incluye el nombre de la tienda y una descripción. Esta vista se utiliza para mostrar la página de inicio de la aplicación Symphony.
def inicio(request):
   context = {'tienda': 'Symphony', 'descripcion': '¡Somos una escuela de música que te ayuda a impulsar tu desarrollo musical!'}
   return render(request, 'inicio.html', context)