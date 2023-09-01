from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser, models.Model):
    telegram_id =  models.CharField(
        'Идентификатор телеграмма',
        blank=True,
        unique=True,
        max_length=255
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} (id:{self.pk})'
