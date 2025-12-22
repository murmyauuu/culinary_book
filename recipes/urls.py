# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("create/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("<int:pk>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
]
