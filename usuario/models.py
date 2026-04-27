from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('filme.Filme', blank=True, related_name='usuarios_vistos')