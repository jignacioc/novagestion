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

class PostularPrograma(models.Model):
    id_postulacion = models.AutoField(primary_key=True)
    id = models.ForeignKey(Programa, on_delete=models.CASCADE, verbose_name="ID del programa: ", null=True, blank=True)
    nombreAlumno = models.CharField(max_length=70, verbose_name="Nombre del alumno: ")
    emailAlumno = models.EmailField(max_length=70, verbose_name="Email del alumno: ")
    motivoPostulacion = models.CharField(max_length=70, verbose_name="Motivo de la postulación: ")
    def __str__(self):
        return self.nombreAlumno