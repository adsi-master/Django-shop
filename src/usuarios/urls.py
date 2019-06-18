from django.urls import path

from .views import usuariosLista, usuariosCrear, usuariosBorrar, usuariosEditar, usuariosDetalle

urlpatterns = [
    path('', usuariosLista, name='usuariosLista'),
    path('crear/', usuariosCrear, name='usuariosCrear'),
    path('detalle/<int:id>', usuariosDetalle, name='usuariosDetalle'),
    path('editar/<int:id>', usuariosEditar, name='usuariosEditar'),
    path('borrar/<int:id>', usuariosBorrar, name='usuariosBorar'),
]