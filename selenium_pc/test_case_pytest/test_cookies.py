import time,functools
from selenium import webdriver
from Conf.Setting import Setting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCookies():

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path="E:\Gitproject\Project\chromedriver.exe") #可执行路径
        bd_url = "https://www.baidu.com/"
        self.driver.get(bd_url)
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    # def screen_error(self,func):
    #     def wrapper(self, *args, **kwargs):
    #         try:
    #             func(self, *args, **kwargs)
    #         except Exception as e:
    #             self.driver.get_screenshot_as_file(Setting.Pic_path+set.timef+"error.png")
    #             print(e)
    #     return wrapper

    # def test_cookies(self):
    #     try:
    #         bd_cookies =self.driver.get_cookies()
    #         print("\n 百度cookies:", bd_cookies)
    #         assert isinstance(bd_cookies,list)
    #         assert bd_cookies[0].get('domain') == '.baidu.com'
    #         assert bd_cookies[-1].get('domain') =='www.baidu.com'
    #         print(bd_cookies[-1].get('name1')==None) #推荐用get(key)的写法
    #         print(bd_cookies[-1].get('value'))
    #         #self.driver.add_cookie({'name':'chendamao','value':'222333'})
    #         self.driver.get("https://www.taobao.com/")
    #         Tmao_cookies = self.driver.get_cookies()
    #         print("天猫的作用域",Tmao_cookies[-1].get('domain'))
    #         print("\n 天猫cookies:", Tmao_cookies)
    #         self.driver.add_cookie({'name':"chendmao","value":"BOjoQ99tIPrbDQx-V2GmuZlgudY6uU1-PZy8d6IZNGNW_YhnSiEcq34_8ZQNTQTz"})
    #         print(Tmao_cookies[-1].get('value'))
    #         add_name =self.driver.get_cookie("chendmao")
    #         print("追加的信息",add_name)
    #         self.driver.delete_all_cookies()
    #         add_name1 = self.driver.get_cookie("chendmao")
    #         print("追加的信息", add_name1)
    #     except Exception as e:
    #         self.driver.get_screenshot_as_file(Setting.Pic_path + set.timef + "error.png")
    #         print(e)


