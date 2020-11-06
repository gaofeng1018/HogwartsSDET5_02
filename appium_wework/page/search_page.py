#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> search_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/3 15:38
@Desc   ：
==================================================
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium_wework.page.base_page import BasePage


class SearchPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def search_contact(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//android.widget.RelativeLayout//android.widget.RelativeLayout//android.widget.LinearLayout//android.widget.RelativeLayout[1]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'搜索')]").send_keys(name)
        # 计算搜索结果条数
        contacts = self.driver.find_elements(MobileBy.XPATH,
                                             "//*[contains(@text,'张三') and @class = 'android.widget.TextView']")
        print(type(contacts))
        number = len(contacts)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='张三' and @class='android.widget.TextView']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.LinearLayout//android.widget.RelativeLayout//android.widget.LinearLayout[2]//android.widget.RelativeLayout").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'编辑成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'删除成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        sleep(2)
        # 计算删除一个联系人后的搜索条数
        update_contacts = self.driver.find_elements(MobileBy.XPATH,
                                                    "//*[contains(@text,'张三') and @class='android.widget.TextView']")
        update_number = len(update_contacts)
        result = (number - update_number)
        return result
