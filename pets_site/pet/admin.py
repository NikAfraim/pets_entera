"""
Содержит настройку админ панели для моделей:

- Type;
- Pet;
- ...
"""
from django.contrib import admin

from .models import Pet, Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Настройку админ панели для модели Type"""

    list_display = (
        "id",
        "name",
        "slug",
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """Настройку админ панели для модели Pet"""

    list_display = (
        "id",
        "name",
        "type",
        "owner",
    )
    list_filter = ('type', 'owner')
    search_fields = ('name',)
    list_editable = ('name',)
    ordering = ('name',)
