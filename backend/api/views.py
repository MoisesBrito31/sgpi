from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import Q

from core.views import logado
from proposta.models import ItemProduto
from item.models import Item,Tipo
from item.forms import ItemForm
from django.forms.models import model_to_dict

class IndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Item.objects.all()
        try:
            """
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Item.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Item.objects.filter(Q(nome__contains=find) | Q(codigo__contains=find))
            """
            js ='['
            for x in infor:
                js=f'{js}{model_to_dict(x)}'
            js = f'{js}]'
            js = js.replace('}{','},{')
            print(js)
        except:
            pass
        return JsonResponse(js,safe=False)
        #return logado('item/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)

