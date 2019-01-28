__author__="Nightwish"
__title__="工具类"

"""
pytest简单的工具类
2019年  以后可自行扩展
"""

import os

class Command():
    path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    stuite_path = path + os.sep + "test_case_pytest"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def jia(self):
        return self.a+self.b
    def jian(self):
        return self.a-self.b