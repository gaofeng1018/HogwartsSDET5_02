#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> test_contact
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/2 19:01
@Desc   ：
==================================================
"""
from appium_wework.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "张三"
        gender = "男"
        phonenum = "13000000010"
        result = self.main.goto_address().click_addmember().add_member_manual().add_contact(name, gender,
                                                                                            phonenum).get_toast()
        assert result == "添加成功"

    def test_deletecontact(self):
        name = "张三"
        # gender = "男"
        # phonenum = "13000000009"
        result1 = self.main.goto_address().click_searchmember().search_contact(name)
        assert result1 == 1
