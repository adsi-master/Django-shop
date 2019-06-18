from django.contrib import admin
from .models import Usuario, DatosUsuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["alias", "tipousuario", "correo"]
    # list_display_links = ["body"]
    # list_editable = ["title"]
    class Meta:
        model = Usuario
admin.site.register(Usuario, UsuarioAdmin)


admin.site.register(DatosUsuario)