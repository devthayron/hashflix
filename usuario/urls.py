from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView,RegisterView
from django.urls import reverse_lazy 

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registrar/', RegisterView.as_view(), name='register'),
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/alterar-senha/', auth_views.PasswordChangeView.as_view(template_name='usuarios/profile.html', success_url=reverse_lazy('filmes:list')), name='change_password'),
]