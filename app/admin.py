from django.contrib import admin
from .models import *
from django.contrib import admin
admin.site.register(Medicamento)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
admin.site.register(Fornecedor)
admin.site.register(PedidoReposicao)
admin.site.register(ReceitaMedica)
admin.site.register(Relatorio)