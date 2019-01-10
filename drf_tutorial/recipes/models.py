from django.db import models

from model_utils.models import TimeStampedModel

# Create your models here.


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(TimeStampedModel):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey("Recipe", related_name="ingredients",
                               on_delete=models.CASCADE)
