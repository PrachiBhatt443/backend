from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# from useraccount.models import User
from recipe.models import Recipe
from .serializers import UserDetailSerializer
from recipe.serializers import RecipeListSerializer
from rest_framework import status
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
# from .serializers import UserDetailSerializer
from .models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_recipes(request):
    user = request.user
    recipes = Recipe.objects.filter(author=user)
    serializer = RecipeListSerializer(recipes, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)