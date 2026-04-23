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
      # ao comparar o resultado da atualização com 1, garantimos que o filme existia e foi atualizado corretamente
      # pois o método update retorna o número de registros afetados, que deve ser 1 para um filme específico
        return (
            self.filter(pk=filme_pk)
            .update(visualizacoes=F('visualizacoes') + 1) == 1
            )

    def filme_destaque(self):
        return self.recentes().first()
    
    
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

    objects = FilmeManager()

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey('Filme',related_name='episodios',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    video = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.filme.titulo} - {self.titulo}'