from django.contrib import admin
from .models import Cargo, Responsavel, Cliente, Relacao


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display=('nome','cargo','email','telefone','get_cliente_set')

    def get_cliente_set(self,obj):
        return obj.cliente_set.first()

    get_cliente_set.short_description = "Empresa"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','endereco','cnpj','get_responsaveis')

    def get_responsaveis(self, obj):
        return ', '.join([m.nome for m in obj.responsaveis.all()])

    get_responsaveis.short_description = 'Responsáveis'

@admin.register(Relacao)
class RelacaoAdmin(admin.ModelAdmin):
    list_display=('funcionario','empresa')

