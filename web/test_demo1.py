#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import shelve

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://www.baidu.com")
        sleep(2)

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'eVjl3FUGKAwX2FD9xVfo7nq9ExgedID0qx0I3Ojz0gADYzgnZG9HvWNPcqszhAHD'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '01168243'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'gnn1s3GmzHY5maICtz7riUjkfDYIG13Wbbbt1yacvl7TCXHa10HxP40mPX3KbwFpCdbYbekHcPKwrCF_shx4FLb0Na_T7CLxnEgpLs8zZEZiCcgvmCswlugZsnEJdteUWL5eB7uEy9bRh-TXy52PKGMGdc0JsHGUQOcCCu6k2BZEDU9opcSHgPNyBfWNNK18rlnstxl2WDI0S0_VFxnqySjDReGA8DDfWYM2d6Jv8_8e9scaEKb0xoheNq0mCibwe0eVZjzBUZ853iQbfhnCnw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': True,
                             'value': 'ssid=s4470350840'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324963171026'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850043850836'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850043850836'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603535233, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3gtgvtj'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606095950, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1666575934, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '75461a3126cbb39ff08f9bd58fe42c2d3b5c887a4e78ca4031e34ead02c3c44c'},
            {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True,
             'value': 'o2163046706'},
            {'domain': '.qq.com', 'expiry': 1603503994, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634725751, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
                             'value': '1603101806,1603188257,1603189751'},
            {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True,
             'value': '00010000fdcb43941d5ee20cf2e16bd1e33bc5c0500e95b36058fd986fb08c77642fbd12fb15c939a1bb8468'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '8205526055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9622691'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': True, 'value': '2163046706'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '6944625664'},
            {'domain': '.qq.com', 'expiry': 1915084825, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '1_2163046706'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'ycykxRqS4P'},
            {'domain': '.qq.com', 'expiry': 1603590334, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.15599625.1603101807'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634637786, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)

    def test_shelve(self):
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'eVjl3FUGKAwX2FD9xVfo7nq9ExgedID0qx0I3Ojz0gADYzgnZG9HvWNPcqszhAHD'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
        #      'value': '01168243'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'gnn1s3GmzHY5maICtz7riUjkfDYIG13Wbbbt1yacvl7TCXHa10HxP40mPX3KbwFpCdbYbekHcPKwrCF_shx4FLb0Na_T7CLxnEgpLs8zZEZiCcgvmCswlugZsnEJdteUWL5eB7uEy9bRh-TXy52PKGMGdc0JsHGUQOcCCu6k2BZEDU9opcSHgPNyBfWNNK18rlnstxl2WDI0S0_VFxnqySjDReGA8DDfWYM2d6Jv8_8e9scaEKb0xoheNq0mCibwe0eVZjzBUZ853iQbfhnCnw'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': True,
        #                      'value': 'ssid=s4470350840'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324963171026'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850043850836'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850043850836'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603535233, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '3gtgvtj'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606095950, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 1666575934, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1737553657.1582007476'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
        #      'value': '75461a3126cbb39ff08f9bd58fe42c2d3b5c887a4e78ca4031e34ead02c3c44c'},
        #     {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True,
        #      'value': 'o2163046706'},
        #     {'domain': '.qq.com', 'expiry': 1603503994, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634725751, 'httpOnly': False,
        #                      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
        #                      'value': '1603101806,1603188257,1603189751'},
        #     {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True,
        #      'value': '00010000fdcb43941d5ee20cf2e16bd1e33bc5c0500e95b36058fd986fb08c77642fbd12fb15c939a1bb8468'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': True, 'value': '8205526055'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a9622691'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
        #      'secure': True, 'value': '2163046706'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': True, 'value': '6944625664'},
        #     {'domain': '.qq.com', 'expiry': 1915084825, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': True, 'value': '1_2163046706'},
        #     {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
        #      'value': 'ycykxRqS4P'},
        #     {'domain': '.qq.com', 'expiry': 1603590334, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.15599625.1603101807'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634637786, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': True, 'value': '0'}]

        db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            'D:\\Learning\\software\\Selenium\\docs\\contacts.xlsx')
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert filename == 'contacts.xlsx'
        sleep(3)
