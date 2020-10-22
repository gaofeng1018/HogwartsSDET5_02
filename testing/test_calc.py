#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pytest
import yaml
import allure

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    # add_datas = datas["add"]["datas"]
    # add_ids = datas["add"]["ids"]
    # print(add_datas)
    # print(add_ids)
    return datas

@allure.feature("测试模块")
class TestCalc:
    # 加法测试
    # @allure.story("加法测试")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()["add"]["datas"], ids=get_datas()["add"]["ids"])
    def test_add(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    # @allure.story("加法测试float")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', [
        [0.1, 0.2, 0.3], [0.1, 0.1, 0.2]
    ])
    def test_add_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    # 减法测试
    # @allure.story("减法测试")
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('a,b,expect', get_datas()["sub"]["datas"], ids=get_datas()["sub"]["ids"])
    def test_sub(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.sub(a, b)
        assert result == expect

    # @allure.story("减法测试float")
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a, b, expect', [
        [0.1, 0.2, -0.1], [0.1, 0.1, 0]
    ])
    def test_sub_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    # 除法测试
    # @allure.story("除法测试")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()["div"]["datas"])
    def test_div(self, get_calc, a, b, expect):
        # result = self.calc.div(a, b)
        result = get_calc.div(a, b)
        assert result == expect

    # 除数为0
    # @allure.story("除法测试，除数为0")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b', [
        [0.1, 0], [10, 0]
    ])
    def test_div_zero(self, get_calc, a, b):
        try:
            # result = self.calc.div(a, b)
            result = get_calc.div(a, b)
        except ZeroDivisionError as e:
            print("除数为0", e)

    # 乘法测试
    # @allure.story("乘法测试")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b,expect', get_datas()["mul"]["datas"], ids=get_datas()["mul"]["ids"])
    def test_mul(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.mul(a, b)
        assert result == expect

    # @allure.story("乘法测试float")
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a, b, expect', [
        [0.1, 0.2, 0.02], [0.1, 2, 0.2]
    ])
    def test_mul_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect