from django.db import models
from core.models import Base
from stdimage import StdImageField


class Familia(Base):
    nome = models.CharField('Família', max_length=20)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = "Famílias"

    def __str__(self):
        return self.nome


class Tipo(Base):
    nome = models.CharField('Tipo', max_length=20)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.nome


class Linha(Base):
    nome = models.CharField('Linha', max_length=20)
    descricao = models.CharField('descrição', max_length=50, default='', blank=True)

    class Meta:
        verbose_name = 'Linha'
        verbose_name_plural = "Linhas"

    def __str__(self):
        return self.nome


class Fabricante(Base):
    nome = models.CharField('Fabricante', max_length=20)
    pais = models.CharField('Nacionalidade', max_length=20, default='', blank=True)
    img = StdImageField('Imagem', upload_to='fabricante',variations={'thumb' :{'height': 100, 'width': 100, 'crop': True}}, blank = True)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = "Fabricantes"

    def __str__(self):
        return self.nome


class Item(Base):
    codigo = models.CharField('Código de Cadastro', max_length=20, help_text="Imforme o codigo do produto", unique=True)
    nome = models.CharField('Código de Identificação', max_length=30, unique=True)
    descricao = models.CharField('Descrição', max_length=50, blank=True)
    preco = models.DecimalField('Preço Compra', decimal_places=2, max_digits=8, default=0.00)
    fabricante = models.ForeignKey(Fabricante,on_delete=models.CASCADE)
    linha = models.ForeignKey(Linha,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia,on_delete=models.CASCADE)
    img = StdImageField('Imagem', upload_to='itens', variations={'thumb' :{'height': 100, 'width': 100, 'crop': True}}, blank = True)
    

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f'{self.nome}({self.codigo})'
    


