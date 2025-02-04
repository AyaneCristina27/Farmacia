from django.contrib import admin
from .models import *
from django.contrib import admin

class MedicamentoReceitaInline(admin.TabularInline):
    model = MedicamentoReceita
    extra = 1

class ReceitaMedicaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "medico", "data_emissao")
    inlines = [ MedicamentoReceitaInline]

admin.site.register(Medicamento)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
admin.site.register(Fornecedor)
admin.site.register(PedidoReposicao)
admin.site.register(ReceitaMedica, ReceitaMedicaAdmin)
admin.site.register(Relatorio)