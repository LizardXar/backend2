from django.shortcuts import render, redirect, get_object_or_404
from cine.forms import ComidaForm, CategoriaComidaForm, CineForm, CiudadForm, CategoriaForm, PeliculaForm
from cine.models import Comida, CategoriaComida, Cine, Ciudad, Categoria, Pelicula

# Create your views here.
# --------------------- Paginas principales --------------------#
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'cine/index.html', {'categorias':categorias})

def peliculas_por_categoria(request, idCategoria):
    categoria = get_object_or_404(Categoria, idCategoria=idCategoria)
    peliculas = Pelicula.objects.filter(categoria=categoria)
    return render(request, 'cine/peliculas_por_categoria.html', {'categoria': categoria, 'peliculas': peliculas})

def cine_cards(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'cine/cinesciudades.html', {'ciudades':ciudades})

def cines_por_ciudad(request, idCiudad):
    ciudad = get_object_or_404(Ciudad, idCiudad=idCiudad)
    cines = Cine.objects.filter(ciudad=ciudad)
    return render(request, 'cine/cines_por_ciudades.html', {'cines':cines})

def comidas_cards(request):
    categoria_comida = CategoriaComida.objects.all()
    return render(request, 'cine/comidascategorias.html', {'categoria_comida':categoria_comida})

def comidas_por_categoria(request, idCategoriaComida):
    categoria = get_object_or_404(CategoriaComida, idCategoriaComida=idCategoriaComida)
    comidas = Comida.objects.filter(categoria=categoria)
    return render(request, 'cine/comidas_por_categoria.html', {'categoria':categoria, 'comidas':comidas})

#---------------------- COMIDAS -------------------------#
def todos_comida(request):
    comidas = Comida.objects.all()
    return render(request, 'cine/comidas.html', {'comidas':comidas})

def crear_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/comidas/')
    else:
        form = ComidaForm()

    return render(request, 'cine/comidaAdd.html', {'form': form})

def cargar_editar_comida(request, idComida):
    comida = get_object_or_404(Comida, idComida=idComida)
    form = ComidaForm(instance=comida)
    return render(request, 'cine/comidaEdit.html', { 'form': form, 'comida':comida })

def editar_comida(request, idComida):
    comida = get_object_or_404(Comida, idComida=idComida)

    if request.method == 'POST':
        form = ComidaForm(request.POST, request.FILES, instance=comida)
        if form.is_valid():
            if 'imagenComida' in request.FILES:
                comida.imagenComida = request.FILES['imagenComida']
            form.save()
            return redirect('/cine/comidas/')

    else:
        form = ComidaForm(instance=comida)

    return render(request, 'cine/comidaEdit.html', {'form': form, 'comida': comida})

def eliminar_comida(request, idComida):
    comida = get_object_or_404(Comida, idComida=idComida)
    
    if request.method == 'POST':
        comida.delete()
        return redirect('/cine/comidas/')
    
    return render(request, 'cine/comidaDel.html', {'comida':comida})

# ---------------------- CATEGORIA ----------------------#
def todos_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'cine/categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/categorias/')
    else:
        form = CategoriaForm()

    return render(request, 'cine/categoriaAdd.html', {'form': form})

def cargar_editar_categoria(request, idCategoria):
    categoria = get_object_or_404(Categoria, idCategoria=idCategoria)
    form = CategoriaForm(instance=categoria)
    return render(request, 'cine/categoriaEdit.html', {'form': form, 'categoria': categoria})

def editar_categoria(request, idCategoria):
    categoria = get_object_or_404(Categoria, idCategoria=idCategoria)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            if 'imagenCategoria' in request.FILES:
                categoria.imagenCategoria = request.FILES['imagenCategoria']
            form.save()
            return redirect('/cine/categorias/')

    return render(request, 'cine/categoriaEdit.html', {'form': form})

def eliminar_categoria(request, idCategoria):
    categoria = get_object_or_404(Categoria, idCategoria=idCategoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('/cine/categorias/')

    return render(request, 'cine/categoriaDel.html', {'categoria': categoria})

# ---------------------- PELICULA ----------------------#
def todos_pelicula(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'cine/peliculas.html', {'peliculas': peliculas})

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/peliculas/')
    else:
        form = PeliculaForm()

    return render(request, 'cine/peliculaAdd.html', {'form': form})

def cargar_editar_pelicula(request, idPelicula):
    pelicula = get_object_or_404(Pelicula, idPelicula=idPelicula)
    form = PeliculaForm(instance=pelicula)
    return render(request, 'cine/peliculaEdit.html', {'form': form, 'pelicula': pelicula})

def editar_pelicula(request, idPelicula):
    pelicula = get_object_or_404(Pelicula, idPelicula=idPelicula)

    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            if 'imagenPelicula' in request.FILES:
                pelicula.imagenPelicula = request.FILES['imagenPelicula']
            form.save()
            return redirect('/cine/peliculas/')

    return render(request, 'cine/peliculaEdit.html', {'form': form})

def eliminar_pelicula(request, idPelicula):
    pelicula = get_object_or_404(Pelicula, idPelicula=idPelicula)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('/cine/peliculas/')

    return render(request, 'cine/peliculaDel.html', {'pelicula': pelicula})

# ---------------------- CIUDAD ----------------------#
def todos_ciudad(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'cine/ciudades.html', {'ciudades': ciudades})

def crear_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/ciudades/')
    else:
        form = CiudadForm()

    return render(request, 'cine/ciudadAdd.html', {'form': form})

def cargar_editar_ciudad(request, idCiudad):
    ciudad = get_object_or_404(Ciudad, idCiudad=idCiudad)
    form = CiudadForm(instance=ciudad)
    return render(request, 'cine/ciudadEdit.html', {'form': form, 'ciudad': ciudad})

def editar_ciudad(request, idCiudad):
    ciudad = get_object_or_404(Ciudad, idCiudad=idCiudad)

    if request.method == 'POST':
        form = CiudadForm(request.POST, request.FILES, instance=ciudad)
        if form.is_valid():
            if 'imagenCiudad' in request.FILES:
                ciudad.imagenCiudad = request.FILES['imagenCiudad']
            form.save()
            return redirect('/cine/ciudades/')

    return render(request, 'cine/ciudadEdit.html', {'form': form})

def eliminar_ciudad(request, idCiudad):
    ciudad = get_object_or_404(Ciudad, idCiudad=idCiudad)
    if request.method == 'POST':
        ciudad.delete()
        return redirect('/cine/ciudades/')

    return render(request, 'cine/ciudadDel.html', {'ciudad': ciudad})

# ---------------------- CINE ----------------------#
def todos_cine(request):
    cines = Cine.objects.all()
    return render(request, 'cine/cines.html', {'cines': cines})

def crear_cine(request):
    if request.method == 'POST':
        form = CineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/cines/')
    else:
        form = CineForm()

    return render(request, 'cine/cineAdd.html', {'form': form})

def cargar_editar_cine(request, idCine):
    cine = get_object_or_404(Cine, idCine=idCine)
    form = CineForm(instance=cine)
    return render(request, 'cine/cineEdit.html', {'form': form, 'cine': cine})

def editar_cine(request, idCine):
    cine = get_object_or_404(Cine, idCine=idCine)

    if request.method == 'POST':
        form = CineForm(request.POST, request.FILES, instance=cine)
        if form.is_valid():
            if 'imagenCine' in request.FILES:
                cine.imagenCine = request.FILES['imagenCine']
            form.save()
            return redirect('/cine/cines/')

    return render(request, 'cine/cineEdit.html', {'form': form})

def eliminar_cine(request, idCine):
    cine = get_object_or_404(Cine, idCine=idCine)
    if request.method == 'POST':
        cine.delete()
        return redirect('/cine/cines/')

    return render(request, 'cine/cineDel.html', {'cine': cine})

# ---------------------- CATEGORIA COMIDAS ----------------------#
def todos_categoria_comida(request):
    categorias_comidas = CategoriaComida.objects.all()
    return render(request, 'cine/categoria_comidas.html', {'categorias_comidas': categorias_comidas})

def crear_categoria_comida(request):
    if request.method == 'POST':
        form = CategoriaComidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cine/categoria_comidas/')
    else:
        form = CategoriaComidaForm()

    return render(request, 'cine/categoria_comidaAdd.html', {'form': form})

def cargar_editar_categoria_comida(request, idCategoriaComida):
    categoria_comida = get_object_or_404(CategoriaComida, idCategoriaComida=idCategoriaComida)
    form = CategoriaComidaForm(instance=categoria_comida)
    return render(request, 'cine/categoria_comidaEdit.html', {'form': form, 'categoria_comida': categoria_comida})

def editar_categoria_comida(request, idCategoriaComida):
    categoria_comida = get_object_or_404(CategoriaComida, idCategoriaComida=idCategoriaComida)

    if request.method == 'POST':
        form = CategoriaComidaForm(request.POST, request.FILES, instance=categoria_comida)
        if form.is_valid():
            if 'imagenCatComida' in request.FILES:
                categoria_comida.imagenCatComida = request.FILES['imagenCatComida']
            form.save()
            return redirect('/cine/categoria_comidas/')

    return render(request, 'cine/categoria_comidaEdit.html', {'form': form})

def eliminar_categoria_comida(request, idCategoriaComida):
    categoria_comida = get_object_or_404(CategoriaComida, idCategoriaComida=idCategoriaComida)
    if request.method == 'POST':
        categoria_comida.delete()
        return redirect('/cine/categoria_comidas/')

    return render(request, 'cine/categoria_comidaDel.html', {'categoria_comida': categoria_comida})
