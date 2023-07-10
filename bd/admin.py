from django.contrib import admin
from .models import Usuario, Vacas, Bezerro, Reprodutor,Prenha

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email')

@admin.register(Vacas)
class VacasAdmin(admin.ModelAdmin):
    list_display = ('nome_vaca', 'raca', 'lote', 'numero_v', 'statu')

@admin.register(Bezerro)
class BezerroAdmin(admin.ModelAdmin):
    list_display = ('nome_bezerro', 'numero_b', 'raca', 'lote')

@admin.register(Reprodutor)
class ReprodutorAdmin(admin.ModelAdmin):
    list_display = ('nome_reprodutor', 'numero_r', 'raca', 'lote')

@admin.register(Prenha)
class PrenhaAdmin(admin.ModelAdmin):
    list_display = ('vaca_id',)
