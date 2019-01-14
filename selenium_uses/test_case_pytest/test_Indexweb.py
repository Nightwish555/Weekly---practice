
import pytest
import sys,time,openpyxl
from util.command import Command
from util.Base import Base
from config.setting import Setting as set #文件路径类

from selenium import webdriver

cmd =Command()
base =Base()


class TestIndexWeb():

    """
    pageobject 首个页面
    """
    flag = 3
    base_url ="http://www.ctrip.com/"

    def setup_class(self):
        try:
            self.driver = cmd.start_brower(self.base_url)

        except Exception as err:
            print(format(err))

    def teardown_class(self):
        if set.debug:print("END"*3)
        self.driver.quit()

    def test_step_start(self,msg=base.read_dict_data(1,6)):
        """
        检查 "携程旅行网官网" in self.driver.title
        :param msg:
        :return:
        """
        try:
            wb = openpyxl.load_workbook(set._xlsx_path)
            ws =wb[wb.sheetnames[0]]
            ws["E2"] =base.load_time()
            start = time.clock()
            cmd.check_title(base.read_dict_data(1,3))
            ws["F2"] = base.response_ms(start)
            ws["H2"] =msg[-4:]
        except Exception as err:
            msg =msg.replace("pass","fail")
            ws["H2"] = msg[-4:]
            print(msg,err)
        finally:
            wb.save(set._xlsx_path)
            wb.close()

    # def flaginfo(self):#反射修改
    #     if hasattr(TestIndexWeb,"flag"):
    #         setattr(TestIndexWeb,"flag",4)
    #     return self.flag
    #
    # def test_flag(self):
    #     self.flaginfo()
    #     print("flag=",self.flaginfo())

    #条件满足就不跳过
    @pytest.mark.skipif(flag>5,reason=base.read_dict_data(1,6))
    def test_step_check(self,msg=base.read_dict_data(2,6)):
        try:
            wb = openpyxl.load_workbook(set._xlsx_path)
            ws = wb[wb.sheetnames[0]]
            ws["E3"] = base.load_time()
            start = time.clock()
            if set.debug:print("解析cookies里面的domain",cmd.get_web_cookies()['domain'])
            assert cmd.get_web_cookies()['domain'] == "www.ctrip.com"
            ws["F3"] = base.response_ms(start)
            ws["H3"] = msg[-4:]
            #assert cmd.get_web_cookies()['value'] == "/" #存下来对象
        except Exception as err:
            msg =msg.replace("pass","fail")
            ws["H3"] = msg[-4:]
            print(msg,err)
        finally:
            wb.save(set._xlsx_path)
            wb.close()

    #预设条件，函数返回在xfail的第一个区域里
    @pytest.mark.xfail(sys.version_info<=(3,3),reason="当前页面信息不相符") #实际上肯定是大于的
    def test_index_checkInfo(self,msg=base.read_dict_data(3,6)):
        """
        验证当前网页是否和目标一致
        :param msg:
        :return:
        """
        client = self.driver
        try:
            wb = openpyxl.load_workbook(set._xlsx_path)
            ws = wb[wb.sheetnames[0]]
            ws["E4"] = base.load_time()
            start = time.clock()
            if set.debug:print("当前网页",client.current_url)
            assert self.base_url ==client.current_url #self.base_url用的类变量没用数据驱动
            ws["F4"] = base.response_ms(start)
            ws["H4"] = msg[-4:]
        except Exception as err:
            msg =msg.replace("pass","fail")
            ws["H4"] = msg[-4:]
            print(msg,err)
        finally:
            wb.save(set._xlsx_path)
            wb.close()


    # def test_index_checklogin(self):
    #     """
    #     主页上找到登录按钮的元素
    #     :return:
    #     """
    #     elelogin = cmd.find_element_wait('css=>#c_ph_login')
    #     cmd.colour_element(elelogin)#带颜色的
    #     time.sleep(5)
    #     if elelogin: #有信息返回就是
    #         assert "登录" == elelogin.text
    #
    # def test_login_step1(self):
    #     """
    #     主页切换到登陆页面
    #     :return:
    #     """
    #     elelogin = cmd.find_element_wait('css=>#c_ph_login')
    #     if elelogin:
    #         elelogin.click()
    #         time.sleep(1)
    #         assert "passport.ctrip.com/user/login" in self.driver.current_url
    #         assert "登录首页" in self.driver.title
    #         print("切换到登录页面成功")
    #         assert cmd.get_web_cookies()['httpOnly'] ==False
    # #
    # def test_login_step2(self):
    #     """
    #     检查登录页面元素
    #     :return:
    #     """
    #     login_title =cmd.find_element_wait('xpath=>//*[@id="logintitle"]')
    #     print(login_title.text)
    #     assert "携程账号登录" in login_title.text
    #     assert '手机号查单>' in login_title.text
    #     userfield =cmd.element_send_keys("id=>nloginname","13817293484") #验证输入账号
    #     time.sleep(1)
    #     pwdfield =cmd.element_send_keys("id=>npwd","abcd.1234")
    #     time.sleep(1)
    #     if userfield and pwdfield:
    #         pass
    #     draft_element =cmd.find_element_wait("xpath=>//*[@id='sliderddnormal']/div[1]/div[4]")
    #     if draft_element:
    #         move_element =cmd.find_element_wait('xpath=>//*[@id="sliderddnormal"]/div[1]/div[2]')
    #         #press_move_element封装方法讲解
    #         cmd.press_move_element(move_element,300,0)
    #         orc_element =cmd.find_element_wait('xpath=>//*[@id="sliderddnormal-choose"]/div[2]/div[1]/div/span')
    #         if orc_element:#等待输入验证码 万能验证码
    #             time.sleep(15)
    #             enter = cmd.find_element_wait("id=>nsubmit")
    #             print("页面元素", enter.text)
    #         print("end")
    #     else:
    #         enter =cmd.find_element_wait("id=>nsubmit")
    #         print("页面元素",enter.value)





# t = IndexWeb()
# print(base.get_ini_date("config","Drivers","chrome"))
if __name__ == '__main__':
    #--durations=10
    import os
    #py.test test_conf2bin.py --junit-xml=test_conf2bin_report.xml --cov-report=html --cov-config=.coveragerc --cov=./
    pytest.main(["-durations=2", cmd.stuite_path+os.sep+"test_Indexweb.py"])