from django.db import models

# Create your models here.
class MetodoPago(models.Model):
    nombMetPago = models.CharField(max_length = 45,default = "",verbose_name = "Nombre método de pago")

    class Meta:
        verbose_name = "Método de pago"
        verbose_name_plural = "Métodos de pago"
    
    def __str__(self):
        return self.nombMetPago

class DetalleMet(models.Model):
    IdMetodo = models.ForeignKey(MetodoPago,on_delete = models.CASCADE,verbose_name = "Método de pago")
    valor = models.FloatField(verbose_name = "Valor")
    created_at = models.DateTimeField(auto_now_add = True,auto_now = False, verbose_name = "Creado el")
    update_at = models.DateTimeField(auto_now_add = False,auto_now = True,verbose_name = "Actualizado el")
    class Meta:
        verbose_name = "Detalle método"
        verbose_name_plural = "Detalles métodos"
    
    def __str__(self):
        return str(self.IdMetodo)