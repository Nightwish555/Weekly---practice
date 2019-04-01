__author__="Nightwish"
__title__="Pytest测试类"

import pytest
import os,time

from My_selenium_eg.pages.cmdPage import CmdPage
from My_selenium_eg.config.element import ELEMENT

url_base=r"https://www.baidu.com"

sea=CmdPage(url_base)

class TestSearchPage():
    def setup_class(self):
        sea.get_driver()

    def teardown_class(self):
        time.sleep(20)
        sea.quit_url()

    def test_goto_url(self):
        sea.goto_url()

    def test_write_text(self):
        search_input=ELEMENT['百度文本框']
        sea._search_text(search_input,"Dota2")

    def test_click(self):
        search_btn = ELEMENT['百度一下按钮']
        sea.click_search_btn(search_btn)


if __name__ == '__main__':
    pytest.main([sea.stuite_path+os.sep+"testSearchPage.py"])
