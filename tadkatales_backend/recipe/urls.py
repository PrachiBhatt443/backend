# from django.urls import path
# from .views import recipes_list, recipe_detail, create_recipe, toggle_favorite_recipe
# from . import api
# urlpatterns = [
#     path('recipes/', recipes_list, name='recipes-list'),
#     path('recipes/<uuid:pk>/', recipe_detail, name='recipe-detail'),
#     path('recipes/create/', create_recipe, name='create-recipe'),
#     path('recipes/<uuid:pk>/favorite/', toggle_favorite_recipe, name='toggle-favorite-recipe'),
#     path('',api.recipes_list,name='api_recipes_list'),
# ]
from django.urls import path
from . import api

urlpatterns = [
    path('', api.recipes_list, name='api_recipes_list'),
    path('create/', api.create_recipe, name='api_create_recipe'),
    path('<uuid:pk>/', api.recipe_detail, name='api_recipe_detail'),
    path('<uuid:pk>/toggle_favorite/', api.toggle_favorite_recipe, name='api_toggle_favorite_recipe'),
]

