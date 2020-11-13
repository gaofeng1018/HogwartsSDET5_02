#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> test_wrapper
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/11 17:03
==================================================
"""


# 装饰器
def tmp(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')

    return wrapper


def a(a1):
    print('a')
    print(a1)


@tmp
def test_a():
    a(20)
