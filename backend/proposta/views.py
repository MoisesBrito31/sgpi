from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import View
from core.views import logado, UserPermission
from core.models import Usuario
from cliente.models import Relacao as Cli_relacao
from .models import Proposta, Tipo, Cliente, Responsavel, Vendedor, ItemConjunto, ItemProduto, Arquivos, Item, Conjunto
from .forms import PropostaForm
from datetime import datetime



class IndexView(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Proposta.objects.all()
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Proposta.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = Proposta.objects.filter(Q(projeto__contains=find) | Q(descricao__contains=find))
        except:
            pass
        return logado('proposta/view.html',request,context={'find':find,'filtro':filtro},dados=infor,nivel_min=2,msg=mesagem)

class PropostaAdd(View):
    def get(self, request):
        try:
            c_id = int(request.GET['cliente_id'])
            relacao = Cli_relacao.objects.filter(empresa=c_id) 
        except:
            c_id = ""
            relacao = {}
        cliente = Cliente.objects.all()
        form = PropostaForm()
        return logado('proposta/add.html',request,context={'relacao':relacao,'empresa':cliente, 'clienteID':c_id},dados=form,titulo='add Proposta',nivel_min=2)
    def post(self,request):
            proj = request.POST['projeto']
            tip = Tipo.objects.get(id=request.POST['tipo']) 
            client = Cliente.objects.get(id=request.POST['cliente'])
            try:
                respo = Responsavel.objects.get(id=request.POST['responsavel'])
            except:
                respo = 0
            data = request.POST['datafinal']
            desc = request.POST['descricao']
            tecn = Usuario.objects.get(token=request.COOKIES['userID'])
            vend = Vendedor.objects.get(id=request.POST['vendedor'])
            if respo == 0:
                obj = Proposta(projeto=proj,tipo=tip,cliente=client,datafinal=data,descricao=desc,tecnico=tecn,vendedor=vend)
            else:
                obj = Proposta(projeto=proj,tipo=tip,cliente=client,responsavel=respo,datafinal=data,descricao=desc,tecnico=tecn,vendedor=vend)    
            obj.save()
            return logado('proposta/add.html',request,dados=PropostaForm(),nivel_min=2,msg='gravado')
 
class PropostaView(View):
    def get(self, request):
        index = request.GET['id']
        form = Proposta.objects.get(id=index)
        form2 = ItemProduto.objects.all().filter(proposta=index)
        form3 = ItemConjunto.objects.all().filter(proposta=index)
        form4 = Arquivos.objects.all().filter(proposta=index)
        cont = {
            'itens':form2,
            'conjuntos':form3,
            'arquivos': form4,
        }
        return logado('proposta/proposta.html',request,context=cont,dados=form,nivel_min=2)

class PropostaEdit(View):
    def get(self, request):
        index = request.GET['id']
        obj = Proposta.objects.get(id=index)
        relacao = Cli_relacao.objects.all().filter(empresa=obj.cliente)
        form = PropostaForm(instance=obj)
        cliente = obj.cliente
        if obj.datafinal.month<=9:
            mes = f'0{str(obj.datafinal.month)}'
        else:
            mes = str(obj.datafinal.month)
        if obj.datafinal.day<=9:
            dia = f'0{str(obj.datafinal.day)}'
        else:
            dia = str(obj.datafinal.day)
        data = f'{obj.datafinal.year}-{mes}-{dia}'
        return logado('proposta/edit.html',request,context={'data':data,'cliente':cliente,'relacao':relacao,'propostaID':index},dados=form,titulo='Proposta edit',nivel_min=2)       
    def post(self, request):
            index = int(request.POST['id'])
            form = PropostaForm(request.POST, request.FILES,instance=Proposta.objects.get(id=index))
            if form.is_valid:
                form.save()
                return redirect(f'/proposta/proposta?id={index}')
            else:
                return redirect('/erro')

class PropostaDelete(View):
    def get(self, request):
        if UserPermission(request,nivel_min=2):
            index = request.GET['id']
            i = Proposta.objects.get(id=index)
            i.delete()
            return redirect('/proposta')
        else:
            return redirect('/erro')

class ItensAlt(View):
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            val = int(request.POST['valor'])
            rel_id = int(request.POST['itens_id'])
            redire_id = int(request.POST['proposta_id'])
            rel = ItemProduto.objects.get(id=rel_id)
            rel.quantidade = val
            rel.save()
            return redirect(f'/proposta/proposta?id={redire_id}')
        else:
            return redirect('/erro')

class ItensDel(View):
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            rel_id = int(request.POST['itens_id'])
            redire_id = int(request.POST['proposta_id'])
            rel = ItemProduto.objects.get(id=rel_id)
            rel.delete()
            return redirect(f'/proposta/proposta?id={redire_id}')
        else:
            return redirect('/erro')

class ItensAdd(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Item.objects.all()
        conj_id = request.GET['proposta']
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Item.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = infor.filter(Q(nome__contains=find) | Q(codigo__contains=find))
        except:
            pass
        return logado('proposta/itens_add.html',request,context={'find':find,'filtro':filtro,'proposta':conj_id},dados=infor,nivel_min=2,msg=mesagem)
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            comp_id = int(request.POST['item_id'])
            conj_id = int(request.POST['proposta_id'])
            qtd = int(request.POST['quantidade'])
            compo =Item.objects.get(id=comp_id)
            conju = Proposta.objects.get(id=conj_id)
            rel = ItemProduto(item=compo,proposta=conju,quantidade=qtd)
            rel.save()
            return redirect(f'/proposta/proposta?id={conj_id}')
        else:
            return redirect('/login')

class ConjuntosAlt(View):
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            val = int(request.POST['valor'])
            rel_id = int(request.POST['conjunto_id'])
            redire_id = int(request.POST['proposta_id'])
            rel = ItemConjunto.objects.get(id=rel_id)
            rel.quantidade = val
            rel.save()
            return redirect(f'/proposta/proposta?id={redire_id}')
        else:
            return redirect('/erro')

class ConjuntosDel(View):
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            rel_id = int(request.POST['conjunto_id'])
            redire_id = int(request.POST['proposta_id'])
            rel = ItemConjunto.objects.get(id=rel_id)
            rel.delete()
            return redirect(f'/proposta/proposta?id={redire_id}')
        else:
            return redirect('/erro')

class ConjuntosAdd(View):
    def get(self, request):
        mesagem = 'ok'
        filtro='none'
        find = ''
        infor = Conjunto.objects.all()
        conj_id = request.GET['proposta']
        try:
            filtro = request.GET['filtro']
            if filtro != 'none':
                infor = Conjunto.objects.all().order_by(filtro)
            mesagem = request.GET['msg']            
            find = request.GET['find']
            infor = infor.filter(Q(nome__contains=find))
        except:
            pass
        return logado('proposta/conjuntos_add.html',request,context={'find':find,'filtro':filtro,'proposta':conj_id},dados=infor,nivel_min=2,msg=mesagem)
    def post(self, request):
        if UserPermission(request,nivel_min=2):
            comp_id = int(request.POST['conjunto_id'])
            conj_id = int(request.POST['proposta_id'])
            qtd = int(request.POST['quantidade'])
            compo =Conjunto.objects.get(id=comp_id)
            conju = Proposta.objects.get(id=conj_id)
            rel = ItemConjunto(item=compo,proposta=conju,quantidade=qtd)
            rel.save()
            return redirect(f'/proposta/proposta?id={conj_id}')
        else:
            return redirect('/login')