from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UsuarioParametros, TipoDocumento, EstadoCivil

class FormLogin(UserCreationForm):
    
    class Meta:
        model = User
        fields=[
            'username','password'
        ]

class UParametrosForm(forms.ModelForm):
    tipodocumento = forms.ModelChoiceField(initial='', queryset=TipoDocumento.objects.all(), widget=forms.Select(attrs={'class':'dropdown-trigger btn'}))
    estasdocivil = forms.ModelChoiceField(initial='', queryset=EstadoCivil.objects.all(), widget=forms.Select(attrs={'class':'dropdown-trigger btn'}))

    class Meta:
        model = UsuarioParametros
        fields=[
            'tipodocumento','documento','nombre', 'apellido', 'telefono', 'correo', 'direccion',
            'estasdocivil','genero'
        ]       
        widgets={
            'documento' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'correo' : forms.TextInput(attrs={'class': 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),
            'genero' : forms.TextInput(attrs={'class': 'form-control'}),
            'avatar' : forms.TextInput(attrs={'class': 'thumbnail'})
        }
