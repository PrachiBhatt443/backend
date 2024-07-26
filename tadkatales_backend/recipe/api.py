from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from .models import Recipe
from .serializers import RecipeListSerializer, RecipeDetailSerializer
from .forms import RecipeForm
from useraccount.models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def recipes_list(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = User.objects.get(pk=user_id)
    except Exception as e:
        user = None

    
    favorites = []
    recipes = Recipe.objects.all()
    
    ingredients = request.GET.getlist('ingredients', [])
    cuisine = request.GET.get('cuisine', '')
    meal_type = request.GET.get('mealType', '')
    difficulty = request.GET.get('difficulty', '')
    category = request.GET.get('category', '')
    author_id = request.GET.get('author_id', '')
    is_favorites = request.GET.get('is_favorites', '')

    if category:
        recipes = recipes.filter(category=category)

    if ingredients:
        for ingredient in ingredients:
            recipes = recipes.filter(description__icontains=ingredient)

    if cuisine:
        recipes = recipes.filter(category__icontains=cuisine)

    if meal_type:
        recipes = recipes.filter(category__icontains=meal_type)

    if difficulty:
        recipes = recipes.filter(category__icontains=difficulty)


    if author_id:
        recipes = recipes.filter(author_id=author_id)

    if is_favorites:
        recipes = recipes.filter(favorited__in=[user])

    if user:
        for recipe in recipes:
            if user in recipe.favorited.all():
                favorites.append(recipe.id)

    serializer = RecipeListSerializer(recipes, many=True)

    return JsonResponse({
        'data': serializer.data,
        'favorites': favorites
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)

    serializer = RecipeDetailSerializer(recipe, many=False)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def create_recipe(request):
    form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)


@api_view(['POST'])
def toggle_favorite_recipe(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)

    if request.user in recipe.favorited.all():
        recipe.favorited.remove(request.user)
        is_favorite = False
    else:
        recipe.favorited.add(request.user)
        is_favorite = True

    return JsonResponse({'is_favorite': is_favorite})

