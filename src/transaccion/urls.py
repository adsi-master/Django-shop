from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking, name="Chequeo"),
    path('checkout/',views.checkout,name="test"),
    path('factura/', views.factura, name="Factura")
]