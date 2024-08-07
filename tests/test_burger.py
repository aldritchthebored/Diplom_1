from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Тестовая булочка", 217)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Тестовая начинка'
        mock_ingredient.price = 77
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.remove_ingredient(0)
        assert mock_ingredient_1 not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient_2, mock_ingredient_1]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 124
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 98
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 78
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        assert burger.get_price() == 424

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Тестовая булочка'
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_1.get_name.return_value = 'Тестовый соус'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_2.get_name.return_value = 'Тестовая начинка'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 424
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.get_price = mock_burger.get_price
        expected_receipt = '(==== Тестовая булочка ====)\n' \
                           '= sauce Тестовый соус =\n' \
                           '= filling Тестовая начинка =\n' \
                           '(==== Тестовая булочка ====)\n' \
                           '\nPrice: 424'
        assert burger.get_receipt() == expected_receipt


