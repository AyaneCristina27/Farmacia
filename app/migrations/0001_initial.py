# Generated by Django 5.1.5 on 2025-01-21 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('contato', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('fabricante', models.CharField(max_length=200)),
                ('validade', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('vendas', 'Vendas'), ('estoque', 'Estoque'), ('conformidade', 'Conformidade')], max_length=20)),
                ('data_geracao', models.DateTimeField(auto_now_add=True)),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicamentoReceita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_prescrita', models.PositiveIntegerField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoReposicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_transito', 'Em Trânsito'), ('entregue', 'Entregue')], default='pendente', max_length=20)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fornecedor')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='ReceitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.CharField(max_length=200)),
                ('data_emissao', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('medicamentos', models.ManyToManyField(through='app.MedicamentoReceita', to='app.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='medicamentoreceita',
            name='receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.receitamedica'),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicamento')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='app.venda')),
            ],
        ),
    ]
