from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import mostrarP,crearP,editarP,eliminarP
from .models import UsuarioParametros

urlpatterns = [
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name= 'pablo-chupa' ),
    path('mostrarP/',mostrarP, name= 'mostrarP' ),
    path('crearP/',crearP, name= 'crearP' ),
    path('editarP/<int:documento>',editarP, name= 'editarP' ),
    path('eliminarP/<int:documento>',eliminarP, name= 'eliminarP' ),
    
]
