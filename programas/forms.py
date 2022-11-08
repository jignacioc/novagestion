from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Programa, PostularPrograma

class PublicarPrograma(ModelForm):
    class Meta:
        model = Programa
        fields = ["nombrePrograma", "localizacion_cel", "duracion", "nombreCEL", "vacantes"]

class PostularPrograma(ModelForm):

    id_postulacion = models.AutoField(primary_key=True)
    id = models.ForeignKey(Programa, on_delete=models.CASCADE)
    class Meta:
        model = PostularPrograma
        fields = ["nombreAlumno", "emailAlumno", "motivoPostulacion"]
