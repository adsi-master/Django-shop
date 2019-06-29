from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< HEAD
from .views import mostrarP, Home
=======
from .views import mostrarP, RegistroUsuario
>>>>>>> 7c7bcc5be620524393232a5801248c2a67ad0647
from .models import UsuarioParametros


urlpatterns = [
    path('login/',LoginView.as_view(template_name='usuario/login/login.html'), name= 'login' ),
    path('mostrarP/',mostrarP, name= 'mostrarP' ),
<<<<<<< HEAD
    path('home/', Home.as_view()),
    # path('registrar/',RegistroUsuario.as_view(), name= 'registro' ),
=======
    path('registrar/',RegistroUsuario.as_view(), name= 'registro' ),
>>>>>>> 7c7bcc5be620524393232a5801248c2a67ad0647
    
    
]
