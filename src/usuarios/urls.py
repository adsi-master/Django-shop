from django.urls import path

from .views import mostrarP
from .views import mostrarP, RegistroUsuario
from .models import UsuarioParametros


urlpatterns = [
    path('mostrarP/',mostrarP, name= 'mostrarP' ),
    path('registrar/',RegistroUsuario.as_view(), name= 'registrarse' ),
    
    
]
# password2 username
