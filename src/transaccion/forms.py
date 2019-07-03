from django import forms
from .models import DetalleMet, DetalleTra, MetodoPago, Transaccion

class FacturaForm(forms.ModelForm):
    IdTransaccion = forms.CharField(label="IdTransaccion",widget=forms.TextInput)
    IdProducto = forms.Charfield(label="IdProducto",widget=forms.TextInput)
    Fecha = forms.DateTimeField(label="Fecha", required=False)
    Cantidad = forms.IntegerField(label="Cantidad", required=False)(label="Cantidad")
    class Meta:
        model = DetalleTra
        fields = ('IdTransaccion', 'IdProducto' ,'Fecha','Cantidad')

FacturaFormSet = modelformset_factory(DetalleTra,form=FacturaForm,extra=0,can_delete=True)