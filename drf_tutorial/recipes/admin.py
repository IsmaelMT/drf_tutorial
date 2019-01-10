from django.contrib import admin

from drf_tutorial.recipes import models


class IngredientInline(admin.TabularInline):
    model = models.Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]


admin.site.register(models.Recipe, RecipeAdmin)
