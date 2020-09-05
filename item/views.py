from django.shortcuts import render,redirect
from django.db.models import Q
from django.views.generic import View
from core.views import logado
from .models import Item,Tipo
from .forms import ItemForm


class IndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = '*'
        infor = Item.objects.all()
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Item.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Item.objects.filter(Q(nome__contains=find) | Q(codigo__contains=find))
        except:
            pass
        return logado('item/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)

class ItemAdd(View):
    def get(self, request):
        return logado('item/add.html',request,dados=ItemForm(),nivel_min=2)
    def post(self,request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return logado('item/add.html',request,dados=ItemForm(),nivel_min=2,msg='gravado')
        else:
            return logado('item/add.html',request,dados=ItemForm(),nivel_min=2,msg='falha')

class ItemEdit(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = ItemForm(instance=Item.objects.get(id=index))
            return logado('item/edit.html',request,context={'id':index},dados=form,nivel_min=2)
        except:
            return redirect('item') 
    def post(self, request):
        form = ItemForm(request.POST, request.FILES, instance=Item.objects.get(id=request.POST['id']))
        if form.is_valid:
            form.save()
            return logado('item/edit.html',request,dados=form,nivel_min=2,msg='gravado')
        else:
            return logado('item/edit.html',request,dados=form,nivel_min=2,msg='falha')


class ItemDelete(View):
    def get(self, request):
        try:
            index = request.GET['id']
            i = Item.objects.get(id=index)
            i.delete()
            return logado('item/view.html',request,dados=Item.objects.all(),nivel_min=2,msg='gravado')
        except:
            return logado('item/view.html',request,dados=Item.objects.all(),nivel_min=2,msg='falha')


class ItemView(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = Item.objects.get(id=index)
            return logado('item/item.html',request,dados=form,nivel_min=2)
        except:
            return redirect('item') 

        