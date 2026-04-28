from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView,RegisterView    

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registrar/', RegisterView.as_view(), name='register'),
    path('perfil/', ProfileView.as_view(), name='profile'),
]