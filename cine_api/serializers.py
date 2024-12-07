from rest_framework import serializers
from cine.models import (
    Categoria, Pelicula, CategoriaComida, Comida, Ciudad, Cine, Funcion, Entrada
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class CategoriaComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaComida
        fields = '__all__'

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class CineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cine
        fields = '__all__'

class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = '__all__'

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'
