from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .forms import ContactForm

def usuariosLista(request):
    usa = Usuario.objects.all()
    form = ContactForm()
    return render(request, 'usuario/listaUsuario.html', {'usa':usa, 'form': form})
    
def usuariosCrear(request):
    return HttpResponse('<h1>AQUI VA CREAR USUARIO<h1>')

def usuariosEditar(request, id):
    return HttpResponse('<h1>AQUI VA EDITAR USUARIO<h1>' + str(id))

def usuariosBorrar(request, id):
    return HttpResponse('<h1>AQUI VA BORRAR USUARIO<h1>' + str(id))

def usuariosDetalle(request, id):
    return HttpResponse('<h1>AQUI VA DETALLE USUARIO<h1>' + str(id))

def login(request):
    return render(request, 'autenticacion/index.html')

def rec_contrasena(request):
    return render(request, 'autenticacion/recuperar.html')
