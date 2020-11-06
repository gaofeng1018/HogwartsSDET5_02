#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> contactadd_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 18:46
@Desc   ：
==================================================
"""
# 编辑联系人页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from appium_wework.page.member_invite_menu_page import MemberInviteMenuPage
from appium_wework.page.base_page import BasePage


class ContactAddPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenum):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[contains(@text,'必填')]").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))

        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        from appium_wework.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
