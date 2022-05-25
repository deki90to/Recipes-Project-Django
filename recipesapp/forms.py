from django import forms
from django.forms import ModelForm
from django.db.models import fields
from . models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['owner', 'likes', 'dislikes']
