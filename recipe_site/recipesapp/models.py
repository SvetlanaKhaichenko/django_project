import uuid

from django.contrib.auth.models import User
from django.db import models

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)

class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=True)
    instructions = models.TextField(null=False, blank=True)
    cooking_time = models.CharField(max_length=50)
    ingredients = models.TextField(null=False, blank=False)
    date_published = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    cover = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    recipe_category = models.ManyToManyField(RecipeCategory, related_name='recipes')

    def __str__(self):
        return self.title




