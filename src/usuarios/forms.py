from django import forms
from src.usuarios.models import Usuario

class ContactForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = {'alias', 'tipousuario', 'correo'}