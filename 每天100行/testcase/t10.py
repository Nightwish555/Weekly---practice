__author__="Ngithwish"
__title__="安卓apk"

# 003-安卓APK安装器
# 遍历文件夹，获取全部的APK文件，依次调用adb install命令安装到测试机中
# 遍历可以使用 os.walk 函数

import os,time
from functools import partial
import shutil
apk_list=[]

class adb_install:

    path = os.path.abspath(os.path.dirname(__file__))

    def check_apk(self,path,suffix):
        file = os.listdir(path)  # 返回path指定的文件夹包含的文件或者文件夹的名字的列表
        for i in file:
            p = os.path.join(path, i)  # 把目录和文件名拼接为一个路径
            s = p.split(os.sep)[-1]
            if os.path.isdir(p):
                self.check_dir(p, suffix)
            elif s.split(".")[-1] == suffix:
                print("File:", s)
                apk_list.append(p)


    def adb_install(self):
        for i in apk_list:
            os.system('adb install -r' +i)


if __name__ == '__main__':
    adb_i=adb_install()
    adb_i.check_apk("E:",".apk")
    adb_i.adb_install()

