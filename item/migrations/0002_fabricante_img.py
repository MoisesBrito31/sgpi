# Generated by Django 3.1 on 2020-08-30 21:46

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='img',
            field=stdimage.models.StdImageField(blank=True, upload_to='fabricante', verbose_name='Imagem'),
        ),
    ]
