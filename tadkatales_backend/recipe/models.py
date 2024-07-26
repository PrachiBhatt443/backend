import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    preparation_time = models.IntegerField()  # Time in minutes
    cooking_time = models.IntegerField()  # Time in minutes
    servings = models.IntegerField()
    category = models.CharField(max_length=255)
    favorited = models.ManyToManyField(User, related_name='favorites', blank=True)
    image = models.ImageField(upload_to='uploads/recipes', blank=True, null=True)
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    ingredients = models.JSONField(blank=True, null=True)
    cuisine = models.CharField(max_length=255, blank=True, null=True)
    meal_type = models.CharField(max_length=255, blank=True, null=True)
    difficulty = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}' if self.image else None

    def __str__(self):
        return self.title
