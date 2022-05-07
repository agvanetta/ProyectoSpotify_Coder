from django.urls import path
from AppSpotify import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    ## perfiles ##
    path('biblioteca/', views.biblioteca, name="Biblioteca"),
    path('buscar/', views.buscar),
    path('buscarTodos/', views.buscarTodos),
    path('perfil/', views.perfil, name="Perfil"),
    path('deletePerfil/<dni>', views.borrarPerfil, name="EliminarPerfil"),
    path('editarPerfil/<dni>', views.editarPerfil, name="EditarPerfil"),

    ## end perfiles ##

    ## Contenido ##
    path('contenido/', views.contenido, name="Contenido"),
    path('miscontenidos/', views.misContenidos, name="misContenidos"),
    path("contenido/lista", views.ContenidoList.as_view(), name="contenidosList"),
    ##expresiones regulares##
    path(r'^editar/(?P<pk>\d+)$', views.ContenidoUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.ContenidoDelete.as_view(), name="Delete"),


    ## Favoritos ##
    path('favoritos/', views.favoritos, name="Favoritos"),
    path('misfavoritos/', views.misFavoritos, name="misFavoritos"),
    path("favoritos/lista", views.FavoritosList.as_view(), name="favoritosList"),
    ##expresiones regulares##
    path(r'^editar/(?P<pk>\d+)$', views.FavoritosUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.FavoritosDelete.as_view(), name="Delete"),


    ## Inicio
    path('', views.inicio, name="Inicio"),

    #Login
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name="AppSpotify/logout.html"), name="Logout"),


]