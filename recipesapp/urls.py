from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<pk>/', views.category, name='category'),
    path('recipe-details/<pk>/', views.recipe_details, name='recipe_details'),
    path('my-recipes/', views.my_recipes, name='my_recipes'),
    path('search/', views.search, name='search'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('like/<pk>/', views.addLike, name='like'),
    path('dislike/<pk>/', views.addDislike, name='dislike'),
]