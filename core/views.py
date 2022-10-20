from django.shortcuts import render, redirect

# Create your views here.

def base(response):
    return redirect('index')

def index(request):
    return render (request, 'core/index.html')