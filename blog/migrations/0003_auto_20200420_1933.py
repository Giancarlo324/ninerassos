# Generated by Django 2.2.8 on 2020-04-21 00:33

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200419_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojavida',
            name='fecha_fin',
            field=models.DateTimeField(default=blog.models.now_plus_30, verbose_name='Fin de suscripción'),
        ),
        migrations.AddField(
            model_name='hojavida',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True, default='1998-08-08', verbose_name='Inicio de suscripción'),
            preserve_default=False,
        ),
    ]