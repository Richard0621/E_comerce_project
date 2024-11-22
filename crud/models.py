from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_original = models.FloatField()
    precio_descuento = models.FloatField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    nuevo = models.BooleanField()
    fecha_creacion = models.DateField(auto_now=True)
    imagen = models.FileField(upload_to="crud/")


    def __str__(self):
        return self.nombre