from django.db import models
from src.usuarios.models import Usuario
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

#modelo de la trasaccion    
class Transaccion(models.Model):
    Total =  models.FloatField(verbose_name = "Total de la transaccion")
    DetaMet = models.ForeignKey(DetalleMet,on_delete = models.CASCADE,verbose_name = "Detalle del Metodo")
    
    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
    
    def __str__(self):
        return str(self.Total)

class DetalleTra(models.Model):
    IdTransaccion = models.ForeignKey(Transaccion,on_delete = models.CASCADE,verbose_name = "Transaccion")
    Usuario_id = models.ForeignKey(Usuario,on_delete = models.CASCADE,verbose_name = "Usuario")
    #IdProducto = models.ForeignKey(Producto,on_delete = models.CASCADE,verbose_name = "Producto")
    Fecha = models.DateTimeFlied(verbose_name="Fecha")
    created_at = models.DateTimeField(auto_now_add = True,auto_now = False, verbose_name = "Creado el")
    update_at = models.DateTimeField(auto_now_add = False,auto_now = True,verbose_name = "Actualizado el")

    class Meta:
        verbose_name="Detalle Transaccion"
        vebose_name_plural="Detalles Transacciones"
    
    def __str__(self):
        return str(self.IdTransaccion)


