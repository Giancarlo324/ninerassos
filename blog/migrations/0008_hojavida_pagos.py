# Generated by Django 2.2.8 on 2020-04-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200422_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojavida',
            name='pagos',
            field=models.IntegerField(default=0, verbose_name='Pagos realizados'),
        ),
    ]
