#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> base_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/10 16:23
==================================================
"""
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.hand_black import handle_black


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def parse_yaml(self, path, func_name):
        # 读取yaml，取出关键数据，用parse进行解析
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        # steps = data['goto_market']
        # 解析yaml内容
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step["content"])
        # return Market(self.driver)

        # try:
        #     if locator is None:
        #         # 如果传的元素是一个(*by是用来解包/解元组)
        #         result = self.driver.find_element(*by)
        #     else:
        #         #如果传的元素是二个，既有by，又有locator
        #         result = self.driver.find_element(by, locator)
        #     self.error_num =0
        #     return result
        # #捕获黑名单中的元素
        # except Exception as e:
        #     #超过最大查找次数
        #     if self.error_num > self.max_num:
        #         raise e
        #     self.error_num += 1
        #     #从黑名单中遍历元素，依次进行处理
        #     for black_ele in self.black_list:
        #         ele = self.driver.find_elements(*black_ele)
        #         if len(ele) > 0:
        #             ele[0].click()
        #             #处理完黑名单后，再次查找原来的元素
        #             return self.find(by, locator)
        #         #如果没有黑名单，直接抛出
        #         raise e
