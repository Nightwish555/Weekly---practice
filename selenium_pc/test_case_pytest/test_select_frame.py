
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

"""
双击和下拉框
"""
#行为链(driver).行为1(元素).操作()

class TestSelect():

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path="F:\selenium_uses\driver\chromedriver.exe") #可执行路径
        bd_url = "https://www.baidu.com/"
        self.driver.get(bd_url)
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    # def action(self):
    #     btn_ele = WebDriverWait(self.driver, timeout=10).until \
    #         (EC.presence_of_element_located((By.ID, "su")))
    #     action_btn = ActionChains(self.driver)
    #     action_btn.double_click(btn_ele).perform()  # 执行
    #     time.sleep(2)
    #
    #
    # def test_double_click(self):
    #     self.action()

    def test_setting(self):
        mouse = self.driver.find_element_by_link_text("设置")
        ActionChains(self.driver).move_to_element(mouse).perform()
        time.sleep(1)
        self.driver.find_element_by_link_text("搜索设置").click()
        time.sleep(2)
        select_ele = self.driver.find_element_by_id("nr")
        info_ele =self.driver.find_element_by_css_selector('#nr > option:nth-child(1)')
        Select(select_ele).select_by_visible_text("每页显示20条")
        time.sleep(2)
        Select(select_ele).select_by_value("50")
        time.sleep(2)
        btn_ele =self.driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]')
        ActionChains(self.driver).double_click(btn_ele).perform()
        time.sleep(2)
        alert = self.driver.switch_to.alert #处理弹框
        alert.accept()
        time.sleep(2)

    def test_move_point(self):
        flag =True
        while flag:
            self.driver.get("https://passport.ctrip.com/user/login")
            #'//*[@id="sliderddnormal"]/div[1]/div[2]'
            exists_ele =self.driver.find_element_by_xpath('//*[@id="sliderddnormal"]/div[1]/div[2]')
            if exists_ele:
                print("=====>")
                #able_move_ele =self.driver.find_element_by_xpath('//*[@id="sliderddnormal"]/div[1]/div[2]/div/i[1]')
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(exists_ele,300,0).perform()
                time.sleep(5)
                break
            else:
                self.test_move_point()
