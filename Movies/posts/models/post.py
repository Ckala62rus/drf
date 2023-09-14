from django.db import models

from common.models.mixins import DateMixin
from .post_file import PostFile


class Post(DateMixin):
    """Посты"""

    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=True)
    is_publish = models.BooleanField(verbose_name='Опубликованно', default=False)
    # files = models.ManyToOneRel(
    #     PostFile,
    #     on_delete=models.CASCADE,
    #     related_name='files',
    # )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.pk} - {self.title}"
