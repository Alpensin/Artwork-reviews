# Generated by Django 3.0.5 on 2021-02-19 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genres', to='api.Genre', verbose_name='связанный жанр'),
        ),
    ]