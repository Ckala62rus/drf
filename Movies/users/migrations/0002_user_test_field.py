# Generated by Django 4.2.3 on 2023-09-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test_field',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
