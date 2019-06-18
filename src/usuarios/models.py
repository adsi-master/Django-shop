from django.db import models
from src.usuariosparametros.models import TipoDocumento, TipoUsuario, Titulo

class Usuario(models.Model):  
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    token = models.CharField('token', max_length=50)
    alias = models.CharField(max_length =50, verbose_name = "Nombre Alias", unique=True)
    contaseña = models.CharField(max_length = 50, default = "", verbose_name = "Contraseña")
    correo = models.CharField(max_length = 50, default = "@", verbose_name = "Correo Electronico")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name = "Registrado el : ")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name = "Actualizado el : ")

    class meta:        
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.alias 

class DatosUsuario(models.Model): 
    usuario_id = models.OneToOneField(Usuario, on_delete = models.CASCADE, verbose_name ="Identificacion del Usuario")
    titulo_nombre = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    tipodocumento_id = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    nombres = models.CharField(max_length = 50, verbose_name = "Nombres")
    apellido = models.CharField(max_length = 50, verbose_name = "Apellidos")
    documento = models.CharField(max_length = 50, verbose_name = "No. Documento")
    telefono = models.CharField(max_length = 50, default = "0", verbose_name = "No. Telefono")
    edad = models.CharField(max_length = 50, default = "0", verbose_name = "Edad")
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name = "Registrado el : ")
    update_ad = models.DateTimeField(auto_now_add=True, verbose_name = "Actualizado el : ")

    class meta:
        verbose_name = "Dato Usuario"
        verbose_name_plural = "Datos Usuarios"

    def __str__(self):
        return self.nombres