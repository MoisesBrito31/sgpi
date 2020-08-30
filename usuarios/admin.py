from django.contrib import admin
from .models import Usuario,Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display=('cargo','nivel','ativo')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('nome','email','ativo','modificado')
    
