from django.db import models
from django.utils.safestring import mark_safe

from common.models.mixins import DateMixin


class PostFile(DateMixin):
    """Файлы поста"""

    file = models.ImageField(upload_to="files/%Y/%m/%d", verbose_name='Файл')
    description = models.CharField(verbose_name="Описание")

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="files"
    )

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    @property
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.file))

    def __str__(self):
        return f"{self.pk} - {self.file.name}"
