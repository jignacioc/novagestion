from django.db import models

# Create your models here.
class Programa(models.Model):
    nombrePrograma = models.CharField(max_length=30, verbose_name="Nombre del programa:")
    localizacion_cel = models.CharField(max_length=30, verbose_name="Localización del CEL:")
    duracion = models.CharField(max_length=30, verbose_name="duración del programa:")
    nombreCEL = models.CharField(max_length=30, verbose_name="Nombre del CEL:")
    vacantes = models.IntegerField(verbose_name="Número de vacantes disponibles:")
    def __str__(self):
        return self.nombrePrograma