from rest_framework import serializers
from .models import Recipe
from useraccount.serializers import UserDetailSerializer

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'servings',
            'category',
            'image_url',
        )

class RecipeDetailSerializer(serializers.ModelSerializer):
    author= UserDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'instructions',
            'preparation_time',
            'cooking_time',
            'servings',
            'category',
            'image_url',
            'author',
            'created_at',
        )
