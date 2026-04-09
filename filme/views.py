from django.shortcuts import render
from .models import Filme

def homepage(request):
    return render(request, 'homepage.html')

def homefilmes(request):
    context = {
        'lista_filmes': Filme.objects.all()
    }
    return render(request,'homefilmes.html',context)