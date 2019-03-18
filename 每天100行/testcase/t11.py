__author__="Nightwish"
__title__="安卓截图工具"

import os,time
import configparser
from config.setting import Setting
set=Setting()

cf=configparser.ConfigParser()
cf.read(set.current_path+os.sep+"config.ini")
tool_cap_folder=cf.get("tool_cap","cap_folder")

class tool_screen():
    """
    安卓截图工具
    """
    def get_screent(self,folder):
        current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        os.system("adb shell screencap -p /sdcard/screen" + current_time + ".png")
        os.system("adb pull /sdcard/screen"+current_time+".png"+folder)

if __name__ == '__main__':
    tool=tool_screen()
    tool.get_screent(tool_cap_folder)



