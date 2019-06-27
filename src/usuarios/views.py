from django.shortcuts import render, HttpResponse,redirect
# Create your views here.

from  django.core.exceptions import ObjectDoesNotExist

from .forms import UParametrosForm
from .models import UsuarioParametros

def crearP(request):
    if request.method == 'POST':
        uparametros_form = UParametrosForm(request.POST)
        if uparametros_form.is_valid():
            uparametros_form.save()
            return redirect('mostrarP')
     
    else:
        uparametros_form = UParametrosForm()
    return render(request, 'usuario/editarP.html',{'uparametros_form': uparametros_form})

def editarP(request,documento):
    uparametros_form = None
    error = None
    try:
        perfil = UsuarioParametros.objects.get(documento = documento)
        if request.method == 'GET':
            uparametros_form = UParametrosForm(instance = perfil)
        else:
            uparametros_form = UParametrosForm(request.POST, instance = perfil)
            if uparametros_form.is_valid():  
                uparametros_form.save()
            return redirect('mostrarP')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'usuario/editarP.html',{'uparametros_form': uparametros_form,'error': error})

def mostrarP(request):
    perfil = UsuarioParametros.objects.get(id=request.user.id)
    form = UParametrosForm(instance=perfil)    
    return render(request,'usuario/mostrarP.html',{'form':form})


def eliminarP(request,documento):
     perfil = UsuarioParametros.objects.get(documento = documento)
     perfil.delete()
     return redirect('mostrarP')
