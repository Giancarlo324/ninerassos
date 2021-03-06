# Generated by Django 2.2.8 on 2020-05-06 05:49

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars_count', models.DecimalField(decimal_places=1, default=5, max_digits=2, verbose_name='calificación')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('body', models.TextField(verbose_name='Escribe el porqué dejas este comentario y calificación')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Hojavida',
            fields=[
                ('imagen', models.ImageField(upload_to='', verbose_name='Foto de perfil')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Identificación')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('birth_date', models.DateField(verbose_name='Fecha de nacimiento(mm/dd/yyyy)')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10, verbose_name='Sexo')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('num_telefono', models.IntegerField(verbose_name='Celular')),
                ('residencia', models.CharField(max_length=255, verbose_name='Dirección de residencia')),
                ('habilidades', models.TextField(verbose_name='Habilidades y aptitudes')),
                ('experiencia_lab', models.TextField(verbose_name='Experiencia laboral')),
                ('formacion', models.TextField(verbose_name='Formación académica')),
                ('stars_count', models.DecimalField(decimal_places=1, default=5, max_digits=2)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='Inicio de suscripción')),
                ('fecha_fin', models.DateTimeField(default=blog.models.now_plus_30, verbose_name='Fin de suscripción')),
                ('pagos', models.IntegerField(default=0, verbose_name='Pagos realizados')),
                ('title', models.CharField(max_length=200, verbose_name='Escribe un título a tu servicio')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='Escribe una breve descripción de como brindas tu servicio de niñera')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('suscripcion', models.IntegerField(choices=[(0, 'Finalizada'), (1, 'Activa')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
