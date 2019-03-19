__author__="Nightwish"
__title__="寻找元素类"

from selenium.webdriver.common.by import By
from POMdemo.pages.basepages import Pages

class SearchPage(Pages):

    #百度搜索框
    search_input=(By.ID,r"kw")

    #百度一下按钮
    search_btn=(By.ID,r"su")
    def __init__(self,driver,base_url=r"https://www.baidu.com"):
        """
        类实例函数  执行基类的实例化函数
        :param driver:驱动
        :param base_url: 目标url
        """
        Pages.__init__(driver,base_url)

    def gotoBaidu(self):
        """
        打开目标url函数
        :return:
        """
        print("打开首页:",self.base_url)
        self.driver.get(self.base_url)
    def input_search_text(self,text):
        """
        写入搜索的关键字
        :param text: 搜索内容
        :return:
        """
        print("输出搜索关键字:",text)
        self.input_text(self.search_input,text)

    def click_search_btn(self):
        """
        点击按钮
        :return:
        """
        print("点击 百度一下 按钮")
        self.click(self.search_btn)

    def quit_url(self):
        """
        关闭 网页
        :return:
        """

        print("关闭 网页")
        self.quit()
