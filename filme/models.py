from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey('Filme',related_name='episodios',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    video = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.filme.titulo} - {self.titulo}'