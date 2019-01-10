from rest_framework import viewsets

from drf_tutorial.api.serializers import RecipeSerializer
from drf_tutorial.recipes import models


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
