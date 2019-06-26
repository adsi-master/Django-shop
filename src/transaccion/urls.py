from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking, name="Chequeo"),
    path('factura/', views.factura, name="Factura")
]