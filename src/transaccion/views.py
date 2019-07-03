from django.shortcuts import render
from django.views.generic import ListView
from .models import Transaccion
# Create your views here.

# class TransaccionList(ListView):
#     model = 
def checking(request):
    return render(request, 'dailyShop/checkout.html')

class facturaListView(ListView):
    model = Transaccion
    template_name = 'dailyShop/factura.html'
    context_object_name = 'facturaList'
    def get_queryset():
        return Transaccion.objects.filter(Usuarioid=1)