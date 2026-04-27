from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name','is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('Histórico', {
            'fields': ('filmes_vistos',)
        }),
    )