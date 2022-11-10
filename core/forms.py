from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Familia

class RegistrarFamilia(ModelForm):
    class Meta:
        model = Familia
        fields = ["rutJefeFamilia", "numIntegrantes", "direccion", "antecedentes"] 
