# Generated by Django 5.1.6 on 2025-02-19 18:12

import recipesapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0002_recipe_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=recipesapp.models.user_directory_path),
        ),
    ]
