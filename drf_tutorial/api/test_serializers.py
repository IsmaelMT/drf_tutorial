import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from drf_tutorial.recipes import factories
from drf_tutorial.api import serializers


@pytest.mark.django_db
def test_recipe_api_format():

    recipe = factories.RecipeFactory()

    recipe_data = serializers.RecipeSerializer(instance=recipe).data

    assert "name" in recipe_data.keys()
    assert type(recipe_data["name"]) == str

    assert "description" in recipe_data.keys()
    assert type(recipe_data["description"] == str)

    assert "ingredients" in recipe_data.keys()
    assert type(recipe_data["ingredients"] == list)

    assert all(ingredient for ingredient in
               recipe_data["ingredients"] if type(ingredient) == str)


@pytest.mark.django_db(transaction=True)
class TestCRUD(APITestCase):

    def setUp(self):
        self.test_recipe_1 = factories.RecipeFactory()
        self.test_recipe_2 = factories.RecipeFactory()
        self.test_recipe_3 = factories.RecipeFactory()
        self.test_recipe_4 = factories.RecipeFactory()

        self.recipes = [
            self.test_recipe_1,
            self.test_recipe_2,
            self.test_recipe_3,
            self.test_recipe_4
        ]

        self.detail_url = reverse(
            "recipe-detail", kwargs={"pk": self.test_recipe_1.id}
        )

        self.list_url = reverse("recipe-list")

        self.hostname = "http://localhost:8000"

    def test_get_recipe(self):
        response = self.client.get(self.detail_url)

        test_recipe_data = serializers.RecipeSerializer(
            instance=self.test_recipe_1).data

        assert response.status_code == status.HTTP_200_OK
        assert response.data == test_recipe_data

    def test_update_recipe(self):
        assert True
        edit_recipe = {
            "name": self.test_recipe_1.name + "-edited",
            "description": self.test_recipe_1.description + "-edited",
            "ingredients": ["test-ingredient"]
        }

        response = self.client.patch(self.detail_url, edit_recipe)
        response_data = {k: v for k, v in response.data.items() if k != "id"}

        assert response_data == edit_recipe

    def test_post_recipe(self):

        new_recipe = {
            "name": "Tortilla",
            "description": "Little tortilla boy",
            "ingredients": ["eggs", "potatoes"]
        }

        response = self.client.post(self.list_url, new_recipe)

        response_data = {k: v for k, v in response.data.items() if k != "id"}

        assert response_data == new_recipe

    def test_list_recipes(self):

        response = self.client.get(self.list_url)

        assert len(response.data) == len(self.recipes)

    def test_required_ingredients(self):
        new_recipe = {
            "name": "Tortilla",
            "description": "Little tortilla boy",
        }

        response = self.client.post(
            "{}{}".format(self.hostname, self.list_url),
            json=new_recipe
        )

        # # Assert ingredients are required
        assert response.status_code == status.HTTP_400_BAD_REQUEST
