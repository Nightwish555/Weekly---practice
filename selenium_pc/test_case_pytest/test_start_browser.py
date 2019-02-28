import pytest
import time,os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #显示等待 依赖库1
from selenium.webdriver.common.by import By #显示等待 依赖库2
from selenium.webdriver.support import expected_conditions as EC #核心模块 期望场景是否存在

class TestSelenium():#和unittest.TestCase

    """
    测试套件 testsuite
    setup_class() <--所有testcase执行前执行一次，负责给予self.driver对象的生命
    testcase =100个
    teardown_class()<--所有testcase执行后执行一次，负责通过kill self.driver，引发关闭当前self.driver
    创造的所有浏览器的关闭行为。
    """
    path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    temp_path = path + os.sep + "temp" + os.sep
    tools_path = path + os.sep + "tools" + os.sep

    def setup_class(self):
        try:
            self.driver = webdriver.Chrome(executable_path=r"E:\Gitproject\Project"+os.sep+"chromedriver.exe") #可执行路径
            bd_url = "https://www.baidu.com/"
            self.driver.get(bd_url)
            #self.driver.implicitly_wait(10) #隐式等待 秒  2.1  10秒 7.9秒丢掉
            #self.driver.maximize_window()
            time.sleep(2)
        except Exception as err:
            print(format(err))
        #self.driver.set_window_size(600, 800)

    def teardown_class(self):
        self.driver.quit()

    # def test_open(self):
    #     print("implicitly_wait" in dir(self.driver))
    #     self.driver.get("https://testerhome.com/")
    #     print("在testerhome的区域内")
    #     time.sleep(2)
    #
    # def test_check_url(self):
    #     try:
    #         self.driver.back() #后退
    #         input_element = self.driver.find_element_by_id("kw")
    #         assert input_element == True
    #         assert "百度一下，你就知道" ==self.driver.title
    #         self.driver.forward() #前进
    #     except AssertionError as err:
    #         print(err)
    # #
    # def test_check_webinfo(self):
    #     """
    #     检查这个url的信息
    #     :return:
    #     """
    #     try:
    #         self.driver.get("https://testerhome.com/topics/18151")
    #         time.sleep(1)
    #         assert "https://testerhome.com/topics/18151" ==self.driver.current_url
    #         assert "18151" in self.driver.current_url #当前
    #         #print(self.driver.page_source)
    #         assert "演练内容（二）" in self.driver.page_source
    #         b_element =self.driver.find_element_by_class_name("reply-buttons")
    #         assert b_element ==True
    #     except AssertionError as err:
    #         print(err)
    #
    # def test_id1(self):
    #     self.driver.get("https://www.baidu.com/")
    #     input_element =self.driver.find_element_by_css_selector("#kw")
    #     input_element.send_keys("testerhome")
    #     time.sleep(1)
    #     self.driver.find_element_by_id("su").submit()
    #     time.sleep(5)

    # def test_id1(self):
    #     #self.driver.get("https://www.baidu.com/")
    #     input_element =self.driver.find_element_by_css_selector("#kw")
    #     input_element.send_keys("testerhome")
    #     time.sleep(1)
    #     sub_ele =self.driver.find_element_by_id("su")
    #     safe_ele =self.driver.find_element_by_id("jgwab")
    #     assert safe_ele == True
    #     print("\n",sub_ele.size,"\n")
    #     print(sub_ele.size.get("height")==34)
    #     assert isinstance(sub_ele.size,dict) ==True
    #     time.sleep(5)

    def test_check_text(self):
        self.driver.get("https://testerhome.com/topics/18151")
        #txt_ele =self.driver.find_element_by_css_selector('#main-nav-menu > ul > li:nth-child(2) > a')
        txt_ele =WebDriverWait(self.driver,timeout=10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR,"#main-nav-menu > ul > li:nth-child(2) > a")))
        assert txt_ele.is_enabled() ==True
        print("===>",txt_ele.is_selected())
        assert "Bug" in txt_ele.text
        print("查询文本",txt_ele.text)

    # def test_link(self):
    #     """
    #     定位器链接，判断对象是同一个
    #     :return:
    #     """
    #     ele1 = self.driver.find_element_by_partial_link_text("贴")
    #     ele2 = self.driver.find_element_by_link_text("贴吧")
    #     time.sleep(5)
    #     print(id(ele1), id(ele2))
    #     assert ele1 == ele2
        # 业务替换成新闻 结合上面的。

    # def test_handle(self):
    #     print("wins句柄",self.driver.window_handles)
    #     self.driver.get("http://news.baidu.com/")
    #     self.driver.back() #后退
    #     time.sleep(5)
    #     self.driver.forward() #前进
    #     assert "https://www.baidu.com/" == self.driver.current_url()