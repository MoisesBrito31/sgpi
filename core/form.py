from django import forms
from .models import Usuario, Vara, Processo


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'img','nivel']


class VaraForm(forms.ModelForm):
    class Meta:
        model = Vara
        fields = '__all__'


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = '__all__'