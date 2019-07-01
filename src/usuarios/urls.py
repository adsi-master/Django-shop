from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import mostrarPerfil, EditarPerfil
from .views import RegistroUsuario



urlpatterns = [
    path('perfil/',mostrarPerfil, name= 'mostrarP' ),
    path('editar/',EditarPerfil.as_view(), name= 'profile' ),
    path('registrar/',RegistroUsuario.as_view(), name= 'registrarse' ),
    
    
]




