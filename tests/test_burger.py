from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import pytest

@pytest.fixture
def mock_bun():
    return Bun(name="Sesame Bun", price=50.0)

@pytest.fixture
def mock_ingredients():
    return [
        Ingredient(ingredient_type="SAUCE", name="Ketchup", price=10.0),
        Ingredient(ingredient_type="FILLING", name="Cheese", price=20.0),
    ]

def test_set_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient(mock_ingredients):
    burger = Burger()
    burger.add_ingredient(mock_ingredients[0])
    burger.add_ingredient(mock_ingredients[1])
    assert len(burger.ingredients) == 2

@pytest.mark.parametrize("index_from, index_to", [(0, 1), (1, 0)])
def test_move_ingredient(mock_ingredients, index_from, index_to):
    burger = Burger()
    burger.add_ingredient(mock_ingredients[0])
    burger.add_ingredient(mock_ingredients[1])
    burger.move_ingredient(index_from, index_to)
    assert burger.ingredients[index_to] == mock_ingredients[index_from]

def test_get_receipt(mock_bun, mock_ingredients):
    burger = Burger()
    burger.set_buns(mock_bun)
    for ingredient in mock_ingredients:
        burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert "Sesame Bun" in receipt
    assert "Ketchup" in receipt
    assert "Cheese" in receipt
