# Generated by Django 4.0.4 on 2022-05-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0007_alter_recipe_recipe_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
