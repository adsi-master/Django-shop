from django.shortcuts import render
from django.http import HttpResponse

def usuariosLista(request):
    return HttpResponse('<h1>AQUI VA LISTA USUARIOS<h1>')
    
def usuariosCrear(request):
    return HttpResponse('<h1>AQUI VA CREAR USUARIO<h1>')

def usuariosEditar(request, id):
    return HttpResponse('<h1>AQUI VA EDITAR USUARIO<h1>' + str(id))

def usuariosBorrar(request, id):
    return HttpResponse('<h1>AQUI VA BORRAR USUARIO<h1>' + str(id))

def usuariosDetalle(request, id):
    return HttpResponse('<h1>AQUI VA DETALLE USUARIO<h1>' + str(id))
