from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from .models import Usuario

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/profile.html'

class ProfileCreateView(TemplateView):
    template_name = 'usuarios/profile_create.html'
  