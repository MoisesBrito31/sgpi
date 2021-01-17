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
    list_display=('componente','quantidade', 'valor', 'get_item')

    def get_item(self, obj):
        return str(obj.conjunto)

    get_item.short_description = 'Conjunto'

@admin.register(Conjunto)
class ConjuntoAdmin(admin.ModelAdmin):
    list_display=('nome','tipo','valor','get_lista')

    def get_lista(self , obj):
        return ',---'.join(str(m.relacao_set.first()) for m in obj.lista.all())

    get_lista.short_description = 'Componentes'
