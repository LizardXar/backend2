from django.urls import path,include
from cine import views as vista


urlpatterns = [
    # ---------------- Registro y mantenedor usuarios ----------#
    path('usuarios/', vista.todos_usuarios, name='usuarios'),
    path('usuarioAdd/', vista.crear_usuario, name='crearUsuario'),
    path('usuarioEdit/<int:idUsuario>/', vista.cargar_editar_usuario, name='cargarEditarUsuario'),
    path('usuarioEditado/<int:idUsuario>/', vista.editar_usuario, name='editarUsuario'),
    path('usuarioDel/<int:idUsuario>/', vista.eliminar_usuario, name='eliminarUsuario'),

    # --------------- Contenido principal ----------#
    path('index/', vista.index, name='index'),
    path('categoria/<int:idCategoria>/', vista.peliculas_por_categoria, name='peliculas_por_categoria'),
    path('cinesciudades/', vista.cine_cards, name='cine_cards'),
    path('cines_por_ciudades/<int:idCiudad>/', vista.cines_por_ciudad, name='cines_por_ciudad'),
    path('comidascategorias/', vista.comidas_cards, name='comidas_cards'),
    path('comidas/<int:idCategoriaComida>/', vista.comidas_por_categoria, name='comidas_por_categoria'),

    # -------------- Categoría Comidas ----------- #
    path('categoria_comidas/', vista.todos_categoria_comida, name='categoriasComidas'),
    path('categoria_comidasAdd/', vista.crear_categoria_comida, name='crearCategoriaComida'),
    path('categoria_comidaEdit/<int:idCategoriaComida>/', vista.cargar_editar_categoria_comida, name='editarCategoriaComida'),
    path('categoria_comidaEditado/<int:idCategoriaComida>/', vista.editar_categoria_comida, name='categoriaComidaEditado'),
    path('categoria_comidaDel/<int:idCategoriaComida>/', vista.eliminar_categoria_comida, name='eliminarCategoriaComida'),

    # ----------------- Comidas ----------------- #
    path('comidas/', vista.todos_comida, name='comidas'),
    path('comidasAdd/', vista.crear_comida, name='crearComidas'),
    path('comidaEdit/<int:idComida>/', vista.cargar_editar_comida, name='editarComida'),
    path('comidaEditado/<int:idComida>/', vista.editar_comida, name='comidaEditado'),
    path('comidaDel/<int:idComida>/', vista.eliminar_comida, name='eliminarComida'),

    # -------------- Categorías ------------------ #
    path('categorias/', vista.todos_categoria, name='categorias'),
    path('categoriaAdd/', vista.crear_categoria, name='crearCategoria'),
    path('categoriaEdit/<int:idCategoria>/', vista.cargar_editar_categoria, name='editarCategoria'),
    path('categoriaEditado/<int:idCategoria>/', vista.editar_categoria, name='categoriaEditado'),
    path('categoriaDel/<int:idCategoria>/', vista.eliminar_categoria, name='eliminarCategoria'),

    # ---------------- Películas ----------------- #
    path('peliculas/', vista.todos_pelicula, name='peliculas'),
    path('peliculaAdd/', vista.crear_pelicula, name='crearPelicula'),
    path('peliculaEdit/<int:idPelicula>/', vista.cargar_editar_pelicula, name='editarPelicula'),
    path('peliculaEditado/<int:idPelicula>/', vista.editar_pelicula, name='peliculaEditado'),
    path('peliculaDel/<int:idPelicula>/', vista.eliminar_pelicula, name='eliminarPelicula'),

    # ---------------- Cines --------------------- #
    path('cines/', vista.todos_cine, name='cines'),
    path('cineAdd/', vista.crear_cine, name='crearCine'),
    path('cineEdit/<int:idCine>/', vista.cargar_editar_cine, name='editarCine'),
    path('cineEditado/<int:idCine>/', vista.editar_cine, name='cineEditado'),
    path('cineDel/<int:idCine>/', vista.eliminar_cine, name='eliminarCine'),

    # ---------------- Ciudades ------------------ #
    path('ciudades/', vista.todos_ciudad, name='ciudades'),
    path('ciudadAdd/', vista.crear_ciudad, name='crearCiudad'),
    path('ciudadEdit/<int:idCiudad>/', vista.cargar_editar_ciudad, name='editarCiudad'),
    path('ciudadEditado/<int:idCiudad>/', vista.editar_ciudad, name='ciudadEditado'),
    path('ciudadDel/<int:idCiudad>/', vista.eliminar_ciudad, name='eliminarCiudad'),
]