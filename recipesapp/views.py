from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from . forms import *
from django.db.models import Q


def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'categories': categories ,'recipes': recipes})


def category(request, pk):
    category = Category.objects.get(pk=pk)
    category_recipes = category.recipe_set.all()
    return render(request, 'home.html', {'category': category, 'category_recipes': category_recipes})


def recipe_details(request, pk):
    recipe_details = Recipe.objects.get(pk=pk)
    return render(request, 'home.html', {'recipe_details': recipe_details})


def my_recipes(request):
    my_recipes = Recipe.objects.all()
    return render(request, 'home.html', {'my_recipes': my_recipes})


def search(request):
	if request.method == 'GET':
		q = request.GET.get('q')
	else:
		return ''
	searched = Recipe.objects.filter(
		Q(recipe_name__icontains=q) | Q(recipe_text__icontains=q) | Q(recipe_ingredients__icontains=q))
	context = {'searched': searched, 'q': q}
	return render(request, 'search.html', context)


@login_required(login_url='login')
def create_recipe(request):
    create_recipe_form = RecipeForm()
    if request.method == 'POST':
        create_recipe_form = RecipeForm(request.POST, request.FILES)
        if create_recipe_form.is_valid():
            recipe = create_recipe_form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            return redirect('home')
    return render(request, 'home.html', {'create_recipe_form': create_recipe_form})


@login_required(login_url='login')
def addLike(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    isDislike = False
    for dislike in recipe.dislikes.all():
        if dislike == request.user:
            isDislike = True
            break
    if isDislike:
        recipe.dislikes.remove(request.user)
    isLike = False
    for like in recipe.likes.all():
        if like == request.user:
            isLike = True
    if not isLike:
        recipe.likes.add(request.user)
    if isLike:
        recipe.likes.remove(request.user)
    return redirect('recipe_details', pk=recipe.pk)


@login_required(login_url='login')
def addDislike(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    isLike = False
    for like in recipe.likes.all():
        if like == request.user:
            isLike = True
            break
    if isLike:
        recipe.likes.remove(request.user)
    isDislike = False
    for dislike in recipe.dislikes.all():
        if dislike == request.user:
            isDislike = True
            break
    if not isDislike:
        recipe.dislikes.add(request.user)
    if isDislike:
        recipe.dislikes.remove(request.user)
    return redirect('recipe_details', pk=recipe.pk)