__author__="Nightwish"
__title__="元素类"

from selenium.webdriver.common.by import By
# 页面元素
ELEMENT = {

    # 百度登录界面元素
    '百度文本框': (By.ID, r"kw"),
    '百度一下按钮': (By.ID, r"su"),

}
print(*ELEMENT['百度文本框'])



