from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import View
from core.views import logado, UserPermission
from proposta.models import Proposta, ItemConjunto
from .models import Componente, Conjunto, Relacao
from .forms import ConjuntoForm, ComponenteForm


class IndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Conjunto.objects.all()
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Conjunto.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Conjunto.objects.filter(Q(nome__contains=find))
        except:
            pass
        return logado('conjunto/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)

class ConjuntoView(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = Conjunto.objects.get(id=index)
            form2 = Relacao.objects.all().filter(conjunto=index)
            form3 = ItemConjunto.objects.all().filter(item=index)
            return logado('conjunto/conjunto.html',request,context={'componentes':form2,'projetos': form3},dados=form,nivel_min=2)
        except:
            return redirect('/erro') 

class ConjuntoAdd(View):    
    def get(self, request):
        return logado('conjunto/add.html',request,dados=ConjuntoForm(),nivel_min=2)
    def post(self,request):
        form = ConjuntoForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return logado('conjunto/add.html',request,dados=ConjuntoForm(),nivel_min=2,msg='gravado')
        else:
            return logado('conjunto/add.html',request,dados=ConjuntoForm(),nivel_min=2,msg='falha')

class ConjuntoDelete(View):
    def get(self, request):
        try:
            index = request.GET['id']
            i = Conjunto.objects.get(id=index)
            i.delete()
            return logado('conjunto/view.html',request,dados=Conjunto.objects.all(),nivel_min=2,msg='gravado')
        except:
            return logado('conjunto/view.html',request,dados=Conjunto.objects.all(),nivel_min=2,msg='falha')

class ConjuntoEdit(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = ConjuntoForm(instance=Conjunto.objects.get(id=index))
            return logado('conjunto/edit.html',request,context={'id':index},dados=form,nivel_min=2)
        except:
            return redirect('/erro') 
    def post(self, request):
        form = ConjuntoForm(request.POST, request.FILES, instance=Conjunto.objects.get(id=request.POST['id']))
        if form.is_valid:
            index = request.POST['id']
            form.save()
            return logado('conjunto/edit.html',request,context={'id':index},dados=form,nivel_min=2,msg='gravado')
        else:
            return logado('conjunto/edit.html',request,context={'id':index},dados=form,nivel_min=2,msg='falha')


class ComponenteIndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Componente.objects.all()
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Componente.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Componente.objects.filter(Q(nome__contains=find))
        except:
            pass
        return logado('conjunto/componente/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)

class ComponenteAdd(View):    
    def get(self, request):
        return logado('conjunto/componente/add.html',request,dados=ComponenteForm(),nivel_min=2)
    def post(self,request):
        form = ComponenteForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return logado('conjunto/componente/add.html',request,dados=ComponenteForm(),nivel_min=2,msg='gravado')
        else:
            return logado('conjunto/componente/add.html',request,dados=ComponenteForm(),nivel_min=2,msg='falha')

class ComponenteEdit(View):
    def get(self, request):
        try:
            index = request.GET['id']
            form = ComponenteForm(instance=Componente.objects.get(id=index))
            return logado('conjunto/componente/edit.html',request,context={'id':index},dados=form,nivel_min=2)
        except:
            return redirect('/erro') 
    def post(self, request):
        form = ComponenteForm(request.POST, request.FILES, instance=Componente.objects.get(id=request.POST['id']))
        if form.is_valid:
            form.save()
            rl = Relacao.objects.all().first()
            rl.save()
            cj = Conjunto.objects.all().first()
            cj.save()
            return logado('conjunto/componente/edit.html',request,dados=form,nivel_min=2,msg='gravado')
        else:
            return logado('conjunto/componente/edit.html',request,dados=form,nivel_min=2,msg='falha')

class ComponenteDelete(View):
    def get(self, request):
        try:
            index = request.GET['id']
            i = Componente.objects.get(id=index)
            i.delete()
            return logado('conjunto/componente/view.html',request,dados=Componente.objects.all(),nivel_min=2,msg='gravado')
        except:
            return logado('conjunto/componente/view.html',request,dados=Componente.objects.all(),nivel_min=2,msg='falha')

class RelacaoAlt(View):
    def post(self, request):
        try:
            if UserPermission(request,nivel_min=2):
                val = int(request.POST['valor'])
                rel_id = request.POST['relacao_id']
                redire_id = request.POST['conjunto_id']
                rel = Relacao.objects.get(id=rel_id)
                rel.quantidade = val
                rel.save()
                c = Conjunto.objects.all().first()
                c.save()
                return redirect(f'/conjunto/conjunto?id={redire_id}')
            else:
                return redirect('/erro')
        except:
            return redirect('/erro')

class RelacaoDel(View):
    def post(self, request):
        try:
            if UserPermission(request,nivel_min=2):
                rel_id = request.POST['relacao_id']
                redire_id = request.POST['conjunto_id']
                rel = Relacao.objects.get(id=rel_id)
                rel.delete()
                c = Conjunto.objects.all().first()
                c.save()
                return redirect(f'/conjunto/conjunto?id={redire_id}')
            else:
                return redirect('/erro')
        except:
            return redirect('/erro')

class RelacaoAdd(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Componente.objects.all()
        conj_id = request.GET['conjunto_id']
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Componente.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Componente.objects.filter(Q(nome__contains=find))
        except:
            pass
        return logado('conjunto/relacao_add.html',request,context={'find':find,'filtro':filtro,'conjunto_id':conj_id},dados=infor,nivel_min=2,msg=mesagem)
    def post(self, request):
        try:
            if UserPermission(request,nivel_min=2):
                comp_id = int(request.POST['componente_id'])
                conj_id = int(request.POST['conjunto_id'])
                qtd = int(request.POST['quantidade'])
                compo = Componente.objects.get(id=comp_id)
                conju = Conjunto.objects.get(id=conj_id)
                rel = Relacao(componente=compo,conjunto=conju,quantidade=qtd)
                rel.save()
                c = Conjunto.objects.all().first()
                c.save()
                return redirect(f'/conjunto/conjunto?id={conj_id}')
            else:
                return redirect('/login')
        except:
            return redirect('/erro')

