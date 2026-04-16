from .models import Filme

def lista_filmes_recentes(request):

    lista_filmes = Filme.objects.order_by('-data_criacao')[:5]
    context = {
        'lista_filmes_recentes': lista_filmes,   
    }
    return context

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.order_by('-visualizacoes')[:5]
    context = {
        'lista_filmes_em_alta': lista_filmes,
    }
    return context