__author__="Nightwish"
__title__="Pages基类"
#coding=utf-8


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

    def find_element(self,*loc):
        """
        重写原有的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        """
        重写文本方法
        :param loc:
        :param text: 文本内容
        :return:
        """
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        """
        重写点击方法
        :param loc:
        :return:
        """
        self.find_element(*loc).click()

    def get_title(self):
        """
        重写得到网页标题的方法
        :return:
        """
        return self.driver.title
    def quit(self):
        """
        关闭网页
        :return:
        """
        self.driver.quit()

