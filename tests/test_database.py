import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_database():
    return Database()


def test_available_buns(mock_database):
    buns = mock_database.available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_price() == 200


def test_available_ingredients(mock_database):
    ingredients = mock_database.available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[4].get_name() == "dinosaur"
    assert ingredients[5].get_price() == 300


def test_buns_and_ingredients_are_separate(mock_database):
    buns = mock_database.available_buns()
    ingredients = mock_database.available_ingredients()
    for bun in buns:
        assert bun.get_name() not in [ingredient.get_name() for ingredient in ingredients]
