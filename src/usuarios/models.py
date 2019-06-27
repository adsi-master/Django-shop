from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import User

# modelo usuario incluye los campos de:
# username, firstname, lastname, email, password, groups... 

class UsuarioParametros(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipodocumento = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=100, default="")
    Apellido = models.CharField(max_length=100, default="")
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    documento = models.CharField(max_length=50,  primary_key=True) 
    estasdocivil = models.CharField(max_length=50) 
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
