from django.contrib import admin

from .models import MetodoPago
from .models import DetalleMet

# Register your models here.
class MetodoPagoModelAdmin(admin.ModelAdmin):
    list_display = ('nombMetPago',)
    list_display_links = ('nombMetPago',)
    list_filter = ('nombMetPago',)
    search_fields = ('nombMetPago',)
    class Meta:
        model = MetodoPago

admin.site.register(MetodoPago,MetodoPagoModelAdmin)

class DetalleMetModelAdmin(admin.ModelAdmin):
    list_display = ('IdMetodo','valor','created_at',)
    list_display_links = ('IdMetodo',)
    list_filter = ('created_at',)
    search_fields = ('created_at',)
    class Meta:
        model = DetalleMet

admin.site.register(DetalleMet,DetalleMetModelAdmin)