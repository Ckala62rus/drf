# Generated by Django 4.2.3 on 2023-09-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Идентификатор телеграмма'),
        ),
    ]