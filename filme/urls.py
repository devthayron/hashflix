from django.urls import path
from .views import HomePageView,FilmeListView,FilmeDetailView

app_name = 'filmes'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('filmes/', FilmeListView.as_view(), name='list'),
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='detail')

]
