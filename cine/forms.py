from django import forms
from cine.models import Categoria, CategoriaComida, Pelicula, Comida, Ciudad, Cine
from django.core.exceptions import ValidationError


# Formulario para Categoria
class CategoriaForm(forms.ModelForm):
    nombreCategoria = forms.CharField(label='Nombre de la Categoría', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la categoría'}))
    descripcion = forms.CharField(label='Descripción',widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    imagenCategoria = forms.ImageField(label='Imagen de la categoria',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria   
        fields = '__all__'

# Formulario para Pelicula
class PeliculaForm(forms.ModelForm):
    titulo = forms.CharField(label='Nombre de la Pelicula',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la película'}))
    descripcion = forms.CharField(label='Descripción de la Pelicula',widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    fecha_estreno = forms.DateField(label='Fecha de estreno de la Pelicula',widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    duracion = forms.IntegerField(label='Duración de la Pelicula',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en minutos'}))
    categoria = forms.ModelChoiceField(label='Categoria de la Pelicula',queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    imagenPelicula = forms.ImageField(label='Imagen de la Pelicula',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Pelicula    
        fields = '__all__'
    
    def clean_duracion(self):
        duracion = self.cleaned_data['duracion']

        try:
            duracion = int(duracion)
        except ValueError:
            raise forms.ValidationError("La duración debe ser un número entero.")

        if duracion <= 0:
            raise forms.ValidationError('La duración debe ser mayor a 0 minutos.')
        return duracion

    def clean_fecha_estreno(self):
        fecha_estreno = self.cleaned_data.get('fecha_estreno')
        if fecha_estreno.year <= 1900:
            raise forms.ValidationError('La fecha de estreno debe ser posterior a 1900.')
        return fecha_estreno

# Formulario para Ciudad
class CiudadForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre de la ciudad',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la ciudad'}))
    pais = forms.CharField(label='Pais de la ciudad',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el país'}))
    imagenCiudad = forms.ImageField(label='Imagen de la ciudad',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Ciudad  
        fields = '__all__'

# Formulario para Cine
class CineForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del Cine',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del cine'}))
    direccion = forms.CharField(label='Dirección del cine',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección del cine'}))
    ciudad = forms.ModelChoiceField(label='Ciudad del cine',queryset=Ciudad.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    imagenCine = forms.ImageField(label='Imagen del cine',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cine    
        fields = '__all__'

# Formulario para Comida
class ComidaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre de la comida',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la comida'}))
    categoria = forms.ModelChoiceField(label='Tipo de comida',queryset=CategoriaComida.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    precio = forms.IntegerField(label='Precio de la comida',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}))
    imagenComida = forms.ImageField(label='Imagen de la comida',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comida  
        fields = '__all__'
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']

        try:
            precio = int(precio)
        except ValueError:
            raise forms.ValidationError("El precio debe ser un número entero.")


        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return precio

# Formulario para Categoria Comida
class CategoriaComidaForm(forms.ModelForm):
    nombreCategoriaComida = forms.CharField(label='Nombre de la Categoría de comida',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la categoria'}))
    descripcionCategoria = forms.CharField(label='Descripción de la Categoría de comida',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el descripción de la categoria'}))
    imagenCatComida = forms.ImageField(label='Imagen de la Categoría de comida',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CategoriaComida
        fields = '__all__'