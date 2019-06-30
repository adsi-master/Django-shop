"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',LoginView.as_view(template_name='usuario/login/login.html'), name= 'login' ),
    path('home/', TemplateView.as_view(template_name='index.html' ), name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('src.usuarios.urls'), name='usuarios'),
    path('transaccion/', include('src.transaccion.urls'))
]
