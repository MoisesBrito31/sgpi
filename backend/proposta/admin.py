from django.contrib import admin
from .models import ItemConjunto, ItemProduto, Proposta, Arquivo, Arquivos, Tipo, TipoArquivo, Vendedor

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display=('nome',)


@admin.register(TipoArquivo)
class TipoArquivoAdmin(admin.ModelAdmin):
    list_display=('nome',)


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display=('nome','tipo')

@admin.register(Arquivos)
class ArquivosAdmin(admin.ModelAdmin):
    list_display=('arquivo','proposta')

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display=('nome', 'email', 'telefone')

@admin.register(ItemProduto)
class ItemProduto(admin.ModelAdmin):
    list_display=('item','proposta','quantidade')

@admin.register(ItemConjunto)
class ItemConjunto(admin.ModelAdmin):
    list_display=('item','proposta','quantidade')

@admin.register(Proposta)
class ItemConjunto(admin.ModelAdmin):
    list_display=('projeto','cliente','vendedor','descricao')


