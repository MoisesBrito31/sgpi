# Generated by Django 3.1 on 2020-09-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjunto', '0002_auto_20200831_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='conjunto',
            name='descricao',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='Descrição'),
        ),
    ]
