from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView

class HomePageView(TemplateView):
    template_name = 'filmes/homepage.html'

class FilmeListView(ListView):
    template_name = 'filmes/list.html'
    model = Filme
    context_object_name = 'filmes'


    # otimização para evitar consultas adicionais ao acessar os episódios de cada filme
    def get_queryset(self):
        return Filme.objects.prefetch_related('episodios')

    # função que serve para adicionar dados extras no template
    def get_context_data(self, **kwargs):
        """
        Adiciona dados extras ao contexto da view.
        manager personalizado para obter filmes em destaque, recentes e em alta.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'filmes_recentes': Filme.objects.recentes(),
            'filmes_em_alta': Filme.objects.em_alta(),
            'filme_destaque': Filme.objects.filme_destaque(),
        })

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
        Filme.objects.incrementar_visualizacoes(filme.pk)
  
        return filme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme = self.object # filme atual
        
        context.update({
            'filmes_relacionados': Filme.objects.relacionados(filme)
        })

        return context

class FilmeSearchView(ListView):
    template_name = 'filmes/search.html'
    model = Filme
    context_object_name = 'filmes'

    def get_queryset(self):
        # nome 'q' é definido no "name" do input de pesquisa
        pesquisa = self.request.GET.get('q','').strip()
        queryset = self.model.objects.all()

        if pesquisa:
            return queryset.filter(titulo__icontains=pesquisa)
        
        return queryset