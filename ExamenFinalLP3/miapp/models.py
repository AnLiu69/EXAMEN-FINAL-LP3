from django.db import models

# Create your models here.
class Flores_Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.TextField()
    sexo = models.CharField(max_length=100)
    # auto_now_add me permitirá registrar
    # la fecha cuando cree el registro
    fecha_registro = models.DateTimeField(auto_now_add=True)