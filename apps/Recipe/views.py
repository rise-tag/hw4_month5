from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, \
RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from apps.recipe.models import Recipe
from apps.recipe.serializers import RecipeSerializer

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeCreateAPIView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdateAPIView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrievAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeViewSets(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer