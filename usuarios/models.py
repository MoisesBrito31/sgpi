import datetime
from django.db import models
from random import randint as randon
from stdimage import StdImageField
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60 
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)


class Token():
    token = 'abcdefghij'
    __base =(
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z',
        'a','c','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9',
    )

    def __init__(self, qtd=100):
        self.GeraToken(qtd)

    def GeraToken(self, qtd):
        ret = str('')
        for x in range(qtd):
            ret = str.format('{}{}', ret, self.__base[randon(0,59)])
        self.token = ret


class Base(models.Model):
    criado = models.DateTimeField('Criado',auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)
    class Meta:
        abstract = True


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    nivel = models.IntegerField('Nivel de Acesso')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo


class Usuario(Base):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('email', max_length=100, unique=True)
    nivel = models.ForeignKey('usuarios.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    senha = models.CharField('senha', max_length=10)
    token = models.CharField('token', max_length=255, default='', blank=True)
    img = StdImageField(
                            'Imagem', upload_to='usuarios', 
                            variations={'thumb':{'width' : 100,'height':100}},
                            blank=True
                        )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome

    def loggin(self):
        self.token = Token.GeraToken()
       
    def UserPermission(request, nivel_min=5):
        try:
            usu = str(request.COOKIES['userID'])
            user = Usuario.objects.get(token=usu)
            if user.nivel.nivel> nivel_min:
                return False
            else:
                return True
        except:
            return False

    def logado(alvo, request, context={}, titulo='', msg='ok', dados='', nivel_min=5):
        try:
            usu = str(request.COOKIES['userID'])
            user = Usuario.objects.get(token=usu)
            context['user'] = user
            context['titulo'] = titulo
            context['msg'] = msg
            context['dados'] = dados
            if user.nivel.nivel> nivel_min:
                context['msg'] = 'Você não tem Autorização para acessar essa pagina'
                return render(request, 'erro.html', context)
            else:
                return render(request, alvo, context)
        except:
            redir = alvo.split('.')[0]
            response = HttpResponseRedirect('login')
            set_cookie(response,'redirect', redir)
            return response