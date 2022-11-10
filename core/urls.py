from unicodedata import name
from django.urls import path
from .views import index, base, familia

urlpatterns = [
    path('', base, name="base"),
    path('index',index, name="index"),
    path('registrar_familia', familia, name="familia")
]