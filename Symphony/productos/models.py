# productos/models.py
from django.db import models

INSTRUMENTOS_OPCIONES = [
    ('guitarra', 'Guitarra'),
    ('piano', 'Piano'),
    ('violin', 'Violín'),
    ('bateria', 'Batería'),
    ('flauta', 'Flauta'),
    ('otro', 'Otro'),
]

class Clases(models.Model):
    instrumento = models.CharField(
        max_length=100,
        choices=INSTRUMENTOS_OPCIONES,
        default='otro'
    )
    profesor = models.CharField(max_length=100, default="Sin asignar")
    horario = models.CharField(max_length=100, default="Pendiente")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cupos = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clases'