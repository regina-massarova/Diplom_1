from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_ingredient_creation():
    sauce = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="Ketchup", price=20.0)
    assert sauce.get_type() == INGREDIENT_TYPE_SAUCE
    assert sauce.get_name() == "Ketchup"
    assert sauce.get_price() == 20.0

def test_ingredient_type_filling():
    filling = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="Cheese", price=30.0)
    assert filling.get_type() == INGREDIENT_TYPE_FILLING
    assert filling.get_name() == "Cheese"
    assert filling.get_price() == 30.0
