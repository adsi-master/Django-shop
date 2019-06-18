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
    usuario_id = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name ="Identificacion del Usuario")
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