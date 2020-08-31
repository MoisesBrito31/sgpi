from django.contrib import admin
from .models import TipoComponente, TipoConjunto, Componente, Relacao, Conjunto

@admin.register(TipoComponente)
class TipoComponenteAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(TipoConjunto)
class TipoConjuntoAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display=('nome','preco_compra','preco_venda','fator','tipo')

@admin.register(Relacao)
class RelacaoAdmin(admin.ModelAdmin):
    list_display=('componente','quantidade', 'valor')

@admin.register(Conjunto)
class ConjuntoAdmin(admin.ModelAdmin):
    list_display=('nome','tipo','valor')
