from django import forms
from .models import Cliente, Responsavel



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome','endereco','cnpj','industria','logo')

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = '__all__'