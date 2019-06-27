from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UsuarioParametros

class FormLogin(UserCreationForm):
    
    class Meta:
        model = User
        fields=[
            'username','password'
        ]

class UParametrosForm(forms.ModelForm):
    
    class Meta:
        model = UsuarioParametros
        fields=[
            'usuario','tipodocumento','documento','Nombre', 'Apellido', 'telefono', 'correo', 'direccion',
            'estasdocivil','genero'
        ]       
        widgets={
            'usuario' : forms.Select(attrs={'class':'form-control'}),
            'tipodocumento' : forms.TextInput(attrs={'class': 'form-control'}),
            'documento' : forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'correo' : forms.TextInput(attrs={'class': 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),
            'estasdocivil' : forms.TextInput(attrs={'class': 'form-control'}),
            'genero' : forms.TextInput(attrs={'class': 'form-control'}),
            'avatar' : forms.TextInput(attrs={'class': 'thumbnail'})
        }
