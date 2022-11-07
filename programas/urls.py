from unicodedata import name
from django.urls import path
from .views import programas, publicar_programas

urlpatterns = [
    path('programas',programas, name="programas"),
    path('publicar_programas', publicar_programas, name="publicar_programas"),
]