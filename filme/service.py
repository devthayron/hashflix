from .models import Filme

def get_filmes_relacionados(filme, limite=5):

    filmes_relacionados = Filme.objects.filter(
        categoria=filme.categoria
    ).exclude(id=filme.id)[:limite]

    return filmes_relacionados


def get_lista_filmes_recentes(limite=5):
    return Filme.objects.order_by('-data_criacao')[:limite]

def get_lista_filmes_em_alta(limite=5):
    return Filme.objects.order_by('visualizacoes')[:limite]