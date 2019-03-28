__author__="Nightwish"
__title__="Pages基类"
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import time

class Pages(object):
    """
    Page 基类 所有page都该继承该类
    """
    def __init__(self,base_url):
        """
        类实例函数
        :param base_url:目标url
        """
        self.base_url=base_url

    def isDisplayTimeOut(self, element, timeSes):
        """
        在指定时间内，轮询元素是否显示
        :param element: 元素对象
        :param timeSes: 轮询时间
        :return:
        """
        start_time = int(time.time())  # 秒级时间戳
        timeStr = int(timeSes)
        while (int(time.time()) - start_time) <= timeSes:
            if element.is_displayed():
                return True
            self.wait(500)
        return False

    def find_element(self,*loc):
        """
        寻找元素
        :param loc:
        :return:
        """
        # TimeOut=20
        # try:
        #     self.driver.implicitly_wait(TimeOut)  # 智能等待；超时设置
        #
        #     element=self.driver.find_element(*loc) #如果element没有找到，到此处会开始等待
        #     if self.isDisplayTimeOut(element, TimeOut):
        #         self.hightlight(element)  # 高亮显示
        #     else:
        #         raise ElementNotVisibleException  # 抛出异常，给except捕获
        #
        #     self.driver.implicitly_wait(0) #恢复超时设置
        #     return element
        #
        # except (NoSuchElementException, ElementNotVisibleException) as ex:
        #     self.getImage
        #     raise ex

        if ',' not in loc:
            return self.driver.find_element_by_id(loc)
        loc_id=loc.split(',')[0]
        loc_value=loc.solit(',')[1]
        if  loc_id=="i" or loc_id=="id":
            element=self.driver.find_element_by_id(loc_value)
        elif loc_id=="n" or loc_id=="name":
            element=self.driver.find_element_by_name(loc_value)
        elif loc_id=="cl" or loc_id=="class_name":
            element=self.driver.find_element_by_class_name(loc_value)
        elif loc_id=="t" or loc_id=="tag_name":
            element=self.driver.find_element_by_tag_name(loc_value)
        elif loc_id=="l" or loc_id=="link_text":
            element=self.driver.find_element_by_link_text(loc_value)
        elif loc_id=="p" or loc_id=="partial_link_text":
            element=self.driver.find_element_by_partial_link_text(loc_value)
        elif loc_id=="x" or loc_id=="xpath":
            element=self.driver.find_element_by_xpath(loc_value)
        elif loc_id=="cs" or loc_id=="css_selector":
            element=self.driver.find_element_by_css_selector(loc_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element


    def hightlight(self, element):
        """
        元素高亮显示
        :param element: 元素对象
        :return: 无
        """
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "border: 2px solid red;")

    def input_text(self,loc,text):
        """
        文本方法
        :param loc:
        :param text: 文本内容
        :return:
        """
        self.find_element(*loc).send_keys(text)



    def click(self,loc):
        """
        点击方法
        :param loc:
        :return:
        """
        self.find_element(*loc).click()

    def F5(self):
        """
        刷新网页
        :return:
        """
        return self.driver.refresh()

    def quit(self):
        """
        关闭网页
        :return:
        """
        self.driver.quit()

