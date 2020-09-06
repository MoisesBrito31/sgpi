from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.views.generic import View
from core.views import logado, UserPermission
from proposta.models import Proposta
from .models import Cliente, Responsavel, Relacao
from .forms import ClienteForm, ResponsavelForm


class IndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = '*'
        infor = Cliente.objects.all()
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Cliente.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Cliente.objects.filter(Q(nome__contains=find))
        except:
            pass
        return logado('cliente/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)


class ClienteAdd(View):    
    def get(self, request):
        return logado('cliente/add.html',request,dados=ClienteForm(),nivel_min=2)
    def post(self,request):
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return logado('cliente/add.html',request,dados=ClienteForm(),nivel_min=2,msg='gravado')
        else:
            return logado('cliente/add.html',request,dados=ClienteForm(),nivel_min=2,msg='falha')


class ClienteEdit(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = ClienteForm(instance=Cliente.objects.get(id=index))
            return logado('cliente/edit.html',request,context={'id':index},dados=form,nivel_min=2)
        except:
            return redirect('cliente') 
    def post(self, request):
        form = ClienteForm(request.POST, request.FILES, instance=Cliente.objects.get(id=request.POST['id']))
        if form.is_valid:
            form.save()
            return logado('cliente/edit.html',request,dados=form,nivel_min=2,msg='gravado')
        else:
            return logado('cliente/edit.html',request,dados=form,nivel_min=2,msg='falha')


class ClienteDelete(View):
    def get(self, request):
        try:
            index = request.GET['id']
            i = Cliente.objects.get(id=index)
            i.delete()
            return logado('cliente/view.html',request,dados=Cliente.objects.all(),nivel_min=2,msg='gravado')
        except:
            return logado('cliente/view.html',request,dados=Cliente.objects.all(),nivel_min=2,msg='falha')




class ClienteView(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = Cliente.objects.get(id=index)
            form2 = Relacao.objects.all().filter(empresa=index)
            form3 = Proposta.objects.all().filter(cliente=index)
            return logado('cliente/cliente.html',request,context={'funcionarios':form2,'propostas':form3},dados=form,nivel_min=2)
        except:
            return redirect('cliente') 

class ResponsavelAdd(View):    
    def get(self, request):
        try:
            index = request.GET['id']
            return logado('cliente/responsavel/add.html',request,context={'clienteID':index},dados=ResponsavelForm(),nivel_min=2)
        except:
            return logado('cliente/responsavel/add.html',request,dados=ResponsavelForm(),nivel_min=2)
    def post(self,request):
        form = ResponsavelForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                index = request.POST['cliente_id']
                client = Cliente.objects.get(id=index)
                form.save()
                func = Responsavel.objects.all().last() 
                R = Relacao(funcionario=func,empresa=client)
                R.save()
                return logado('cliente/responsavel/add.html',request,context={'clienteID':index},dados=ResponsavelForm(),nivel_min=2,msg='gravado')
            except:
                pass
        return logado('cliente/responsavel/add.html',request,dados=ResponsavelForm(),nivel_min=2,msg='falha')


class ResponsavelEdit(View):
    def get(self, request):
        try:
            index = request.GET['id']
            c_index = request.GET['cliente_id']
            form = ResponsavelForm(instance=Responsavel.objects.get(id=index))
            return logado('cliente/responsavel/edit.html',request,context={'id':index,'clienteID':c_index},dados=form,nivel_min=2)
        except:
            return redirect('cliente') 
    def post(self, request):
        index = request.POST['id']
        c_index = request.POST['cliente_id']
        form = ResponsavelForm(request.POST, request.FILES, instance=Responsavel.objects.get(id=index))
        if form.is_valid:
            form.save()
            return logado('cliente/responsavel/edit.html',request,context={'id':index,'clienteID':c_index},dados=form,nivel_min=2,msg='gravado')
        else:
            return logado('cliente/responsavel/edit.html',request,context={'id':index,'clienteID':c_index},dados=form,nivel_min=2,msg='falha')


class ResponsavelDelete(View):
    def get(self, request):
        try:
            if UserPermission(request,nivel_min=2):
                index = request.GET['id']
                i = Responsavel.objects.get(id=index)
                i.delete()
                return HttpResponse("ok")
            else:
                return HttpResponse("falha você não tem permissão")
        except:
            return HttpResponse("falha")