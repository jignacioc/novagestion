from unicodedata import name
from django.urls import path
from .views import index, base

urlpatterns = [
    path('', base, name="base"),
    path('index',index, name="index"),
]