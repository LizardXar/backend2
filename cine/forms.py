from django import forms
from cine.models import Categoria, CategoriaComida, Pelicula, Comida, Ciudad, Cine
from django.core.exceptions import ValidationError


# Formulario para Categoria
class CategoriaForm(forms.ModelForm):
    nombreCategoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la categoría'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    imagenCategoria = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria   
        fields = '__all__'

# Formulario para Pelicula
class PeliculaForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la película'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    fecha_estreno = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    duracion = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en minutos'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    imagenPelicula = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

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
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la ciudad'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el país'}))
    imagenCiudad = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Ciudad  
        fields = '__all__'

# Formulario para Cine
class CineForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del cine'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección del cine'}))
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    imagenCine = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cine    
        fields = '__all__'

# Formulario para Comida
class ComidaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la comida'}))
    categoria = forms.ModelChoiceField(queryset=CategoriaComida.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}))
    imagenComida = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

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
    nombreCategoriaComida = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la categoria'}))
    descripcionCategoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el descripción de la categoria'}))
    imagenCatComida = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CategoriaComida
        fields = '__all__'