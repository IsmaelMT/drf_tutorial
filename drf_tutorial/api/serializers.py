from drf_tutorial.recipes import models
from rest_framework import serializers


class IngredientField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return data


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientField(
        required=True,
        many=True,
        queryset=models.Ingredient.objects.all()
    )

    def validate_ingredients(self, value):

        if len(value) == 0:
            raise serializers.ValidationError(
                "The ingredients list can't be empty"
            )

        return value

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients")

        recipe = models.Recipe.objects.create(**validated_data)

        for ing_name in ingredients:
            models.Ingredient.objects.create(recipe=recipe, name=ing_name)

        return recipe

    def update(self, instance, validated_data):

        ingredients = validated_data.pop("ingredients", None)

        if ingredients:
            instance.ingredients.all().delete()

            for ing_name in ingredients:
                models.Ingredient.objects.create(recipe=instance, name=ing_name)

        instance = super(RecipeSerializer, self).update(instance, validated_data)

        return instance

    class Meta:
        model = models.Recipe
        fields = ("id", "name", "description", "ingredients")
