import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(1, 1) == 2

    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division(self):
        assert self.calc.division(30, 2) == 15
    def test_subtraction(self):
        assert self.calc.subtraction(10, 2) == 8

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print("Выполнение метода Teardown")
