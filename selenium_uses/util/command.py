
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains,TouchActions
import os
from util.Base import Base
base = Base()

"""
pytest新版的webdriver工具类
2019年
"""

class Command():

    path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    stuite_path = path + os.sep + "test_case_pytest"

    def start_brower(self,base_url):
        chromedriver = base.get_ini_date("config", "Drivers", "chrome")
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get(base_url) #"http://www.ctrip.com/"
        self.driver.implicitly_wait(10)
        return self.driver


    def find_element_wait(self,located,timeout=12,poll=0.5):
        """
        隐式等待12秒 self.driver.定位器
        :param located:
        :param timeout:
        :param poll:
        :return:
        """
        if "=>" not in located:
            raise NameError("Positioning syntax errors")
        by =located.split("=>")[0]
        value =located.split("=>")[1]
        if by == "id" or by =="ID":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name" or by =="NAME":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class"or by =="CLASS":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text" or by=="LINK_TEXT":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath" or by=="XPATH":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css" or by=="CSS":
            element =WebDriverWait(self.driver,timeout, poll).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        return element

    def clear_element_text(self,located):
        """
        选中元素清除元素上的信息，让焦点到确保在顶头位置
        :param located:
        :return:
        """
        try:
            element =self.find_element_wait(located)
            if element.text: #如果有文本获取焦点后删除
                element.click()
                element.clear()
            else:
                element.click() #获取焦点
            return element
        except Exception as error:
            print(format(error))

    def get_element_text(self,pattern, position):
        """
        获取元素文本内容
        :param pattern: 元素定位方法， id， name等
        :param position: 定位元素的value
        :return: 
        """
        try:
            element = self.find_element_wait(pattern, position)
            # t = element.get_attribute('value')
            text = element.text
            return text
        except Exception as error:
            print(error)

    def element_send_keys(self,located, context):
        """
        定位元素后根据状态清除后send_keys(文本)
        :param located: 元素定位方法，id，name "定位器=>value"
        :param context: 要输入的内容
        :return:
        """
        try:
            element = self.clear_element_text(located)
            if element:
                element.send_keys(context)
            return element
        except Exception as error:
            print(error)

    def get_web_cookies(self):
        """
        获得cookies
        :return:
        """
        cookies =self.driver.get_cookies()
        for cookie in cookies:
            return cookie
            #['domain'],cookie['name'],cookie['value'],cookie['expiry'],cookie['path']

    def capture_screen(self,scene):
        """
        捕获截图
        :return:
        """
        try:
            screen_dir =self.path+os.sep+"ScreenShot"+os.sep
            result =self.driver.get_screenshot_as_file(screen_dir+scene)
            return result
        except IOError as error:
            print(format(error))

    def check_title(self,checkData):
        """
        检查网页title
        :param checkData:
        :return:
        """
        assert checkData in self.driver.title

    def colour_element(self,element):
        self.driver.execute_script("arguments[0].setAttribute('style',\
        arguments[1]);",element,"background:green;border:2px solid red;")


    def press_move_element(self,able_move_ele,x,y):
        """
        长按元素按需求移动位置
        :param able_move_ele:
        :param x:
        :param y:
        :return:
        """
        from selenium.webdriver import ActionChains
        self.driver.save_screenshot('before_move_element.png')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(able_move_ele,x,y).perform()
        self.driver.save_screenshot('after_move_to_element.png')
