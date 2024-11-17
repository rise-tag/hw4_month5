from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.recipe.views import RecipeAPI

router = DefaultRouter()
router.register("api_recipe", RecipeAPI, basename='api-recipe')
router.register("recipe_viewsets", RecipeAPI, basename='api-recipe-viewsets')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls

from apps.recipe.views import RecipeListAPIView, RecipeCreateAPIView, \
RecipeUpdateAPIView, RecipeDeleteAPIView, RecipeRetrievAPIView

urlpatterns = [
    path("recipe_list", RecipeListAPIView.as_view(), name='list_api'),
    path("create/", RecipeCreateAPIView.as_view(), name='create_recipe'),
    path("update/<int:pk>", RecipeUpdateAPIView.as_view(), name='delete_recipe'),
    path("<int:pk>", RecipeRetrievAPIView.as_view(), name='retriev_recipe'),
    path("delete/<int:pk>", RecipeDeleteAPIView.as_view(), name='delete_recipe')
]