from django.db import models
from django.utils import timezone
from django.db.models import F

class FilmeManager(models.Manager):
    def relacionados(self, filme, limite=8):
        return (
        self.filter(categoria=filme.categoria)
        .exclude(pk=filme.pk)
        .order_by('-data_criacao')[:limite]
        )

    def recentes(self, limite=8):
        return self.order_by('-data_criacao')[:limite]
    
    def em_alta(self, limite=8):
        return self.order_by('-visualizacoes')[:limite]
    
    def incrementar_visualizacoes(self, filme_pk):
        return (
            self.filter(pk=filme_pk)
            .update(visualizacoes=F('visualizacoes') + 1) 
            == 1    # Retorna True se exatamente 1 registro foi atualizado
            )

    def filme_destaque(self):
        return self.filter(destaque=True).order_by('-data_criacao').first()
    
    
# choices → define opções fixas para um campo
# formato: (valor_salvo_no_banco, valor_exibido_para_usuario)

LISTA_CATEGORIAS = (
    ('ANALISES','Análises'),
    ('PROGRAMACAO','Programação'),
    ('APRESENTACAO','Apresentação'),
    ('OUTROS','Outros'),
)
class Filme(models.Model):
    titulo = models.CharField(max_length=50)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField()
    categoria = models.CharField(max_length=20,choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)  # Define a data na criação e permite alteração manual depois
    destaque = models.BooleanField(default=False,help_text='Marque como destaque para exibir o destaque no homepage')

    objects = FilmeManager()

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        """
        Garantir que apenas um filme seja destaque.
        Se este filme for marcado como destaque, desmarque os outros.
        """
        if self.destaque:
            Filme.objects.exclude(pk=self.pk).update(destaque=False)

        return super().save(*args, **kwargs)


class Episodio(models.Model):
    filme = models.ForeignKey('Filme',related_name='episodios',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    video = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.filme.titulo} - {self.titulo}'