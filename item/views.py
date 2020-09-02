from django.shortcuts import render,redirect
from django.views.generic import View
from core.views import logado
from .models import Item


class IndexView(View):
    def get(self, request):
        try:
            mensagem =  request.GET['msg']
        except:
            mensagem = 'ok'
        return logado('item/view.html',request,dados=Item.objects.all(),nivel_min=2,msg=mensagem)
