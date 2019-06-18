from django.contrib import admin
from .models import Usuario, TipoUsuario, DatosUsuario, Titulo, TipoDocumento

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(DatosUsuario)
admin.site.register(Titulo)
admin.site.register(TipoDocumento)