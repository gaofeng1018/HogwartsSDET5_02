#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> app
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 16:20
@Desc   ：
==================================================
"""
from appium import webdriver

from appium_wework.page.base_page import BasePage
from appium_wework.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['noReset'] = 'true'
            desired_caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver.launch_app()
            # self.driver.start_activity(app_package=,app_activity=)

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
