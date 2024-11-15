from django.contrib import admin
from cine.models import Categoria, CategoriaComida, Cine, Ciudad, Comida, Pelicula


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['idCategoria', 'descripcion', 'nombreCategoria']

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['idPelicula', 'titulo', 'descripcion', 'fecha_estreno', 'duracion', 'categoria']

class ComidaAdmin(admin.ModelAdmin):
    list_display = ['idComida', 'nombre', 'categoria', 'precio']

class CiudadAdmin(admin.ModelAdmin):
    list_display = ['idCiudad', 'nombre', 'pais']

class CineAdmin(admin.ModelAdmin):
    list_display = ['idCine', 'nombre', 'direccion', 'ciudad']

class CategoriaComidaAdmin(admin.ModelAdmin):
    list_display = ['idCategoriaComida', 'nombreCategoriaComida']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Comida, ComidaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Cine, CineAdmin)
admin.site.register(CategoriaComida, CategoriaComidaAdmin)