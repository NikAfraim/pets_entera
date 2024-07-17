"""
Содержит настройку админ панели для моделей:

- User;
- ...
"""
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройку админ панели для модели User."""

    list_display = (
        "id",
        "email",
        "username",
    )
    list_filter = ('email', 'username')
    search_fields = ('username',)
    list_editable = ('username',)
    ordering = ('username',)
