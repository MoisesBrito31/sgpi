from django.db import models
from stdimage import StdImageField
from core.models import Base
from item.models import Item


class Cargo(Base):
    nome = models.CharField('Cargo', max_length=35)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome

class Industria(Base):
    nome = models.CharField('Cargo', max_length=35)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Indústria'
        verbose_name_plural = 'Indústrias'

    def __str__(self):
        return self.nome


class Responsavel(Base):
    nome = models.CharField('Nome',max_length=50)
    email = models.EmailField('E-Mail', max_length=60)
    telefone = models.IntegerField('Telefone')
    cargo = models.ForeignKey(Cargo, blank=True, on_delete=models.CASCADE)
   

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome


class Cliente(Base):
    nome = models.CharField('Cliente', max_length=30, unique=True)
    endereco = models.CharField('Endereço', max_length=50, blank=True)
    cnpj = models.CharField('CNPJ', max_length=20, blank=True)
    responsaveis = models.ManyToManyField(Responsavel,through='Relacao')
    industria = models.ForeignKey(Industria, blank=True, default=1 ,on_delete=models.CASCADE)
    logo = StdImageField('Imagem', upload_to='cliente/logo', variations={'thumb' :{'height': 150, 'width': 150, 'crop': True}}, blank = True)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Relacao(Base):
    funcionario = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Relação'
        verbose_name_plural = 'Relações'


