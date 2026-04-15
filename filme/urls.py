from django.urls import path
from .views import HomePageView,FilmeListView,FilmeDetailView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('filmes/',FilmeListView.as_view()),
    path('filmes/<int:pk>',FilmeDetailView.as_view())

]
