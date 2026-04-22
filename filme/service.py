from .models import Filme
from django.db.models import F

def get_filmes_relacionados(filme, limite=8):

    filmes_relacionados = Filme.objects.filter(
        categoria=filme.categoria
    ).exclude(id=filme.id)[:limite]

    return filmes_relacionados

def get_lista_filmes_recentes(limite=8):
    return Filme.objects.order_by('-data_criacao')[:limite]

def get_lista_filmes_em_alta(limite=8):
    return Filme.objects.order_by('-visualizacoes')[:limite]

# F → executa a operação no banco (UPDATE direto)
# evita race condition (duas requisições sobrescrevendo o mesmo valor)
def incrementar_visualizacoes(filme):
    return Filme.objects.filter(id=filme.id).update(visualizacoes=F('visualizacoes') + 1)