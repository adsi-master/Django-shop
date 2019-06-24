from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

# class TransaccionList(ListView):
#     model = 
def checking(request):
    return render(request, 'dailyShop/checkout.html')

def factura(request):
    return render(request, 'dailyShop/factura.html')