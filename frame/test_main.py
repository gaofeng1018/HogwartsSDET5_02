#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> test_main
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/9 15:16
@Desc   ：
==================================================
"""
from frame.main import Main


class TestMain:
    def test_main(self):
        main = Main().goto_market().goto_search().search()
