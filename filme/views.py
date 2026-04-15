from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView

class HomePageView(TemplateView):
    template_name = 'core/homepage.html'

class FilmeListView(ListView):
    template_name = 'filmes/list.html'
    model = Filme
    context_object_name = 'filmes'

class FilmeDetailView(DetailView):
    template_name = 'filmes/detail.html'
    model = Filme
    context_object_name = 'filme'