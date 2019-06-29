from django.shortcuts import render, HttpResponse,redirect
# Create your views here.

from  django.core.exceptions import ObjectDoesNotExist

from .forms import UParametrosForm
from .models import UsuarioParametros
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# class RegistroUsuario(CreateView):
#     model = User
#     template_name = "usuario/Registrar.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy('mostrarP')



def mostrarP(request):
    perfil = UsuarioParametros.objects.get(id=request.user.id)
    form = UParametrosForm(instance=perfil)    
    return render(request,'usuario/mostrarP.html',{'form':form})


from django.views.generic import  TemplateView

class Home(TemplateView):
    template_name= 'index.html' 