from django.contrib import admin
from .models import TipoUsuario, Titulo, TipoDocumento

class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ["nombre",]
    # list_display_links = ["id"]
    # list_editable = ["nombre"]
    class Meta:
        model = TipoUsuario        
admin.site.register(TipoUsuario, TipoUsuarioAdmin)

admin.site.register(Titulo)

admin.site.register(TipoDocumento)

