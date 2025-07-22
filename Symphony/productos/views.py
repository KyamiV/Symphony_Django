from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Clases
from .forms import ClasesForm



def lista_productos(request):
   productos_list = Clases.objects.all().order_by('-fecha_ultima_modificacion')
   paginator = Paginator(productos_list, 10)
   page = request.GET.get('page', 1)
   try:
       productos = paginator.page(page)
   except (PageNotAnInteger, EmptyPage):
       productos = paginator.page(1)
   return render(request, 'productos/product_list.html', {'productos': productos})


def create_product(request):
   form = ClasesForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})


def edit_product(request, pk):
   prod = get_object_or_404(Clases, pk=pk)
   form = ClasesForm(request.POST or None, instance=prod)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})


def delete_product(request, pk):
   prod = get_object_or_404(Clases, pk=pk)
   if request.method == 'POST':
       prod.delete()
       return redirect('productos:lista')
   return render(request, 'productos/product_confirm_delete.html', {'producto': prod})

#al final de views.py, se define la vista inicio que renderiza la plantilla base.html con un contexto que incluye el nombre de la tienda y una descripción. Esta vista se utiliza para mostrar la página de inicio de la aplicación Symphony.
def inicio(request):
   context = {'tienda': 'Symphony', 'descripcion': '¡Somos una escuela de música que te ayuda a impulsar tu desarrollo musical!'}
   return render(request, 'inicio.html', context)

def ver_clase(request, pk):
    # lógica para mostrar detalles de la clase
    return render(request, 'productos/ver_clase.html')

def inscribirse(request, pk):
    # lógica para inscribir al usuario en la clase
    return render(request, 'productos/inscribirse.html')
