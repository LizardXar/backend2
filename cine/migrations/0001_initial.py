# Generated by Django 5.1 on 2024-11-15 03:25

import cine.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField(default='Descripción generica', max_length=200)),
                ('imagenCategoria', models.ImageField(default='categoria/categoria.png', null=True, upload_to=cine.models.Categoria.generarNombre)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='CategoriaComida',
            fields=[
                ('idCategoriaComida', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoriaComida', models.CharField(max_length=200)),
                ('descripcionCategoria', models.CharField(max_length=200)),
                ('imagenCatComida', models.ImageField(default='catcomida/catcomida.png', null=True, upload_to=cine.models.CategoriaComida.generarNombre)),
            ],
            options={
                'verbose_name': 'Categoria comida',
                'verbose_name_plural': 'Categorias comida',
                'db_table': 'categoria_comida',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('imagenCiudad', models.ImageField(default='ciudad/ciudad.png', null=True, upload_to=cine.models.Ciudad.generarNombre)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'db_table': 'ciudad',
            },
        ),
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('idCine', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=300)),
                ('imagenCine', models.ImageField(default='cine/cine.png', null=True, upload_to=cine.models.Cine.generarNombre)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.ciudad')),
            ],
            options={
                'verbose_name': 'Cine',
                'verbose_name_plural': 'Cines',
                'db_table': 'cine',
            },
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('idComida', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('imagenComida', models.ImageField(default='comidas/comida.png', null=True, upload_to=cine.models.Comida.generarNombre)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.categoriacomida')),
            ],
            options={
                'verbose_name': 'Comida',
                'verbose_name_plural': 'Comidas',
                'db_table': 'comida',
            },
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('idPelicula', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_estreno', models.DateField()),
                ('duracion', models.PositiveIntegerField()),
                ('imagenPelicula', models.ImageField(default='peliculas/pelicula.png', null=True, upload_to=cine.models.Pelicula.generarNombre)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.categoria')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
                'db_table': 'pelicula',
            },
        ),
    ]
