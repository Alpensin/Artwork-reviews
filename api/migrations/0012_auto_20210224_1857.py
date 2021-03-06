# Generated by Django 3.0.5 on 2021-02-24 15:57

import api.validators.title_validator
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210223_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date'], 'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='оценка не может быть меньше 1'), django.core.validators.MaxValueValidator(10, message='оценка не может быть больше 10')], verbose_name='оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.SmallIntegerField(blank=True, null=True, validators=[api.validators.title_validator.year_validator], verbose_name='год'),
        ),
    ]
