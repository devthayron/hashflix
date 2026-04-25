from django.contrib import admin 
from .models import Filme,Episodio

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','visualizacoes','data_criacao','destaque')
    list_filter = ('categoria',)
    search_fields = ('titulo',)
    ordering = ('-visualizacoes',)
    readonly_fields = ('visualizacoes',)

@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('filme','titulo')
    list_filter = ('filme',)
    search_fields = ('filme',)
