from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MedicamentoView(View):
    def get(self, request, *args, **kwargs):
        medicamentos = Medicamento.objects.all()
        return render(request, 'medicamentos.html', {'medicamentos': medicamentos})


class ClienteView(View):
    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes})


class VendaView(View):
    def get(self, request, *args, **kwargs):
        vendas = Venda.objects.all()
        return render(request, 'vendas.html', {'vendas': vendas})


class FornecedorView(View):
    def get(self, request, *args, **kwargs):
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {'fornecedores': fornecedores})


class PedidoReposicaoView(View):
    def get(self, request, *args, **kwargs):
        pedidos = PedidoReposicao.objects.all()
        return render(request, 'pedidos.html', {'pedidos': pedidos})


class ReceitaMedicaView(View):
    def get(self, request, *args, **kwargs):
        receitas = ReceitaMedica.objects.all()
        print(dir(receitas))
        return render(request, 'receitas.html', {'receitas': receitas})


class RelatorioView(View):
    def get(self, request, *args, **kwargs):
        relatorios = Relatorio.objects.all()
        return render(request, 'relatorios.html', {'relatorios': relatorios})
