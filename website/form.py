from django.forms import ModelForm
from website.models import Cliente

class FormCliente( ModelForm ):
    class Meta:
        model = Cliente
        fields ='__all__'


