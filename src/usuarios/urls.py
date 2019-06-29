from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import mostrarP, Home
from .models import UsuarioParametros


urlpatterns = [
    path('login/',LoginView.as_view(template_name='usuario/login/login.html'), name= 'login' ),
    path('mostrarP/',mostrarP, name= 'mostrarP' ),
    path('home/', Home.as_view()),
    # path('registrar/',RegistroUsuario.as_view(), name= 'registro' ),
    
    
]
