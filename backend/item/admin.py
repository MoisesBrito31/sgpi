from django.contrib import admin
from .models import Item, Tipo, Linha, Fabricante, Familia


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'fabricante', 'linha', 'tipo', 'familia')


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Linha)
class LinhaAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display=('nome',)
