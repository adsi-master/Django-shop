from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# from  django.core.exceptions import ObjectDoesNotExist
from .forms import UParametrosForm, RegistroUserForm
from .models import UsuarioParametros


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/register/register.html"
    form_class = RegistroUserForm
    success_url = reverse_lazy('login')



def mostrarP(request):
    perfil = UsuarioParametros.objects.get(id=request.user.id)
    form = UParametrosForm(instance=perfil)    
    return render(request,'usuario/mostrarP.html',{'form':form})


from django.views.generic import  TemplateView