#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> edit_contact_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/5 15:59
@Desc   ：
==================================================
"""
from appium_wework.page.base_page import BasePage


# from appium_wework.page.search_page import SearchPage


class EditContactPage(BasePage):

    def edit_contact(self):
        from appium.webdriver.common.mobileby import MobileBy
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'删除成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        from appium_wework.page.search_page import SearchPage
        return SearchPage(self.driver)
