# Generated by Django 4.1.7 on 2023-04-20 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.TextField(primary_key=True, serialize=False)),
                ('movieid', models.IntegerField(blank=True)),
                ('genre', models.TextField()),
                ('imdbId', models.IntegerField()),
                ('tmdbId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MoviesRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.FloatField()),
                ('tag', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_ratings', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
