from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UParametrosForm, RegistroUserForm
from .models import UsuarioParametros



class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/register/register.html"
    form_class = RegistroUserForm
    success_url = reverse_lazy('home')
    
@method_decorator(login_required, name='dispatch')
class EditarPerfil(UpdateView):
    form_class = UParametrosForm
    success_url = reverse_lazy('mostrarP')
    template_name = 'usuario/editarP.html'

    def get_object(self):
        #recuperar el objeto que se va a editar
        profile, created = UsuarioParametros.objects.get_or_create(usuario = self.request.user)
        return profile



def mostrarPerfil(request):
    perfil = UsuarioParametros.objects.get(id=request.user.id)   
    return render(request,'usuario/mostrarP.html',{'perfil':perfil})

class Home(TemplateView):
    template_name='index.html'


