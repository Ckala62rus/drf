# Generated by Django 4.2.3 on 2023-08-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм'},
        ),
        migrations.AlterModelOptions(
            name='movieshots',
            options={'verbose_name': 'Кадр из фильма'},
        ),
        migrations.AlterModelOptions(
            name='raiting',
            options={'verbose_name': 'Рейтинг'},
        ),
        migrations.AlterModelOptions(
            name='raitingstar',
            options={'verbose_name': 'Звезда рейтинга'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв'},
        ),
    ]
