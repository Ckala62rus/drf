from django.db import models


class Category(models.Model):
    """Категории"""

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    """При селекте в админке будет отображаться имя и id"""

    def __str__(self):
        return f'{self.name} ({self.id})'

    # Перед сохранением мы можем сделать что-то с моделью
    def save(self, *args, **kwargs):
        if not self.pk:
            return super(Category, self).save(*args, **kwargs)
        return super(Category, self).save(*args, **kwargs)
