from django.shortcuts import render, redirect
from multiprocessing import context
from .forms import PublicarPrograma, PostularPrograma
from .models import Programa

# Create your views here.

def programas(request):
    programa = Programa.objects.all()
    context = {'programa': programa}

    return render (request, 'core/programas.html', context)

    
def publicar_programas(request):

    form = PublicarPrograma()

    if request.method == 'POST':
        form = PublicarPrograma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/programas')
        else:
            form = PublicarPrograma()

    context2 = {'form': form}

    return render (request, 'core/publicar_programas.html', context2)

def postular_programa(request, pk):

    form = PostularPrograma()
    programa = Programa.objects.get(id = pk)

    if request.method == 'POST':
        form = PostularPrograma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
        else:
            form =  PostularPrograma()

    context = {'form': form, 'programa': programa}

    return render (request, 'core/postular_programa.html', context)
