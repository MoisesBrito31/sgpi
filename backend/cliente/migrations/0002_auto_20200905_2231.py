# Generated by Django 3.1 on 2020-09-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=35, verbose_name='Cargo')),
                ('descricao', models.CharField(blank=True, default='', max_length=50, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'Indústria',
                'verbose_name_plural': 'Indústrias',
            },
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nome',
            field=models.CharField(max_length=35, verbose_name='Cargo'),
        ),
    ]
