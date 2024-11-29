from django import forms
from cine.models import Categoria, CategoriaComida, Pelicula, Comida, Ciudad, Cine
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

# Formulario para Categoria
class CategoriaForm(forms.ModelForm):
    nombreCategoria = forms.CharField(label='Nombre de la Categoría', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la categoría'}))
    descripcion = forms.CharField(label='Descripción',widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    imagenCategoria = forms.ImageField(label='Imagen de la categoria',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria   
        fields = '__all__'

    def clean_nombreCategoria(self):
        nombre = self.cleaned_data.get('nombreCategoria')
        if len(nombre) < 3 or len(nombre) > 30:
            raise forms.ValidationError('El nombre de la categoria debe tener entre 3 y 30 caracteres.')
        return nombre
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 3 or len(descripcion) > 200:
            raise forms.ValidationError('La descripcion de la categoria debe tener entre 3 y 200 caracteres.')
        return descripcion    
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
        if fecha_estreno.year >= 2050:
            raise forms.ValidationError('La fecha de estreno debe ser anterior a 2050.')
        return fecha_estreno
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 2 or len(titulo) > 50:
            raise forms.ValidationError('El titulo debe tener entre 2 y 50 caracteres.')
        return titulo
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 3 or len(descripcion) > 300:
            raise forms.ValidationError('La descripcion debe tener entre 3 y 300 caracteres.')
        return descripcion

# Formulario para Ciudad
class CiudadForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre de la ciudad',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la ciudad'}))
    pais = forms.CharField(label='Pais de la ciudad',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el país'}))
    imagenCiudad = forms.ImageField(label='Imagen de la ciudad',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Ciudad  
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3 or len(nombre) > 30:
            raise forms.ValidationError('El nombre de la ciudad debe tener entre 3 y 30 caracteres.')
        return nombre
# Formulario para Cine
class CineForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del Cine',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del cine'}))
    direccion = forms.CharField(label='Dirección del cine',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección del cine'}))
    ciudad = forms.ModelChoiceField(label='Ciudad del cine',queryset=Ciudad.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    imagenCine = forms.ImageField(label='Imagen del cine',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cine    
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3 or len(nombre) > 50:
            raise forms.ValidationError('El nombre del cine debe tener entre 3 y 50 caracteres.')
        return nombre
    
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if len(direccion) < 3 or len(direccion) > 50:
            raise forms.ValidationError('La direccion del cine debe tener entre 3 y 50 caracteres.')
        return direccion

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
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3 or len(nombre) > 50:
            raise forms.ValidationError('El nombre de la comida debe tener entre 3 y 50 caracteres.')
        return nombre

# Formulario para Categoria Comida
class CategoriaComidaForm(forms.ModelForm):
    nombreCategoriaComida = forms.CharField(label='Nombre de la Categoría de comida',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la categoria'}))
    descripcionCategoria = forms.CharField(label='Descripción de la Categoría de comida',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el descripción de la categoria'}))
    imagenCatComida = forms.ImageField(label='Imagen de la Categoría de comida',required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CategoriaComida
        fields = '__all__'
    
    def clean_nombreCategoriaComida(self):
        nombre = self.cleaned_data.get('nombreCategoriaComida')
        if len(nombre) < 3 or len(nombre) > 50:
            raise forms.ValidationError('El nombre de la categoría debe tener entre 3 y 50 caracteres.')
        return nombre

    def clean_descripcionCategoria(self):
        descripcion = self.cleaned_data.get('descripcionCategoria')
        if len(descripcion) < 5 or len(descripcion) > 200:
            raise forms.ValidationError('La descripción de la categoría debe tener entre 5 y 200 caracteres.')
        return descripcion


# Formulario para registrar usuarios
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label="Nombre de Usuario")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True, label="Correo Electrónico")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label="Nombre")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label="Apellido")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False, label="Confirmar Contraseña")
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True, label="Grupo:")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'grupo']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if self.instance and self.instance.pk:
            if not password and not confirm_password:
                return cleaned_data
        else:
            if not password:
                self.add_error('password', "Debes ingresar una contraseña")
            if not confirm_password:
                self.add_error('confirm_password', "Debes confirmar tu contraseña")

            if password != confirm_password:
                self.add_error('password', "Las contraseñas no coinciden")
                self.add_error('confirm_password', "Las contraseñas no coinciden")
            
            if len(password) < 8:
                self.add_error('password', "La contraseña debe tener un mínimo de 8 caracteres")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3 or len(username) > 20:
            raise forms.ValidationError('El nombre de usuario debe tener entre 3 y 20 caracteres.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) < 3 or len(email) > 50:
            raise forms.ValidationError('El correo electrónico debe tener entre 3 y 50 caracteres.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3 or len(first_name) > 20:
            raise forms.ValidationError('El nombre debe tener entre 3 y 20 caracteres.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3 or len(last_name) > 20:
            raise forms.ValidationError('El apellido debe tener entre 3 y 20 caracteres.')
        return last_name
