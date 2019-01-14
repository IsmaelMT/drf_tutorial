import factory

from drf_tutorial.recipes import models


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Ingredient

    name = factory.Faker("name")
    recipe = factory.SubFactory("drf_tutorial.recipes.factories.RecipeFactory")


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Recipe

    name = factory.Faker("sentence")
    description = factory.Faker("text")


    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for ingredient in extracted:
                IngredientFactory(recipe=self)
        else:
            import random
            num_ingredients = random.randrange(1,30)

            for n in range(num_ingredients):
                ingredient = IngredientFactory(recipe=self)
