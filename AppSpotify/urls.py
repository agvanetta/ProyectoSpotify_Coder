from django.urls import path
from AppSpotify import views

urlpatterns = [
    path('biblioteca/', views.biblioteca, name="Biblioteca"),
    path('buscar/', views.buscar),
    path('perfil/', views.perfil, name="Perfil"),
    path('contenido/', views.contenido, name="Contenido"),
    path('favoritos/', views.favoritos, name="Favoritos"),
    path('', views.inicio, name="Inicio"),
]