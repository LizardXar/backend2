from django.shortcuts import render
from django.http import JsonResponse
from cine.models import (
    Categoria, Pelicula, CategoriaComida, Comida, 
    Ciudad, Cine, Funcion, Entrada
)
from cine_api.serializers import (
CategoriaSerializer, PeliculaSerializer, CategoriaComidaSerializer, 
ComidaSerializer, CiudadSerializer, CineSerializer, 
FuncionSerializer, EntradaSerializer)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def categoria_api(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias': list(
            categorias.values('idCategoria', 'nombreCategoria', 'descripcion', 'imagenCategoria')
        )
    }
    return JsonResponse(data)

def pelicula_api(request):
    peliculas = Pelicula.objects.all()
    data = {
        'peliculas': list(
            peliculas.values(
                'idPelicula', 'titulo', 'descripcion', 'fecha_estreno', 
                'duracion', 'categoria__nombreCategoria', 'imagenPelicula'
            )
        )
    }
    return JsonResponse(data)

def categoria_comida_api(request):
    categorias_comida = CategoriaComida.objects.all()
    data = {
        'categorias_comida': list(
            categorias_comida.values(
                'idCategoriaComida', 'nombreCategoriaComida', 
                'descripcionCategoria', 'imagenCatComida'
            )
        )
    }
    return JsonResponse(data)

def comida_api(request):
    comidas = Comida.objects.all()
    data = {
        'comidas': list(
            comidas.values(
                'idComida', 'nombre', 'categoria__nombreCategoriaComida', 
                'precio', 'imagenComida'
            )
        )
    }
    return JsonResponse(data)

def ciudad_api(request):
    ciudades = Ciudad.objects.all()
    data = {
        'ciudades': list(
            ciudades.values('idCiudad', 'nombre', 'pais', 'imagenCiudad')
        )
    }
    return JsonResponse(data)

def cine_api(request):
    cines = Cine.objects.all()
    data = {
        'cines': list(
            cines.values(
                'idCine', 'nombre', 'direccion', 
                'ciudad__nombre', 'imagenCine'
            )
        )
    }
    return JsonResponse(data)

def funcion_api(request):
    funciones = Funcion.objects.all()
    data = {
        'funciones': list(
            funciones.values(
                'idFuncion', 'pelicula__titulo', 'fecha_hora', 
                'entradas_disponibles'
            )
        )
    }
    return JsonResponse(data)

def entrada_api(request):
    entradas = Entrada.objects.all()
    data = {
        'entradas': list(
            entradas.values(
                'idEntrada', 'funcion__pelicula__titulo', 
                'precio', 'vendida'
            )
        )
    }
    return JsonResponse(data)

# Categoría
@api_view(['GET', 'POST'])
def categoria_listado(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detalle(request, pk):
    try:
        categoria = Categoria.objects.get(idCategoria=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Película
@api_view(['GET', 'POST'])
def pelicula_listado(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pelicula_detalle(request, pk):
    try:
        pelicula = Pelicula.objects.get(idPelicula=pk)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeliculaSerializer(pelicula)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        pelicula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CategoriaComida
@api_view(['GET', 'POST'])
def categoria_comida_listado(request):
    if request.method == 'GET':
        categorias_comida = CategoriaComida.objects.all()
        serializer = CategoriaComidaSerializer(categorias_comida, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoriaComidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_comida_detalle(request, pk):
    try:
        categoria_comida = CategoriaComida.objects.get(idCategoriaComida=pk)
    except CategoriaComida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaComidaSerializer(categoria_comida)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CategoriaComidaSerializer(categoria_comida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categoria_comida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Comida
@api_view(['GET', 'POST'])
def comida_listado(request):
    if request.method == 'GET':
        comidas = Comida.objects.all()
        serializer = ComidaSerializer(comidas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ComidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comida_detalle(request, pk):
    try:
        comida = Comida.objects.get(idComida=pk)
    except Comida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComidaSerializer(comida)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ComidaSerializer(comida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        comida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Ciudad
@api_view(['GET', 'POST'])
def ciudad_listado(request):
    if request.method == 'GET':
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ciudad_detalle(request, pk):
    try:
        ciudad = Ciudad.objects.get(idCiudad=pk)
    except Ciudad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CiudadSerializer(ciudad)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CiudadSerializer(ciudad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ciudad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Cine
@api_view(['GET', 'POST'])
def cine_listado(request):
    if request.method == 'GET':
        cines = Cine.objects.all()
        serializer = CineSerializer(cines, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cine_detalle(request, pk):
    try:
        cine = Cine.objects.get(idCine=pk)
    except Cine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CineSerializer(cine)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CineSerializer(cine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        cine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Funcion
@api_view(['GET', 'POST'])
def funcion_listado(request):
    if request.method == 'GET':
        funciones = Funcion.objects.all()
        serializer = FuncionSerializer(funciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FuncionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def funcion_detalle(request, pk):
    try:
        funcion = Funcion.objects.get(idFuncion=pk)
    except Funcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionSerializer(funcion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FuncionSerializer(funcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        funcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Entrada
@api_view(['GET', 'POST'])
def entrada_listado(request):
    if request.method == 'GET':
        entradas = Entrada.objects.all()
        serializer = EntradaSerializer(entradas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EntradaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def entrada_detalle(request, pk):
    try:
        entrada = Entrada.objects.get(idEntrada=pk)
    except Entrada.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EntradaSerializer(entrada)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EntradaSerializer(entrada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        entrada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
