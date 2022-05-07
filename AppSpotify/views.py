from re import template
from django.http import HttpResponse
from django.shortcuts import render
from AppSpotify.forms import PerfilFormulario
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #vistas basadas en clases
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppSpotify.models import Contenido, Favoritos, Perfil

## LOGIN ##

def login_request(request):
    if request.method == "POST": # al "iniciar sesion"
        form = AuthenticationForm(request, data = request.POST) #ller la data del form

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            user=authenticate(username=usuario , password=contra)

            if user:
                login(request, user) #hacemos el login
                #mostramos la pagina de inicio con un msj
                return render(request, "AppSpotify/inicio.html", {'mensaje':f"Bienvenido{user}"})
        
        else:
            return render(request, "AppSpotify/login.html",{"error":"Error, datos incorrectos", "input":"<button> HOLA </button>"})
    
    else:
        form = AuthenticationForm() # mostrar el fomulario
    
    return render(request, "AppSpotify/login.html", {"form":form })

## fin login ##

## registro ##

def register (request):

    if request.method == "POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()

            return render(request, "AppSpotify/login.html", {"creado":"Usuario Creado"})
    
    else:
        form = UserCreationForm()

    return render(request, "AppSpotify/registro.html", {"form":form})


## INICIO
@login_required
def inicio(request):
    return render(request, "AppSpotify/inicio.html")
## FIN INICIO


## views de la app ## 

@login_required
def perfil(request):
    if request.method == 'POST':
        perfil = Perfil(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
        dni=request.POST['dni'], fechaDeNacimiento=request.POST['fechaDeNacimiento'],
        relacion=request.POST['relacion'], generosFavoritos=request.POST['generosFavoritos'])
        perfil.save()

        return render(request, "AppSpotify/perfil.html")
    return render(request, "AppSpotify/perfil.html")

@login_required
def contenido(request):
    if request.method == 'POST':
        contenido = Contenido(nombre=request.POST['nombre'], artista=request.POST['artista'],
        tipo=request.POST['tipo'])
        contenido.save()

        return render(request, "AppSpotify/contenido.html")
    return render(request, "AppSpotify/contenido.html")

@login_required
def favoritos(request):
    if request.method == 'POST':
        favorito = Favoritos(nombre=request.POST['nombre'], artista=request.POST['artista'],
        album=request.POST['album'])
        favorito.save()

        return render(request, "AppSpotify/favoritos.html")
    return render(request, "AppSpotify/favoritos.html")

@login_required
def biblioteca(request):
    return render(request, "AppSpotify/biblioteca.html")

@login_required
def buscar(request):
    if request.GET.get('dni'):
        dni = request.GET.get('dni')
        perfiles = Perfil.objects.filter(dni__iexact=dni)

        return render(request,"AppSpotify/resultadoBusqueda.html", {"perfiles":perfiles, "dni":dni})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

@login_required
def buscarTodos(request):
    
    perfiles = Perfil.objects.all()
    contexto={"perfiles":perfiles}

    return render(request,"AppSpotify/traerPerfiles.html", contexto)

@login_required   
def borrarPerfil(request, dni): #dni_perfil viene por parametro en el metodo DELETE
    dni = dni
    perfil= Perfil.objects.filter(dni__iexact=dni)
    perfil.delete()

    perfiles = Perfil.objects.all()
    contexto={"perfiles":perfiles}

    return render(request,"AppSpotify/traerPerfiles.html", contexto)

@login_required
def editarPerfil(request, dni):
    dni = dni
    perfil= Perfil.objects.get(dni__iexact=dni)

    if request.method == "POST":

        miFormulario = PerfilFormulario(request.POST) # llega la data

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            perfil.nombre=informacion['nombre']
            perfil.apellido=informacion["apellido"]
            perfil.dni=informacion["dni"]
            perfil.fechaDeNacimiento=informacion["fechaDeNacimiento"]
            perfil.relacion=informacion["relacion"]
            perfil.generosFavoritos=informacion["generosFavoritos"]

            perfil.save()

            return render(request, "AppSpotify/biblioteca.html")
    #else
    else:
        miFormulario=PerfilFormulario(initial={"nombre":perfil.nombre,"apellido":perfil.apellido, 
        "dni":perfil.dni,"fechaDeNacimiento":perfil.fechaDeNacimiento,"relacion":perfil.relacion,
        "generosFavoritos":perfil.generosFavoritos})
    
    return render(request, "AppSpotify/editarPerfil.html", {"miFormulario":miFormulario, "perfil":perfil})

## Contenidos ##

@login_required
def misContenidos(request):
    return render(request, "AppSpotify/misContenidos.html")

class ContenidoList(LoginRequiredMixin, ListView):
    model=Contenido
    template_name="AppSpotify/traerContenidos.html"

class ContenidoDelete(LoginRequiredMixin, DeleteView):
    model = Contenido
    success_url = "/AppSpotify/contenido/lista"

class ContenidoUpdate(LoginRequiredMixin, UpdateView):
    model = Contenido
    success_url = "/AppSpotify/contenido/lista"
    fields= ["nombre","artista","tipo"]

## FAVORITOS ##

@login_required
def misFavoritos(request):
    return render(request, "AppSpotify/misFavoritos.html")

class FavoritosList(LoginRequiredMixin, ListView):
    model=Favoritos
    template_name="AppSpotify/traerFavoritos.html"

class FavoritosDelete(LoginRequiredMixin, DeleteView):
    model=Favoritos
    success_url = "/AppSpotify/favoritos/lista"

class FavoritosUpdate(LoginRequiredMixin, UpdateView):
    model=Favoritos
    success_url = "/AppSpotify/favoritos/lista"
    fields= ["nombre","artista","album"]
    
