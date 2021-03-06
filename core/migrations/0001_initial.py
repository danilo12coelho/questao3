# Generated by Django 2.1.5 on 2019-01-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_festa', models.DateField(verbose_name='Data da Festa')),
                ('hora_inicio', models.TimeField(verbose_name='Horario de Inicio')),
                ('hora_termino', models.TimeField(verbose_name='Horario de Termino')),
                ('valor_cobrado', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor cobrado')),
            ],
            options={
                'verbose_name': 'Aluguel',
                'verbose_name_plural': 'Alugueis',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.DateField()),
                ('telefone', models.TimeField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero')),
                ('complemento', models.CharField(max_length=100, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=20, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=3, verbose_name='UF')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='ItemTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Item do Tema',
                'verbose_name_plural': 'Itens do Tema',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('valor_aluguel', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor do aluguel')),
                ('cor_toalha', models.CharField(max_length=50, verbose_name='Cor da Toalha')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
    ]
