# Generated by Django 4.2.3 on 2023-09-04 11:21

from django.db import migrations
import users.models.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.managers.CustomUserManager()),
            ],
        ),
    ]
