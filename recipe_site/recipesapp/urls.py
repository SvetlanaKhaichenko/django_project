from tempfile import template

from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    RecipeCreateView,
    RecipesView,
    UpdateRecipeView,
    RecipeDetailView,
    RecipeDeleteView,
    RegisterView,
    AboutMeView,
    logout_view,
    UpdateAboutMeView,
    CategoriesView,
    CategoriesDetailView,

)


app_name='recipesapp'


urlpatterns = [
    path('', RecipesView.as_view(), name='recipesapp'),
    path('login/', LoginView.as_view(template_name='recipesapp/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('about/<int:pk>/update/', UpdateAboutMeView.as_view(), name='about_me_update'),
    path('logout/', logout_view, name='logout'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_details'),
    path('<int:pk>/update/', UpdateRecipeView.as_view(), name='recipe_update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoriesDetailView.as_view(), name='category_details'),

]
