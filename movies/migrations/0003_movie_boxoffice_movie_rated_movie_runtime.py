# Generated by Django 4.1.7 on 2023-05-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_genre_movie_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='boxoffice',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='rated',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
