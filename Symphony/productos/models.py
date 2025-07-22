from django.db import models

class Clases(models.Model):
    instrumento = models.CharField(max_length=100, default="Por definir")
    profesor = models.CharField(max_length=100, default="Sin asignar")
    horario = models.CharField(max_length=100, default="Pendiente")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad_stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clases'