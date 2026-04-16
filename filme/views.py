from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView
from .service import get_filmes_relacionados

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

    # função que serve para adicionar dados extras no template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme = self.object # filme atual
        
        context['filmes_relacionados'] = get_filmes_relacionados(filme)

        return context
