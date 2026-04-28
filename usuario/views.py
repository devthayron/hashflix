from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,UpdateView
from .models import Usuario
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'usuarios/profile.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('filmes:list')


class RegisterView(FormView):
    template_name = 'usuarios/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        