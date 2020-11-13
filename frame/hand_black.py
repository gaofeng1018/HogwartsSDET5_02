#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：HogwartsSEDT15 -> hand_black
@IDE    ：PyCharm
@Author ：Jeff Gao
@Date   ：2020/11/11 17:18
==================================================
"""
import allure


def handle_black(func):
    def wrapper(*args, **kwargs):
        from frame.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
            # 捕获黑名单中的元素
        except Exception as e:
            instance.driver.save_screenshot("1.png")
            with open("1.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 超过最大查找次数
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            # 从黑名单中遍历元素，依次进行处理
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单后，再次查找原来的元素
                    return wrapper(*args, **kwargs)
                # 如果没有黑名单，直接抛出
                raise e

    return wrapper
