#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> member_invite_menu_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 18:44
@Desc   ：
==================================================
"""
# 邀请页面
from appium.webdriver.common.mobileby import MobileBy

# from appium_wework.page.contactadd_page import ContactAddPage
from appium_wework.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_manual(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from appium_wework.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
