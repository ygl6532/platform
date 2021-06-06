"""
File    : base_page.py
Author  : yang
Email   : sc@163.com
Software: PyCharm
Time    : 2021/6/5 14:07
"""

from time import sleep

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    _driver:WebDriver = None

    _current_element:WebElement = None  # 代表当前element对象

    def start(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:21503",
            "noReset": "True",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".main.view.MainActivity"
        }
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(10)
        sleep(3)
        return self



    def stop(self):
        self._driver.quit()

    def find(self, by):

        # self._driver.find_element(By.ID,'home_search')
        #模拟器太慢,显示等待

        self._current_element  = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(*by)
        )

        # self._current_element = self._driver.find_element(by)


        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self,keyword):
        self._current_element.send_keys(keyword)

        return self





