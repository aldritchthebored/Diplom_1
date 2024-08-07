from praktikum.bun import Bun


class TestBun:
    def test_get_correct_name(self):
        bun = Bun('Тестовая булочка', 217)
        assert bun.get_name() == 'Тестовая булочка'

    def test_get_correct_price(self):
        bun = Bun('Тестовая булочка', 217)
        assert bun.get_price() == 217
