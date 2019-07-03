from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
import stripe

#Stripe 
#Aquí se manda la información a Stripe, que vendría a ser la Api encargada de los pagos.
#Se instaló Stripe y luego lo importamos para poder mandar la información

def checkout(request, **kwargs):
    existing_order = {}
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.Charge.create(
                    amount = 500,
                    currency = 'eur',
                    description = 'Example charge',
                    source = token,
            )
        except:
            print('Tarjeta rechazada') 
    # context = {
    #     'order': existing_order,
    #     'client_token': client_token,
    #     'STRIPE_PUBLISHABLE_KEY': publishKey
    # }

    return render(request, 'dailyShop/checkout.html')



# Create your views here.

# class TransaccionList(ListView):
#     model = 
def checking(request):
    return render(request, 'dailyShop/checkout.html')

def factura(request):
    return render(request, 'dailyShop/factura.html')