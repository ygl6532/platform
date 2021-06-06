"""
File    : demo_page.py
Author  : yang
Email   : sc@163.com
Software: PyCharm
Time    : 2021/6/5 14:14
"""
from time import sleep


from selenium.webdriver.common.by import By
from test_framework.page.base_page import BasePage


class DemoPage(BasePage):
    # todo: po的驱动

    _search_button=(By.ID,'home_search')
    def login(self,username,password):
        pass




    def forget_password(self):
        pass


    def search(self,keyword):


        self.po_run("search")

        self.find(self._search_button).click()

        return self

