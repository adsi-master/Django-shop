from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import User

# modelo usuario incluye los campos de:
# username, firstname, lastname, email, password, groups... 

# Se crea la clase TipoDocumento :
class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo de docuemnto'
        verbose_name_plural = 'Tipos de documentos'

    def __str__(self):
        return self.nombre

# Se crea la clase Genero :
class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.genero

# Se crea la clase EstadoCivil :
class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Tipos de Estados Civiles'

    def __str__(self):
        return self.estado

# Se crea la clase UsuarioParametro :
class UsuarioParametros(models.Model):
    id=models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, blank=True, null=True) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True, blank=True, null=True)
    estasdocivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, blank=True, null=True) 
    genero = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    class Meta:
        verbose_name = 'Perfil usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def __str__(self):
        return self.usuario.username

def create_profile(sender, **kwargs):
    #si el usuario es creado..
    if kwargs['created']:
        #crea instancia de perfildeusuario
        UsuarioParametros.objects.create(usuario=kwargs['instance'])

post_save.connect(create_profile, sender=User)


