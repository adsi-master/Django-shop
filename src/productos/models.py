from django.db import models

# Create your models here.
class Producto(models.Model):
    lenguaje = models.ForeignKey(Lenguaje, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE) 
    nombres = models.CharField(max_length = 45, verbose_name = "Nombre")
    fecha = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha")
    desProducto = models.CharField(max_length = 80, verbose_name = "Descripción")
    imagen = models.CharField(max_length = 50, verbose_name = "Imagen")
    estado = models.CharField(max_length = 50, verbose_name = "Estado" )
    crated_at = models.DateTimeField(auto_now_add = True, verbose_name = "Registrado el : ")
    updated_at = models.DateTimeField(auto_now_add = True, verbose_name = "Actualizado el : ")

  class meta : 
        verbose_name = "producto"

        verbose_name_plural = "productos"

    def __str__ (self):
        
        return self.nombres

class Lenguaje(models.Model):
    nomLenguaje = CharField(max_length = 45)
    version = CharField(max_length = 45)
    crated_at = models.DateTimeField(auto_now_add = True, verbose_name = "Registrado el : ")
    updated_at = models.DateTimeField(auto_now_add = True, verbose_name = "Actualizado el : ")

    class meta:
        verbose_name = "lenguaje"

        verbose_name_plural = "lenguajes"

    def __str__(self):

        return self.nomLenguaje    
