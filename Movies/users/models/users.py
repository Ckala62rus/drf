from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager
from common.models.mixins import DateMixin


class User(AbstractUser, DateMixin):
    telegram_id =  models.CharField(
        'Идентификатор телеграмма',
        blank=True,
        null=True,
        unique=True,
        max_length=255
    )

    # field for default authentication
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} (id:{self.pk})'
