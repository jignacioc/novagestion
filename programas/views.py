from django.shortcuts import render, redirect
from multiprocessing import context
from .forms import PublicarPrograma
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

def eliminar_programa(request):
    programa = Programa.objects.all()
    programa.delete()
    return redirect('/programas')

