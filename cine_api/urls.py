from django.urls import path
from cine_api import views as vista

urlpatterns = [
    #JSON
    path('categoriasapi/', vista.categoria_api, name='categoria_api'),
    path('peliculasapi/', vista.pelicula_api, name='pelicula_api'),
    path('categorias-comidaapi/', vista.categoria_comida_api, name='categoria_comida_api'),
    path('comidasapi/', vista.comida_api, name='comida_api'),
    path('ciudadesapi/', vista.ciudad_api, name='ciudad_api'),
    path('cinesapi/', vista.cine_api, name='cine_api'),
    path('funcionesapi/', vista.funcion_api, name='funcion_api'),
    path('entradasapi/', vista.entrada_api, name='entrada_api'),

    #
    path('categorias/', vista.categoria_listado, name='categoria_listado'),
    path('categorias/<int:pk>/', vista.categoria_detalle, name='categoria_detalle'),

    path('peliculas/', vista.pelicula_listado, name='pelicula_listado'),
    path('peliculas/<int:pk>/', vista.pelicula_detalle, name='pelicula_detalle'),

    path('categorias-comida/', vista.categoria_comida_listado, name='categoria_comida_listado'),
    path('categorias-comida/<int:pk>/', vista.categoria_comida_detalle, name='categoria_comida_detalle'),

    path('comidas/', vista.comida_listado, name='comida_listado'),
    path('comidas/<int:pk>/', vista.comida_detalle, name='comida_detalle'),

    path('ciudades/', vista.ciudad_listado, name='ciudad_listado'),
    path('ciudades/<int:pk>/', vista.ciudad_detalle, name='ciudad_detalle'),

    path('cines/', vista.cine_listado, name='cine_listado'),
    path('cines/<int:pk>/', vista.cine_detalle, name='cine_detalle'),

    path('funciones/', vista.funcion_listado, name='funcion_listado'),
    path('funciones/<int:pk>/', vista.funcion_detalle, name='funcion_detalle'),

    path('entradas/', vista.entrada_listado, name='entrada_listado'),
    path('entradas/<int:pk>/', vista.entrada_detalle, name='entrada_detalle'),
]

