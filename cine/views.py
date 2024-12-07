from django.shortcuts import render, redirect, get_object_or_404
from cine.forms import ComidaForm, CategoriaComidaForm, CineForm, CiudadForm, CategoriaForm, PeliculaForm, UserForm, CompraEntradasForm, FuncionForm
from cine.models import Comida, CategoriaComida, Cine, Ciudad, Categoria, Pelicula, Funcion, Entrada
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group

# Create your views here.
# ------------------- Funciones y entradas -----------#
def funcion_pelicula(request):
    funciones = Funcion.objects.all()
    return render(request, 'cine/funcion_pelicula.html', {'funciones': funciones})

def compra_exito(request):
    cantidad = request.session.get('cantidad', 0)
    precio = 5200 
    total = cantidad * precio

    return render(request, 'cine/compra_exito.html', {
        'cantidad': cantidad,
        'precio': precio,
        'total': total,
    })

def comprar_entradas(request, idFuncion):
    funcion = get_object_or_404(Funcion, idFuncion=idFuncion)
    
    entradas_vendidas = funcion.entradas.filter(vendida=True).count()
    entradas_disponibles = funcion.entradas_disponibles - entradas_vendidas
    
    if request.method == 'POST':
        form = CompraEntradasForm(request.POST)
        form.fields['funcion'].initial = funcion

        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']

            if cantidad > entradas_disponibles:
                form.add_error('cantidad', f'Sólo hay {entradas_disponibles} entradas disponibles para esta función.')
                return render(request, 'cine/comprar_entradas.html', {
                    'form': form,
                    'funcion': funcion,
                    'entradas_disponibles': entradas_disponibles
                })

            # Procesar la compra
            for _ in range(cantidad):
                Entrada.objects.create(
                    funcion=funcion,
                    precio=5200,
                    vendida=True
                )

            funcion.entradas_disponibles -= cantidad
            funcion.save()

            # Guardar en la sesión la cantidad de entradas compradas
            request.session['cantidad'] = cantidad

            return redirect('compra_exito')
    else:
        form = CompraEntradasForm(initial={'funcion': funcion})

    return render(request, 'cine/comprar_entradas.html', {
        'form': form,
        'funcion': funcion,
        'entradas_disponibles': entradas_disponibles
    })


@permission_required('cine.view_funcion')
def todas_funciones(request):
    query = ''
    funciones = Funcion.objects.select_related('pelicula').all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            funciones = funciones.filter(pelicula__titulo__icontains=query)

    return render(request, 'cine/funciones.html', {'funciones': funciones, 'query': query})


@permission_required('cine.view_funcion')
def todas_funciones(request):
    query = ''
    funciones = Funcion.objects.select_related('pelicula').all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            funciones = funciones.filter(pelicula__titulo__icontains=query)

    return render(request, 'cine/funciones.html', {'funciones': funciones, 'query': query})


@permission_required('cine.add_funcion')
def crear_funcion(request):
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cine/funciones/')
    else:
        form = FuncionForm()

    return render(request, 'cine/funcionAdd.html', {'form': form})

@permission_required('cine.view_funcion')
def cargar_editar_funcion(request, idFuncion):
    funcion = get_object_or_404(Funcion, idFuncion=idFuncion)
    form = FuncionForm(instance=funcion)
    return render(request, 'cine/funcionEdit.html', {'form': form, 'funcion': funcion})

@permission_required('cine.change_funcion')
def editar_funcion(request, idFuncion):
    funcion = get_object_or_404(Funcion, idFuncion=idFuncion)

    if request.method == 'POST':
        form = FuncionForm(request.POST, instance=funcion)
        if form.is_valid():
            form.save()
            return redirect('/cine/funciones/')
    else:
        form = FuncionForm(instance=funcion)

    return render(request, 'cine/funcionEdit.html', {'form': form, 'funcion': funcion})

@permission_required('cine.delete_funcion')
def eliminar_funcion(request, idFuncion):
    funcion = get_object_or_404(Funcion, idFuncion=idFuncion)
    
    if request.method == 'POST':
        funcion.delete()
        return redirect('/cine/funciones/')
    
    return render(request, 'cine/funcionDel.html', {'funcion': funcion})

# --------------------- Usuarios --------------------#
def todos_usuarios(request):
    query = ''
    usuarios = User.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            usuarios = usuarios.filter(username__icontains=query)

    return render(request, 'cine/usuarios.html', {'usuarios': usuarios, 'query': query})

@permission_required('auth.add_user')
def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            grupo_id = request.POST.get('grupo')
            if grupo_id:
                grupo = Group.objects.get(id=grupo_id)
                user.groups.add(grupo)

            return redirect('/cine/usuarios/')
    else:
        form = UserForm()

    grupos = Group.objects.all()
    return render(request, 'cine/usuarioAdd.html', {'form': form, 'grupos': grupos})

def cargar_editar_usuario(request, idUsuario):
    usuario = get_object_or_404(User, id=idUsuario)
    form = UserForm(instance=usuario)
    grupos = Group.objects.all()  # Para mostrar los grupos
    return render(request, 'cine/usuarioEdit.html', {'form': form, 'usuario': usuario, 'grupos': grupos})

@permission_required('auth.change_user')
def editar_usuario(request, idUsuario):
    usuario = get_object_or_404(User, id=idUsuario)
    grupo_usuario = usuario.groups.first()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            if form.cleaned_data.get('password'):
                usuario.set_password(form.cleaned_data['password'])
            form.save()
            grupo_id = request.POST.get('grupo')
            if grupo_id:
                usuario.groups.clear()
                grupo = Group.objects.get(id=grupo_id)
                usuario.groups.add(grupo)
            return redirect('/cine/usuarios/')
    else:
        form = UserForm(instance=usuario)
        if grupo_usuario:
            form.fields['grupo'].initial = grupo_usuario.id
    grupos = Group.objects.all()
    return render(request, 'cine/usuarioEdit.html', {'form': form, 'usuario': usuario, 'grupos': grupos})

@permission_required('auth.delete_user')
def eliminar_usuario(request, idUsuario):
    usuario = get_object_or_404(User, id=idUsuario)

    if request.method == 'POST':
        usuario.delete()
        return redirect('/cine/usuarios/')

    return render(request, 'cine/usuarioDel.html', {'usuario': usuario})



# --------------------- Paginas principales --------------------#
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'cine/index.html', {'categorias':categorias})

def peliculas_por_categoria(request, idCategoria):
    categoria = get_object_or_404(Categoria, idCategoria=idCategoria)
    peliculas = Pelicula.objects.filter(categoria=categoria)
    query = ''

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            peliculas = peliculas.filter(titulo__icontains=query)

    return render(request, 'cine/peliculas_por_categoria.html', {'categoria': categoria, 'peliculas': peliculas, 'query': query})


def cine_cards(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'cine/cinesciudades.html', {'ciudades':ciudades})

def cines_por_ciudad(request, idCiudad):
    ciudad = get_object_or_404(Ciudad, idCiudad=idCiudad)
    cines = Cine.objects.filter(ciudad=ciudad)
    query = ''

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            cines = cines.filter(nombre__icontains=query)

    return render(request, 'cine/cines_por_ciudades.html', {'ciudad': ciudad, 'cines': cines, 'query': query})


def comidas_cards(request):
    categoria_comida = CategoriaComida.objects.all()
    return render(request, 'cine/comidascategorias.html', {'categoria_comida':categoria_comida})

def comidas_por_categoria(request, idCategoriaComida):
    categoria = get_object_or_404(CategoriaComida, idCategoriaComida=idCategoriaComida)
    comidas = Comida.objects.filter(categoria=categoria)
    query = ''

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            comidas = comidas.filter(nombre__icontains=query)

    return render(request, 'cine/comidas_por_categoria.html', {'categoria': categoria, 'comidas': comidas, 'query': query})


#---------------------- COMIDAS -------------------------#
@permission_required('cine.view_comida')
def todos_comida(request):
    query = ''
    comidas = Comida.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            comidas = comidas.filter(nombre__icontains=query)

    return render(request, 'cine/comidas.html', {'comidas': comidas, 'query': query})

@permission_required('cine.add_comida')
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

@permission_required('cine.change_comida')
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

@permission_required('cine.delete_comida')
def eliminar_comida(request, idComida):
    comida = get_object_or_404(Comida, idComida=idComida)
    
    if request.method == 'POST':
        comida.delete()
        return redirect('/cine/comidas/')
    
    return render(request, 'cine/comidaDel.html', {'comida':comida})

# ---------------------- CATEGORIA ----------------------#
def todos_categoria(request):
    query = ''
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            categorias = categorias.filter(nombreCategoria__icontains=query)

    return render(request, 'cine/categorias.html', {'categorias': categorias, 'query': query})


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
    query = ''
    peliculas = Pelicula.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            peliculas = peliculas.filter(titulo__icontains=query)

    return render(request, 'cine/peliculas.html', {'peliculas': peliculas, 'query': query})


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
    query = ''
    ciudades = Ciudad.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            ciudades = ciudades.filter(nombre__icontains=query)

    return render(request, 'cine/ciudades.html', {'ciudades': ciudades, 'query': query})


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
    query = ''
    cines = Cine.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            cines = cines.filter(nombre__icontains=query)

    return render(request, 'cine/cines.html', {'cines': cines, 'query': query})


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
    query = ''
    categorias_comidas = CategoriaComida.objects.all()

    if request.method == 'POST':
        query = request.POST.get('buscar', '')
        if query:
            categorias_comidas = categorias_comidas.filter(nombreCategoriaComida__icontains=query)

    return render(request, 'cine/categoria_comidas.html', {'categorias_comidas': categorias_comidas, 'query': query})


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
