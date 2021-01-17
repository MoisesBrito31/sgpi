from django.db import models
from core.models import Base, Usuario
from cliente.models import Cliente, Responsavel
from item.models import Item
from conjunto.models import Conjunto



class Tipo(Base):
    nome = models.CharField('Tipo', max_length=20)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nome

class TipoArquivo(Base):
    nome = models.CharField('Tipo do Arquivo', max_length=20)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Tipo do Arquivo'
        verbose_name_plural = 'Tipos de Arquivos'

    def __str__(self):
        return self.nome


class Vendedor(Base):
    nome = models.CharField('Vendedor', max_length=20)
    email = models.EmailField('E-Mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.nome


class Arquivo(Base):
    nome = models.CharField('Nome do Arquivo', max_length=100)
    arquivo = models.FileField('Arquivo', upload_to='propostas/files')
    tipo = models.ForeignKey(TipoArquivo,on_delete=models.CASCADE)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return f'{self.nome} ({self.tipo})'


class Proposta(Base):
    projeto = models.CharField('Projeto',max_length=200)
    descricao = models.CharField('Descrição', max_length=500)
    tecnico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, blank=True,on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel,blank=True, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    datafinal = models.DateField('Data final')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='ItemProduto')
    conjuntos = models.ManyToManyField(Conjunto ,through='ItemConjunto')
    documentos = models.ManyToManyField(Arquivo, through='Arquivos')

   
    class Meta:
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'

    def __str__(self):
        return self.projeto

class ItemProduto(Base):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return f'{self.item.nome} x {self.quantidade}'


class ItemConjunto(Base):
    item=models.ForeignKey(Conjunto, on_delete=models.CASCADE)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = 'Item Montado'
        verbose_name_plural = 'Itens Montados'

    def __str__(self):
        return f'{self.item.nome} x {self.quantidade}'

class Arquivos(Base):
    arquivo = models.ForeignKey(Arquivo,on_delete=models.CASCADE)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pasta'
        verbose_name_plural = 'Pastas'

    def __str__(self):
        return f'{self.arquivo.nome} - {self.proposta.projeto}'

