import pytest

from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")
    #加法测试
    @pytest.mark.parametrize('a,b,expect',[
        [1, 1, 2], [100, 100, 200], [0.1, 0.3, 0.4], [-1, -1, -2], [1, 0, 1]
    ], ids = ['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    #数字+字符串
    def test_add1(self):
        # calc = Calculator()
        try:
            result = self.calc.add(1, '1')
        except TypeError as e:
            print("type error", e)

    #除法测试
    @pytest.mark.parametrize('a,b,expect', [
        [-1 - 1j, 2, -0.5 - 0.5j], [1 + 1j, 2, 0.5 + 0.5j], [-1, 2, -0.5], [0, 2, 0], [1, 2, 0.5], [2, 2, 1],
        [10, 3, 10 / 3], [10, 2, 5], [100000, 2, 50000]
    ])
    def test_div(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.div(a, b)
        assert result == expect
    #除数为0
    def test_div1(self):
        # calc = Calculator()
        try:
            result = self.calc.div(1, 0)
        except ZeroDivisionError as e:
            print("ZeroDivisionError", e)

