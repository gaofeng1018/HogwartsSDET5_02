#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> base_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/5 14:26
@Desc   ：
==================================================
"""
# base_page.py 基类模块：主要用于初始化driver，定义find，常用的最基本的方法
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
