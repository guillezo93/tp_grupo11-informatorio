from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Noticia, Categoria, Comentario
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def bienvenida(request):
    return render(request, 'index.html')


def contacto(request):
    return render(request, 'contacto.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def noticias(request):
    return render(request, 'noticias.html')


def noticia(request):
    return render(request, 'noticia.html')


def registro1(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                # guardar
                user.save()
                # autenticar
                login(request, user)
                return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Usuario creado correctamente.'})
            except:
                return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'El usuario ya existe.'})
        return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Contraseña Incorrecta'})

# otra manera de registrar clientes, pero de manera mas personalizada.


def registro2(request):
    if request.method == 'POST':
        formulario = CreateUserForm(request.POST)
        if formulario.is_valid():
            # autenticar y reedireccionar:
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            email = formulario.cleaned_data['email']
            User.objects.create_user(
                username=username, email=email, password=password)
            return redirect(to='index')
    else:
        return render(request, 'registro.html', context={
            'form': CreateUserForm()
        })


def login2(request):
    if request.method == 'GET':
        return render(request, 'logueo.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'logueo.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrectos.'})
        else:
            login(request, user)
            return redirect('index')


def logout2(request):
    logout(request)
    return redirect('index')


@login_required
def Listar_Noticias(request):
    contexto = {}

    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()  # RETORNA UNA LISTA DE OBJETOS

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'listar.html', contexto)


@login_required
def Detalle_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)  # RETORNA SOLO UN OBEJTO
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia=n)
    contexto['comentarios'] = c

    return render(request, 'detalle.html', contexto)


@login_required
def Comentar_Noticia(request):

    com = request.POST.get('comentario', None)
    usu = request.user
    noti = request.POST.get('id_noticia', None)  # OBTENGO LA PK
    noticia = Noticia.objects.get(pk=noti)  # BUSCO LA NOTICIA CON ESA PK
    coment = Comentario.objects.create(usuario=usu, noticia=noticia, texto=com)

    return redirect(reverse_lazy('detalle', kwargs={'pk': noti}))
