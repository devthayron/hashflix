from .models import Filme

def get_filmes_relacionados(filme, limite=5):
    """
    Retorna filmes da mesma categoria do filme informado.
    
    excluindo o próprio registro e aplicando limite de retorno.

    Utilizado como fonte de dados para a seção de recomendações na interface de detalhe do filme.
    """

    filmes_relacionados = Filme.objects.filter(
        categoria=filme.categoria
    ).exclude(id=filme.id)[:limite]

    return filmes_relacionados