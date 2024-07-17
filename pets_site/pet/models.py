"""
Содержит модели объектов:

- Питомец;
- Вид питомца;
- ...
"""
from django.conf import settings
from django.db import models
from user.models import User


class Type(models.Model):
    """Модель вида питомца."""

    name = models.CharField(
        verbose_name='Имя',
        max_length=settings.LIMIT_CHAR_200
    )
    slug = models.SlugField(
        unique=True,
        max_length=settings.LIMIT_CHAR_200
    )

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'
        default_related_name = 'Types'

    def __str__(self):
        return f'{self.name}'


class Pet(models.Model):
    """Модель питомца."""

    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name='pets'
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=settings.LIMIT_CHAR_200
    )
    type = models.ForeignKey(
        Type,
        verbose_name="Тип",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='pets/',
        blank=True
    )

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
        default_related_name = 'Pets'

    def __str__(self):
        return f'{self.name}'
