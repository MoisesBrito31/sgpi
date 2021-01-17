from django import forms
from .models import Conjunto, Componente,Relacao



class ConjuntoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
        fields = ('nome', 'tipo', 'descricao')

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ('nome','tipo', 'descricao','preco_compra','fator')

class RelacaoForm(forms.ModelForm):
    class Meta:
        model = Relacao
        fields = ('componente','conjunto','quantidade')