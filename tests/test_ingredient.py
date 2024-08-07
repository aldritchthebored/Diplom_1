import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Тестовый соус', 68)
        assert ingredient.get_name() == 'Тестовый соус'

    def test_get_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Тестовая начинка', 324)
        assert ingredient.get_price() == 324

    @pytest.mark.parametrize(
        'type, name, price, expected_type',
        [
            [INGREDIENT_TYPE_SAUCE, 'Тестовый соус', 78, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Тестовая начинка', 234, 'FILLING']
        ]
    )
    def test_get_correct_type(self, type, name, price, expected_type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_type