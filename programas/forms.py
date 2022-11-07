from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Programa

class PublicarPrograma(ModelForm):
    class Meta:
        model = Programa
        fields = ["nombrePrograma", "localizacion_cel", "duracion", "nombreCEL", "vacantes"]
