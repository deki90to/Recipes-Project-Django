from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 50, blank = False, null = True)
    lastname = models.CharField(max_length = 50, blank = False, null = True)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return f'{self.username}, {self.firstname}, {self.lastname}, {self.email}'


class Category(models.Model):
    recipe_category_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.recipe_category_name}'


class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 200, blank = False, null = True)
    recipe_text = models.TextField(max_length = 2000, blank = False, null = True)
    recipe_ingredients = models.TextField(max_length = 500, blank = False, null = True)
    recipe_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = False, null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    image = ResizedImageField(size=[640, 480], quality=100, null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f'{self.recipe_name}, {self.recipe_text}, {self.recipe_ingredients}, {self.recipe_category}, {self.owner}, {self.created}, \
         Likes {self.likes}, Dislikes {self.dislikes}'
    
    class Meta:
        ordering = ['-created'] 