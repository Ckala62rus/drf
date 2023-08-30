from django.db import models

from .movie import Movie
from .rating_star import RaitingStar


class Raiting(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адресс", max_length=15)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"