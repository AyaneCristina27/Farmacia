from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('medicamentos/', MedicamentoView.as_view(), name='medicamentos'),
    path('clientes/', ClienteView.as_view(), name='clientes'),
    path('vendas/', VendaView.as_view(), name='vendas'),
    path('fornecedores/', FornecedorView.as_view(), name='fornecedores'),
    path('pedidos/', PedidoReposicaoView.as_view(), name='pedidos'),
    path('receitas/', ReceitaMedicaView.as_view(), name='receitas'),
    path('relatorios/', RelatorioView.as_view(), name='relatorios'),
]
