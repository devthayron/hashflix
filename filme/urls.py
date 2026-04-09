from django.urls import path
from .views import homepage,homefilmes

urlpatterns = [
    path('', homepage),
    path('filmes/',homefilmes)
]
