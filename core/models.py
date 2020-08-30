from django.db import models
from random import randint as randon
from stdimage import StdImageField

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
    email = models.EmailField('E-Mail', max_length=100)
    nivel = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    senha = models.CharField('Senha', max_length=10)
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
        tk = Token().token
        self.token = tk

    def logout(self):
        tk = Token().token
        self.token = tk


class Vara(Base):
    nome = models.CharField('nome', max_length= 100)
    juiz = models.CharField('juiz', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    estado = models.CharField('estado', max_length=100)

    class Meta:
        verbose_name = 'Vara Judicial'
        verbose_name_plural = 'Varas Judiciais'

    def __str__(self):
        return self.nome


class Processo(Base):
    numero = models.CharField('numero',max_length=100)
    vara = models.ForeignKey('core.vara', verbose_name='Vara', on_delete=models.CASCADE)
    intimacao = models.DateField('intimação', blank=True)
    inicio = models.DateField('inicio do trabalho', blank=True)
    entrega = models.DateField('entrega', blank=True)
    requerente = models.CharField('Requerente', max_length=100)
    requerido = models.CharField('Requerido', max_length=100)
    honorario_pro = models.DecimalField('Honorário Proposto', decimal_places=2, max_digits=10, blank=True)
    honorario = models.DecimalField('Honorário', decimal_places=2, max_digits=10, blank=True)
    obs = models.TextField('obs', max_length=1000, blank=True)

    class Meta:
        verbose_name= 'Processo'
        verbose_name_plural = 'Processos'

    def __str__(self):
        return self.numero