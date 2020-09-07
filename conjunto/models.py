from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import Base


class TipoConjunto(Base):
    nome = models.CharField('Tipo do Conjunto', max_length=200)
    descricao = models.CharField('Descrição', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Tipo de Conjunto'
        verbose_name_plural = 'Tipos de Conjunto'

    def __str__(self):
        return self.nome

class TipoComponente(Base):
    nome = models.CharField('Tipo de Componente', max_length=200)
    descricao = models.CharField('Descrição', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Tipo de Componente'
        verbose_name_plural = 'Tipos de Componentes'

    def __str__(self):
        return self.nome

class Componente(Base):
    nome = models.CharField('Componente', max_length=200)
    descricao = models.CharField('Descrição', max_length=200, blank=True)
    preco_compra = models.DecimalField('Preço Compra', decimal_places=2, max_digits=8)
    preco_venda = models.DecimalField('Preço Venda', decimal_places=2, max_digits=8, default=0.00)
    fator = models.DecimalField('Fator de Conversão' ,decimal_places=4, max_digits=5 ,default=2.00)
    tipo = models.ForeignKey(TipoComponente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'        

    def __str__(self):
        return self.nome

class Conjunto(Base):
    nome = models.CharField('Conjunto',max_length=200)
    tipo = models.ForeignKey(TipoConjunto, on_delete=models.CASCADE)
    valor = models.DecimalField('Preço', max_digits=8, decimal_places=2, default=0.00)
    lista = models.ManyToManyField(Componente, through='Relacao')
    descricao = models.TextField('Descrição', max_length=200, default="",blank=True)

    class Meta:
        verbose_name = 'Conjunto'
        verbose_name_plural = 'Conjuntos'        

    def __str__(self):
        return self.nome

class Relacao(Base):
    componente = models.ForeignKey(Componente,blank=True, on_delete=models.CASCADE)
    conjunto = models.ForeignKey(Conjunto, blank=True, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    valor = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=0.00)

    class Meta:
        verbose_name = 'Relação'
        verbose_name_plural = 'Realações'        

    def __str__(self):
        return f'{self.componente.nome} (x{self.quantidade})'


@receiver(pre_save, sender=Conjunto)
def calcularConjunto(sender,instance,*args,**kargs):
    valor_final = 0.00
    for x in instance.relacao_set.all():
        valor_final+=float(x.quantidade*x.componente.preco_venda)
    instance.valor = valor_final

@receiver(pre_save, sender=Relacao)
def calcularRelacao(sender,instance,*args,**kargs):
    instance.valor = instance.componente.preco_venda * instance.quantidade

@receiver(pre_save, sender=Componente)
def calcular(sender,instance,*args,**kargs):
    instance.preco_venda = instance.preco_compra * instance.fator
    

