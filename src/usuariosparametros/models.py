from django.db import models

from django.db import models

class TipoUsuario(models.Model):
    nombre = models.CharField("Nomnbre Tipo usuario", max_length=50)

    class meta:
        verbose_name = "Tipo Ususario"
        verbose_name_plural = "Tipos de usuario"

    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    nombre = models.CharField("Nomnbre Tipo Documento", max_length=50)

    class Meta:
        verbose_name="Tipo de documento"
        verbose_name_plural="Tipos de documento"

    def __str__(self):
        return self.nombre

class Titulo(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre Título")
    
    class Meta:
        verbose_name="Título"
        verbose_name_plural="Títulos"
    
    def __str__(self):
        return self.nombre