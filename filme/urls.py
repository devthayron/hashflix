from django.urls import path
from .views import Homepage,Homefilmes

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/',Homefilmes.as_view())
]
