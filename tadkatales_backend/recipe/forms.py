from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'instructions',
            'preparation_time',
            'cooking_time',
            'servings',
            'category',
            'image',
        )
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4}),
            'description': forms.Textarea(attrs={'rows': 2}),
        }
