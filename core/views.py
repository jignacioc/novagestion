from django.shortcuts import render, redirect
from .forms import RegistrarFamilia
from .models import Familia

# Create your views here.

def base(response):
    return redirect('index')

def index(request):
    return render (request, 'core/index.html')

def familia(request):

    form = RegistrarFamilia

    if request.method == 'POST':
        form = RegistrarFamilia(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index')
        else:
            form = RegistrarFamilia()

    context = {"form": form}

    return render(request, 'core/registrar_familia.html', context)