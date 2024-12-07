from django.contrib import admin
from cine.models import Categoria, CategoriaComida, Cine, Ciudad, Comida, Pelicula, Funcion, Entrada


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


class EntradaAdmin(admin.ModelAdmin):
    list_display = ['idEntrada', 'funcion', 'get_cantidad', 'get_total']
    search_fields = ['funcion__nombre']  # Buscar por el nombre de la función asociada
    list_filter = ['funcion']  # Filtrar por la función

    # Métodos para acceder a los atributos 'cantidad' y 'total' si no son campos directos
    def get_cantidad(self, obj):
        return obj.cantidad  # Asumiendo que cantidad es un campo en el modelo Entrada
    get_cantidad.admin_order_field = 'cantidad'  # Permite ordenar por cantidad
    get_cantidad.short_description = 'Cantidad de Entradas'  # Título en el admin

    def get_total(self, obj):
        return obj.total  # Asumiendo que total es un campo en el modelo Entrada
    get_total.admin_order_field = 'total'  # Permite ordenar por total
    get_total.short_description = 'Total'  # Título en el admin

class FuncionAdmin(admin.ModelAdmin):
    list_display = ['idFuncion', 'pelicula', 'get_fecha_hora', 'entradas_disponibles']
    search_fields = ['pelicula__titulo']  # Buscar por título de la película
    list_filter = ['pelicula', 'fecha_hora']  # Filtrar por película y fecha_hora

    # Método para mostrar la fecha y hora de la función de forma legible
    def get_fecha_hora(self, obj):
        return obj.fecha_hora.strftime('%d/%m/%Y %H:%M')  # Formato de fecha y hora
    get_fecha_hora.admin_order_field = 'fecha_hora'  # Permitir ordenar por fecha_hora
    get_fecha_hora.short_description = 'Fecha y Hora'



admin.site.register(Funcion, FuncionAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Comida, ComidaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Cine, CineAdmin)
admin.site.register(CategoriaComida, CategoriaComidaAdmin)