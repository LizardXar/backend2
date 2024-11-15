from django.db import models
import os
from django.utils import timezone



class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200, default='Descripción generica')

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'categoria'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)
    
    imagenCategoria = models.ImageField(upload_to=generarNombre, null=True, default='categoria/categoria.png')

    def __str__(self):
        return f"{self.nombreCategoria}"

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    duracion = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'peliculas'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)
    
    imagenPelicula = models.ImageField(upload_to=generarNombre, null=True, default='peliculas/pelicula.png')


    def __str__(self):
        return f"{self.titulo}"

    class Meta:
        db_table = 'pelicula'
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'

class CategoriaComida(models.Model):
    idCategoriaComida = models.AutoField(primary_key=True)
    nombreCategoriaComida = models.CharField(max_length=200)
    descripcionCategoria = models.CharField(max_length=200)

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'catcomida'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)

    imagenCatComida = models.ImageField(upload_to=generarNombre, null=True, default='catcomida/catcomida.png')

    def __str__(self):
        return f"{self.nombreCategoriaComida}"
    
    class Meta:
        db_table = 'categoria_comida'
        verbose_name = 'Categoria comida'
        verbose_name_plural = 'Categorias comida'

class Comida(models.Model):
    idComida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaComida, on_delete=models.CASCADE)
    precio = models.IntegerField()

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'comidas'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)

    imagenComida = models.ImageField(upload_to=generarNombre, null=True, default='comidas/comida.png')

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

    class Meta:
        db_table = 'comida'
        verbose_name = 'Comida'
        verbose_name_plural = 'Comidas'

class Ciudad(models.Model):
    idCiudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'ciudad'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)

    imagenCiudad = models.ImageField(upload_to=generarNombre, null=True, default='ciudad/ciudad.png')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ciudad'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class Cine(models.Model):
    idCine = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad, null=False, on_delete=models.CASCADE)

    def generarNombre(instance,filename):
        extension = 'png'
        ruta = 'cine'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)

    imagenCine = models.ImageField(upload_to=generarNombre, null=True, default='cine/cine.png')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cine'
        verbose_name = 'Cine'
        verbose_name_plural = 'Cines'
























