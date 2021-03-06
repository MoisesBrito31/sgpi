# Generated by Django 3.1 on 2020-09-11 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20200910_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cargo'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=60, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='telefone',
            field=models.CharField(blank=True, default='-', max_length=30, verbose_name='Telefone'),
        ),
    ]
