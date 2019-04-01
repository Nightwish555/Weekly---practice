__author__="Nightwish"
__title__="Pages基类"
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import sys
import time,datetime

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
        try:
            webelement = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*loc))
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            # 寻找失败时自动截图至指定目录sreenshot，截图名称为调用方法名（测试用例名）+ 时间戳 + png后缀 尚未实现
            self.driver.get_screenshot_as_file(set.SCREENSHOTURL + sys._getframe(1).f_code.co_name + time.strftime(self.get_format_date()+ ".png"))



        # if ',' not in loc:
        #     return self.driver.find_element_by_id(loc)
        # loc_id=loc.split(',')[0]
        # loc_value=loc.solit(',')[1]
        # if  loc_id=="i" or loc_id=="id":
        #     element=self.driver.find_element_by_id(loc_value)
        # elif loc_id=="n" or loc_id=="name":
        #     element=self.driver.find_element_by_name(loc_value)
        # elif loc_id=="cl" or loc_id=="class_name":
        #     element=self.driver.find_element_by_class_name(loc_value)
        # elif loc_id=="t" or loc_id=="tag_name":
        #     element=self.driver.find_element_by_tag_name(loc_value)
        # elif loc_id=="l" or loc_id=="link_text":
        #     element=self.driver.find_element_by_link_text(loc_value)
        # elif loc_id=="p" or loc_id=="partial_link_text":
        #     element=self.driver.find_element_by_partial_link_text(loc_value)
        # elif loc_id=="x" or loc_id=="xpath":
        #     element=self.driver.find_element_by_xpath(loc_value)
        # elif loc_id=="cs" or loc_id=="css_selector":
        #     element=self.driver.find_element_by_css_selector(loc_value)
        # else:
        #     raise NameError("Please enter a valid type of targeting elements.")
        # return element


    def hightlight(self, element):
        """
        元素高亮显示
        :param element: 元素对象
        :return: 无
        """
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "border: 2px solid red;")

    def input_text(self,loc,text):
        """
        文本方法
        :param loc:
        :param text: 文本内容
        :return:
        """
        try:
            self.find_element(*loc).send_keys(text)
        except  (TimeoutException,NoSuchElementException) as e:
            print('Error details :%s' % (e.msg))

    def clear_search_text(self,loc,send_text):
        """
        清除当前文本，然后重新输出问题
        :param loc:
        :param send_text:
        :return:
        """

        try:
            webelement = self.find_element(*loc)
            webelement.clear()
            webelement.send_keys(send_text)
        except  (TimeoutException,NoSuchElementException) as e:
            print('Error details :%s' % (e.msg))

    def click(self,loc):
        """
        点击方法
        :param loc:
        :return:
        """
        try:
            self.find_element(*loc).click()
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :%s' % (e.msg))

    def get_format_time(self, flag=False):
        """
        根据falg布尔值切换显示时间
        :param flag: True获得年月日
        :return:
        """
        if flag:
            return time.strftime("%Y%m%d")
        else:
            return time.strftime("%H%M%S")

    def get_format_date(self):
        now=datetime.datetime.now()
        return "{0}-{1}-{2}".format(now.year,now.month,now.day)


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

    def forward(self):
        """
        网页前进操作
        :return:
        """
        self.driver.forward()
    def back(self):
        """
        网页后退操作
        :return:
        """
        self.driver.back()