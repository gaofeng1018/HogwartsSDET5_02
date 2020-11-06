#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> addresslist_page
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 18:39
@Desc   ：
==================================================
"""
# 通讯录页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage
from appium_wework.page.member_invite_menu_page import MemberInviteMenuPage
from appium_wework.page.search_page import SearchPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def click_addmember(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        return MemberInviteMenuPage(self.driver)

    def click_searchmember(self):
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.RelativeLayout//android.widget.RelativeLayout//android.widget.LinearLayout//android.widget.RelativeLayout[1]").click()
        sleep(1)
        return SearchPage(self.driver)
