import pytest
import time,os
from selenium import webdriver
import requests

Debug =True
#time.sleep()
#函数和类，类一定是() ,函数遇到@property，然后这个函数并且在IDE推荐不是用methods
#函数当成变量用
class TestUWA_START(): #<---继承
    def setup_class(self): #100个任务 def test >pytest
        self.driver =webdriver.Chrome(executable_path=r"E:\Gitproject\Project"+os.sep+"chromedriver.exe") #methods
        self.driver.get("https://www.uwa4d.com/")
        self.driver.implicitly_wait(5.3)
    def teardown_class(self):
        self.driver.quit()

    #css选择器
    def test_index_html(self):
        """
        判断进入到了官网页面，元素正确
        :return:
        """
        assert "https://www.uwa4d.com" in self.driver.current_url
        link_login_ele =self.driver.find_element_by_xpath('//*[@id="header-container"]/div/div/div[2]/ul[2]/a')
        if link_login_ele:
            assert bool(link_login_ele) == True
        else:
            raise Exception("元素找不到")

    def test_html_logo(self):
        """
        判断官网页面的logo存在
        :return:
        """
        logo_ele =self.driver.find_element_by_xpath('//*[@id="header-container"]/div/div/div[1]/a/img')
        if not logo_ele:#bool(logo_ele)
            raise Exception("元素找不到")
        if Debug:time.sleep(2)
        pic_ele=logo_ele.get_attribute("src")
        if pic_ele:
            #接口调用这个pic_ele的结果看他的返回。
            if Debug: print("test_html_logo--->验证attribute",pic_ele)
            assert requests.get(pic_ele).status_code ==200
            assert ".png" in pic_ele
            if Debug:time.sleep(2)

    def test_first_page(self):
        first_page_ele =self.driver.find_element_by_link_text("首页")
        if first_page_ele:
            href_ele =first_page_ele.get_attribute("href")
            assert "index" in href_ele

    def test_get_field_func(self):
        """
        use:
        :return:
        """
        func_ele =self.driver.find_element_by_link_text("功能")
        print(type(func_ele))
        if func_ele:
            assert bool(func_ele) ==True
            return True
        else:
            return False

    def test_func_Below_field(self):
        if self.test_get_field_func():
            field1 =self.driver.find_element_by_link_text("性能诊断与优化")
            assert bool(field1) ==True
            field1.click()


