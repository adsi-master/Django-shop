from django.contrib import admin
from .models import Usuario, TipoUsuario, DatosUsu

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(DatosUsu)