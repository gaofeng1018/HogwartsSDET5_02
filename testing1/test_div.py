import pytest

from pythoncode.calculator import Calculator

# def test_a():
#     print("test case a")

class TestDiv:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [-1-1j, 2, -0.5-0.5j], [1+1j, 2, 0.5+0.5j], [-1, 2, -0.5], [0, 2, 0], [1, 2, 0.5], [2, 2, 1], [10, 3, 10/3],[10, 2, 5], [100000, 2, 50000]
    ])
    def test_div(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.div(a, b)
        assert result == expect

    def test_div1(self):
        # calc = Calculator()
        try:
            result = self.calc.div(1, 0)
        except ZeroDivisionError as e:
            print("ZeroDivisionError", e)