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
    path('miscontenidos/', views.misContenidos, name="misContenidos"),

    ## Favoritos ##
    path('favoritos/', views.favoritos, name="Favoritos"),
    path('misfavoritos/', views.misFavoritos, name="misFavoritos"),
    path("favoritos/lista", views.FavoritosList.as_view(), name="favoritosList"),
    ##expresiones regulares##
    path(r'^editar/(?P<pk>\d+)$', views.FavoritosUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.FavoritosDelete.as_view(), name="Delete"),


    ## Inicio
    path('', views.inicio, name="Inicio"),
]