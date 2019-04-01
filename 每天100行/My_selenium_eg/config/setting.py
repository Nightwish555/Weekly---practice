__author__="Nightwish"
__title__="配置路径类"
from selenium.webdriver.common.by import By
import os
class Setting():
    current_path=os.path.abspath(os.path.dirname(__file__))
    print(current_path)
    # 截图路保存径，绝对路径，也可以用相对路径
    SCREENSHOTURL = 'E:/Gitproject/每天100行/My_selenium_eg/screenshot/'


