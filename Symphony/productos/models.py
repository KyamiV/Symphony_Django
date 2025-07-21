from django.db import models # Symphony/productos/models.py

class Producto(models.Model): # Modelo de producto
    
    nombre = models.CharField(max_length=100) # Nombre del producto
    descripcion = models.TextField() # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.PositiveIntegerField (default=0) #Cantidad en stock
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Fecha de creación del producto
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True) # Fecha de actualización del producto

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos' # Nombre de la tabla en la base de datos
        verbose_name = "Persona" # Nombre singular del modelo
        verbose_name_plural = "Gestión de personas"
