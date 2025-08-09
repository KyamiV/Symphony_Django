# productos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Clases
from .forms import ClasesForm

def inicio(request):
    context = {
        'tienda': 'Symphony',
        'descripcion': '¡Somos una escuela de música que te ayuda a impulsar tu desarrollo musical!'
    }
    return render(request, 'inicio.html', context)

def lista_productos(request):
    productos_list = Clases.objects.all().order_by('-fecha_ultima_modificacion')
    paginator = Paginator(productos_list, 10)
    page = request.GET.get('page', 1)
    try:
        productos = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        productos = paginator.page(1)

    return render(request, 'productos/product_list.html', {
        'clases': productos
    })

def create_product(request):
    form = ClasesForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Clase guardada exitosamente.")
        return redirect('productos:lista')
    return render(request, 'productos/product_form.html', {'form': form})

def edit_product(request, pk):
    prod = get_object_or_404(Clases, pk=pk)
    form = ClasesForm(request.POST or None, instance=prod)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Clase actualizada correctamente.")
        return redirect('productos:lista')
    return render(request, 'productos/product_form.html', {'form': form})

def delete_product(request, pk):
    prod = get_object_or_404(Clases, pk=pk)
    if request.method == 'POST':
        prod.delete()
        messages.success(request, "Clase eliminada exitosamente.")
        return redirect('productos:lista')
    return render(request, 'productos/product_confirm_delete.html', {'producto': prod})

def ver_clase(request, pk):
    return render(request, 'productos/ver_clase.html')

def inscribirse(request, pk):
    return render(request, 'productos/inscribirse.html')