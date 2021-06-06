"""
File    : test_login.py
Author  : yang
Email   : sc@163.com
Software: PyCharm
Time    : 2021/6/5 14:23
"""


import pytest


class TestLogin:

    def setup_class(self):
        from test_framework.page.demo_page import DemoPage
        self.demo = DemoPage()
        self.demo.start()

    def teardown(self):
        # self.demo.stop()
        # self.demo.stop()
        self.demo.stop()

    # todo: 测试数据的驱动
    @pytest.mark.parametrize("username,password", [
        ('user1', 'password1'),
        # ('user2', 'password3'),
        # ('user3', 'password3')
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的驱动
        self.demo.login(username, password)

        assert 1 == 1

    @pytest.mark.parametrize("keyword",[
        'alibaba'
        # 'baidu',
        # 'jd'
    ])
    def test_search(self,keyword):
        self.demo.search(keyword)