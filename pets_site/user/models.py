"""
Содержит модели объектов:

- Пользователь;
- ...
"""
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователь."""

    username = models.CharField(
        verbose_name='Логин',
        max_length=settings.LIMIT_CHAR_200,
        unique=True
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=settings.LIMIT_CHAR_200
    )
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=settings.LIMIT_CHAR_200,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)
