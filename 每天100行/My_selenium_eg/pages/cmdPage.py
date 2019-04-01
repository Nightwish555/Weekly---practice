__author__="Nightwish"
__title__="寻找元素类"

from selenium.webdriver.common.by import By
from My_selenium_eg.pages.basepages import Pages
from selenium import webdriver
from My_selenium_eg.config.setting import Setting
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from My_selenium_eg.config.element import ELEMENT
import configparser
import os,datetime

import time

set=Setting()
class MyConf(configparser.ConfigParser):
    '''
    因为configparser读取的数据会自动转换为小写字母，自己抽取出来修改configparser
    作用是不影响源码
    '''

    def __init__(self):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

conf =MyConf()

class CmdPage(Pages):

    path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    stuite_path = path + os.sep + "test_case"

    #配置文件类路径
    iniDir=set.current_path


    def __init__(self,base_url):
        """
        类实例函数  执行基类的实例化函数
        :param base_url: 目标url
        """
        super().__init__(base_url)
    def get_driver(self):
        chromedriver=self.get_ini_date("config","Driver","chrome_driver")
        print(chromedriver)
        self.driver=webdriver.Chrome(chromedriver)

    def goto_url(self):
        """
        打开目标url函数
        :return:
        """
        print("打开首页:",self.base_url)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def _search_text(self,loc,text):
        """
        写入搜索的关键字
        :param text: 搜索内容
        :return:
        """
        print("输出搜索关键字:",text)
        self.input_text(loc,text)

    def click_search_btn(self,loc):
        """
        点击按钮
        :return:
        """
        print("点击 百度一下 按钮")
        self.click(loc)



    def get_ini_date(self,inifolder,section,item):
       """
       读取配置 函数
       :param inifolder:.ini配置文件名称
       :param section:模块
       :param item:指向
       :return:
       """
       try:
           iniconf=self.iniDir+os.sep+str(inifolder)+".ini"
           print(iniconf)
           conf.read(iniconf,encoding="utf-8")
       except  Exception  as error:
           raise(error)
       return conf.get(section,item)

    def refresh(self):
        """
        刷新网页
        :return:
        """
        return self.F5()

    def get_attribute(self, locate, attribute):
        """
        获取元素属性
        :param locate:
        :param attribute:
        :return:
        """
        element=self.find_element(locate)
        return element.get_attribute(attribute)

    def quit_url(self):
        """
        关闭 网页
        :return:
        """
        print("关闭 网页")
        self.quit()

    def get_title(self):
        """
        得到网页标题的方法
        :return:
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前的网页
        :return:
        """
        return self.driver.current_url

