from django.http import HttpResponse
from django.shortcuts import render

from AppSpotify.models import Contenido, Favoritos, Perfil

# Create your views here.

def inicio(request):
    return render(request, "AppSpotify/inicio.html")

def perfil(request):
    if request.method == 'POST':
        perfil = Perfil(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
        dni=request.POST['dni'], fechaDeNacimiento=request.POST['fechaDeNacimiento'],
        relacion=request.POST['relacion'], generosFavoritos=request.POST['generosFavoritos'])
        perfil.save()

        return render(request, "AppSpotify/perfil.html")
    return render(request, "AppSpotify/perfil.html")

def contenido(request):
    if request.method == 'POST':
        contenido = Contenido(nombre=request.POST['nombre'], artista=request.POST['artista'],
        tipo=request.POST['tipo'])
        contenido.save()

        return render(request, "AppSpotify/contenido.html")
    return render(request, "AppSpotify/contenido.html")

def favoritos(request):
    if request.method == 'POST':
        favorito = Favoritos(nombre=request.POST['nombre'], artista=request.POST['artista'],
        album=request.POST['album'])
        favorito.save()

        return render(request, "AppSpotify/favoritos.html")
    return render(request, "AppSpotify/favoritos.html")

def biblioteca(request):
    return render(request, "AppSpotify/biblioteca.html")

def buscar(request):
    if request.GET.get('dni'):
        dni = request.GET.get('dni')
        perfiles = Perfil.objects.filter(dni__icontains=dni)

        return render(request,"AppSpotify/resultadoBusqueda.html", {"perfiles":perfiles, "dni":dni})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)