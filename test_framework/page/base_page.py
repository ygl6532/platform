"""
File    : base_page.py
Author  : yang
Email   : sc@163.com
Software: PyCharm
Time    : 2021/6/5 14:07
"""
import logging
from time import sleep

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver: WebDriver = None

    _current_element: WebElement = None  # 代表当前element对象

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

    def find(self, *by):
        # self._driver.find_element(By.ID,'home_search')
        # 模拟器太慢,显示等待

        # self._current_element = WebDriverWait(self._driver, 10).until(
        #     EC.presence_of_element_located(*by)
        # )


        try:
            self._current_element = self._driver.find_element(*by)
        except:
            self._current_element = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located(*by)
            )
        else:
            logging.error("未找到元素")

        finally:
            return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)

        return self

    def po_run(self, po_method):
        '''
        1、读取yaml
        2、find_search
        3、find、click、send_keys

        :param po_method:
        :return:
        '''

        with open('../data_yaml/page_demo.yaml', encoding="utf-8") as file:
            import yaml
            #获取yaml对象  读取yaml
            yaml_data = yaml.safe_load(file)
            #2、find_search
            for step in yaml_data[po_method]:
                if isinstance(step,dict):
                    #id click send keys
                    for key in step.keys():
                        if key=="id":
                            locator=(By.ID,step[key])
                            self.find(locator)
                        elif key=="click":
                            self.click()
                        elif key=="send_keys":
                            self.send_keys(step[key])
                        else:
                            logging.error(f"dont know {step}")






