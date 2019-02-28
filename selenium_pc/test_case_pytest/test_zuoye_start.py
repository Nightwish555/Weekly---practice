__author__="Nightwish"
__title__="zuoye"
import os,time
import pytest
from selenium import webdriver


class Test_zuoye_start():
    def setup_class(self):
        """
        #拉起函数 做通过网页驱动拉起所要打开的网页的操作 第一个执行
        :return:
        """
        self.driver=webdriver.Chrome(executable_path=r"G:\selenium pc\driver"+os.sep+"chromedriver.exe")
        des_url="https://www.uwa4d.com/"
        self.driver.get(des_url)
        self.driver.implicitly_wait(5)  #隐式等待
        pass
    def teardown_class(self):
        """
        关闭驱动来关掉网页 最后执行
        :return:
        """
        self.driver.quit()

    def test_shouy(self):
        """
        检索 首页按钮
        :return:
        """
        shouye_ele=self.driver.find_element_by_link_text("首页")
        if shouye_ele:
            class_ele = shouye_ele.get_attribute("class")
            assert "active" in class_ele

    def test_gongn(self):
        """
        检索 功能按钮
        :return:
        """
        gongn_ele=self.driver.find_element_by_link_text("功能")
        if gongn_ele:
            href_ele = gongn_ele.get_attribute("href")
            assert "javascript:void(0);" in href_ele

    def test_wend(self):
        """
        检索 问答按钮
        :return:
        """
        wend_ele = self.driver.find_element_by_link_text("问答")
        if wend_ele:
            href_ele = wend_ele.get_attribute("href")
            assert "https://answer.uwa4d.com" in href_ele

    def test_kaiyuank(self):
        """
        检索 开源库按钮
        :return:
        """
        kaiyuank_ele = self.driver.find_element_by_link_text("开源库")
        if kaiyuank_ele:
            href_ele = kaiyuank_ele.get_attribute("href")
            assert "https://lab.uwa4d.com" in href_ele

    def test_boik(self):
        """
        检索 博客按钮
        :return:
        """
        boike_ele = self.driver.find_element_by_link_text("博客")
        if boike_ele:
            href_ele = boike_ele.get_attribute("href")
            assert "https://blog.uwa4d.com" in href_ele
    def test_jiag(self):
        """
        检索 价格按钮
        :return:
        """
        jiage_ele=self.driver.find_element_by_link_text("价格")
        if jiage_ele:
            href_ele=jiage_ele.get_attribute("href")
            assert "price" in href_ele
    def test_hez(self):
        """
        检索 合作按钮
        :return:
        """
        hezuo_ele=self.driver.find_element_by_link_text("合作")
        if hezuo_ele:
            href_ele=hezuo_ele.get_attribute("href")
            assert "activity-us" in href_ele
    def test_xiaz(self):
        """
        检索 下载按钮 定位后 点击 选中 Android按钮点击
        :return:
        """
        xiazai_ele=self.driver.find_element_by_link_text("下载")
        if xiazai_ele:
            href_ele=xiazai_ele.get_attribute("href")
            assert "download" in href_ele
            xiazai_ele.click()
            android_down=self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div/div[3]/div[1]/div[2]/div[1]/a[1]')
            android_down.click()
            time.sleep(5)






