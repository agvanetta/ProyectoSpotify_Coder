from django.urls import path
from AppSpotify import views

urlpatterns = [
    ## perfiles ##
    path('biblioteca/', views.biblioteca, name="Biblioteca"),
    path('buscar/', views.buscar),
    path('buscarTodos/', views.buscarTodos),
    path('perfil/', views.perfil, name="Perfil"),
    path('deletePerfil/<dni>', views.borrarPerfil, name="EliminarPerfil"),
    path('editarPerfil/<dni>', views.editarPerfil, name="EditarPerfil"),

    ## end perfiles ##

    ## contenido ##
    path('contenido/', views.contenido, name="Contenido"),

    ## Favoritos ##
    path('favoritos/', views.favoritos, name="Favoritos"),


    ## Inicio
    path('', views.inicio, name="Inicio"),
]