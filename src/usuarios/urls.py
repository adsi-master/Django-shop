from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import mostrarPerfil, EditarPerfil, RegistroUsuario, Home
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('perfil/',mostrarPerfil, name= 'mostrarP' ),
    path('editar/',EditarPerfil.as_view(), name= 'profile' ),
    path('registrar/',RegistroUsuario.as_view(), name= 'registrarse' ),
    path('inicio/',Home.as_view(), name= 'home' ),
    path('exit/', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name= 'salir' ),
]


