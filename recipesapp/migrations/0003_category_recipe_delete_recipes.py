# Generated by Django 4.0.4 on 2022-05-20 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0002_rename_recepies_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_text', models.TextField(max_length=2000)),
                ('recipe_ingredients', models.TextField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipesapp.userprofile')),
                ('recipe_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipesapp.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
