from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView
from .service import get_filmes_relacionados,get_lista_filmes_recentes,get_lista_filmes_em_alta,incrementar_visualizacoes

class HomePageView(TemplateView):
    template_name = 'core/homepage.html'

class FilmeListView(ListView):
    template_name = 'filmes/list.html'
    model = Filme
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_filmes_recentes'] = get_lista_filmes_recentes()
        context['lista_filmes_em_alta'] = get_lista_filmes_em_alta()
        return context

class FilmeDetailView(DetailView):

    template_name = 'filmes/detail.html'
    model = Filme       
    context_object_name = 'filme'

    def get_object(self, queryset = None):
        """
        Incrementa visualizações sempre que o filme é acessado.
        """
        filme = super().get_object(queryset)
        incrementar_visualizacoes(filme)
        return filme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme = self.object # filme atual
        
        context['filmes_relacionados'] = get_filmes_relacionados(filme)

        return context

