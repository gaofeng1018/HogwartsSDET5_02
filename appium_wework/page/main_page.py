#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> main_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 16:30
@Desc   ：
==================================================
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.addresslist_page import AddressListPage
from appium_wework.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_message(self):
        # 进入消息页
        pass

    def goto_address(self):
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return AddressListPage(self.driver)
