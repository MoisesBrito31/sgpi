from django import forms
from .models import Item


class ViewForm(forms.Form):
    msg = forms.CharField(label='msg',max_length=15)
    filtro = forms.CharField(label='filtro',)
