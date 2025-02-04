from django.db import models
from django.contrib.auth.models import User

class Medicamento(models.Model):
    nome = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    validade = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.id} - {self.cliente.nome}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.medicamento.nome}"

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    contato = models.CharField(max_length=200)
    email = models.EmailField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class PedidoReposicao(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('em_transito', 'Em Trânsito'),
            ('entregue', 'Entregue'),
        ],
        default='pendente'
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.medicamento.nome} ({self.status})"

class ReceitaMedica(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico = models.CharField(max_length=200)
    data_emissao = models.DateField()
    medicamentos = models.ManyToManyField(Medicamento, through='MedicamentoReceita')

    def __str__(self):
        return f"Receita {self.id} - {self.cliente.nome}"

class MedicamentoReceita(models.Model):
    receita = models.ForeignKey(ReceitaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade_prescrita = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicamento.nome} ({self.quantidade_prescrita})"

class Relatorio(models.Model):
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('vendas', 'Vendas'),
            ('estoque', 'Estoque'),
            ('conformidade', 'Conformidade'),
        ]
    )
    data_geracao = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f"Relatório {self.tipo} - {self.data_geracao.strftime('%Y-%m-%d')}"
