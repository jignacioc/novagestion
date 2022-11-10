from django.db import models

# Create your models here.

class Familia(models.Model):
    rutJefeFamilia = models.CharField(max_length=9, verbose_name="Rut Jefe Familia: ")
    numIntegrantes = models.IntegerField(verbose_name="N° de integrantes: ")
    direccion = models.CharField(max_length=50 ,verbose_name="Dirección Hogar: ")
    antecedentes = models.ImageField(upload_to="media", blank=True)
    
    def __str__(self):
        return self.rutJefeFamilia
