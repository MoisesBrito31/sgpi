from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import View
from core.views import logado
from core.models import Usuario
from cliente.models import Relacao as Cli_relacao
from .models import Proposta, Tipo, Cliente, Responsavel, Vendedor
from .forms import PropostaForm



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
        #try:
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
                print(obj)  
                return logado('proposta/add.html',request,dados=PropostaForm(),nivel_min=2,msg='gravado')
            #else:
            #    return logado('proposta/add.html',request,dados=PropostaForm(),nivel_min=2,msg='falha')
        #except:
            #return logado('proposta/add.html',request,dados=PropostaForm(),nivel_min=2,msg='falha')