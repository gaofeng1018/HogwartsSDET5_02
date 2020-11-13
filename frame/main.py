#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> main
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/10 16:24
==================================================
"""
from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.market import Market


class Main(BasePage):
    def goto_market(self):
        # 制造假的弹窗
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='行情']"))
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # with open("./main.yaml", encoding="utf-8") as f:
        #     data = yaml.load(f)
        # steps = data['goto_market']
        # for step in steps:
        #     if 'click' == step['action']:
        #         self.find(step['by'], step['locator']).click()
        # return Market(self.driver)
        self.parse_yaml("./main.yaml", "goto_market")
        return Market(self.driver)
