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
from django.conf import settings


urlpatterns = [
    path('',LoginView.as_view(template_name='usuario/login/login.html'), name= 'login' ),
    path('home/', TemplateView.as_view(template_name='index.html' ), name='home'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('usuarios/', include('src.usuarios.urls')),
    path('transaccion/', include('src.transaccion.urls'),name="transaccion")
=======
    path('usuarios/', include('src.usuarios.urls'), name='usuarios'),
    path('transaccion/', include('src.transaccion.urls'))
>>>>>>> 0d873f2b703a8bf141299386867264ef293bda7a
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
