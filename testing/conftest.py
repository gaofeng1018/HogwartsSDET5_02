#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pytest

from pythoncode.calculator import Calculator


# @pytest.fixture
# def conn_db():
#     print("完成数据库连接")
#     return "database"
# @pytest.fixture(scope="module")
# def login():
#     #setup操作
#     print("登录操作")
#     #yield相当于return操作
#     yield ['tom', '123456']
#     #teardown操作
#     print("登出操作")

@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")
