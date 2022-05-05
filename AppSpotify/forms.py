from django import forms

class PerfilFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni= forms.IntegerField()
    fechaDeNacimiento = forms.DateField()
    relacion = forms.CharField()
    generosFavoritos = forms.CharField()