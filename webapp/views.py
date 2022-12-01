from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Categoria, Publicacion
from .forms import CategoriaForm, CreateUserForm
from django.contrib.auth import login, authenticate




def bienvenida(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def eventos(request):
    return render(request, 'eventos.html')

def calendario(request):
    return render(request, 'calendario.html')

def registro2(request):
    if request.method == 'POST':
        formulario = CreateUserForm(request.POST)
        if formulario.is_valid():
            #autenticar y reedireccionar:
            username = formulario.cleaned_data['username']        
            password = formulario.cleaned_data['password']
            email = formulario.cleaned_data['email']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(to='index')
    else:
        return render(request, 'registro.html', context = {
            'form': CreateUserForm()
        })

def categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        form = CategoriaForm()
        return render(request, 'categorias.html', context= {
            'form': form, 
            'categorias': categorias
        })
    else:#SE CREA CATEGORIA
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            Categoria.objects.create(categoria=categoria)
        return redirect('categorias')

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    publicaciones = Publicacion.objects.filter(categoria=categoria)
    return render(request, 'publicaciones.html', context= {
        'categoria': categoria,
        'publicaciones': publicaciones
    })

#publicacion = Publicacion.objects.create(blablabla, user=request.user)