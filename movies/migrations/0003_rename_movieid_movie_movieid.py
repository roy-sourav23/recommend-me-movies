# Generated by Django 4.1.7 on 2023-04-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_tag_moviesrating_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movieid',
            new_name='movieId',
        ),
    ]
