from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni= models.IntegerField()
    fechaDeNacimiento = models.DateField()
    relacion = models.CharField(max_length=40)
    generosFavoritos = models.CharField(max_length=100)

    def __str__(self):
        txt="{0}, {1}"
        return txt.format(self.nombre, self.apellido)

class Favoritos(models.Model):
    nombre = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    album = models.CharField(max_length=40)

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.nombre, self.artista)

class Contenido(models.Model):
    nombre = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.nombre, self.artista)