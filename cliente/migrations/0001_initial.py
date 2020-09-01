# Generated by Django 3.1 on 2020-09-01 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=20, verbose_name='Cargo')),
                ('descricao', models.CharField(blank=True, default='', max_length=50, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='Cliente')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('cnpj', models.CharField(blank=True, max_length=20, verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=60, verbose_name='E-Mail')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('cargo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cargo')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
        ),
        migrations.CreateModel(
            name='Relacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.responsavel')),
            ],
            options={
                'verbose_name': 'Relação',
                'verbose_name_plural': 'Relações',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='responsaveis',
            field=models.ManyToManyField(through='cliente.Relacao', to='cliente.Responsavel'),
        ),
    ]
