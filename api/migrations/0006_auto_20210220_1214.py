# Generated by Django 3.0.5 on 2021-02-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_merge_20210219_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='api.Genre', verbose_name='связанный жанр'),
        ),
    ]