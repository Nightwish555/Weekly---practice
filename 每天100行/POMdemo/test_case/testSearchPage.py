__author__="Nightwish"
__title__="Pytest测试类"

import pytest
import os,time

from POMdemo.pages.searchPage import SearchPage

url_base=r"https://www.baidu.com"

sea=SearchPage(url_base)

class TestSearchPage():
    def setup_class(self):
        sea.get_driver()

    def teardown_class(self):
        time.sleep(20)
        sea.quit_url()

    def test_goto_url(self):
        sea.gotoBaidu()
    def test_write_text(self):
        sea.input_search_text("游民星空")

    def test_click(self):
        sea.click_search_btn()


if __name__ == '__main__':
    pytest.main([sea.stuite_path+os.sep+"testSearchPage.py"])
