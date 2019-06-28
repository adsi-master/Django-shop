from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import mostrarP, RegistroUsuario
from .models import UsuarioParametros

urlpatterns = [
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name= 'pablo-chupa' ),
    path('mostrarP/',mostrarP, name= 'mostrarP' ),
    path('registrar/',RegistroUsuario.as_view(), name= 'registro' ),
    
    
]
