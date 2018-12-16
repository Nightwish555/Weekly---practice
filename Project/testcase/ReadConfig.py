# usr/bin/env python
# -*- coding:utf-8 -*-
#单行读取模式
#读取文件的rb模式
#写文件的w模式
#写文件的追加模式 txt

import os
class Path1:
    def __init__(self):
        pass

    def path(self):
        """
        #获取当前py文件所在目录
        :return:
        """
        dir =os.path.abspath(os.path.dirname(__file__)) #\   /
        return dir
    #读取同级目录下的txt文件内容 mode:r
    def read_txt(self,filename):
        """
        :param filename: 相对路径
        :return:
        """
        with open(self.path()+"./../config/"+filename,encoding="utf-8") as fd:
            res=fd.read()
            return res
    #以二进制 格式 读取文件  mode:rb
    def only_read_text(self,filename):
        with open(self.path() + "./../config/" + filename,"rb") as zd:
            zes=zd.read()
            return zes
    #对文件进行写入 mode:w
    def write_text(self,filename,str):
        with open(self.path() + "./../config/" + filename,"w",encoding="utf-8") as wr:
            wr.write(str)
    #以追加模式对之前文件进行 写入 mode:a+
    def add_write_text(self,filename,str):
        with open(self.path() + "./../config/"+filename,mode="a+",encoding="utf-8") as zx:
            zx.write(str)
    #以二进制重新打开一个文件 之后开始从开头写入内容 即会删除原有的内容 mode:wb
    def delete_write_text(self,filename,str):
        with open(self.path() + "./../config/" + filename,"wb") as wb:
            s=bytes(str,encoding="utf-8")
            wb.write(s)
#先创建一个实例
p=Path1()
#调用读取方法 去读取一个txt文件
print(p.read_txt("1.txt")) #代表传参参数

#调用读取方法 mode:rb
print(p.only_read_text("1.txt"))

#对一个文件进行 写入 然后读取内容
p.write_text("2.txt","新的内容")
print(p.read_txt("2.txt"))

#对2.txt 进行追加写入 然后读取内容
p.add_write_text("2.txt","追加内容")
print(p.read_txt("2.txt"))

#对2.txt以二进制重新写入 然后读取
p.delete_write_text("2.txt","新的二进制内容")
print(p.read_txt("2.txt"))


#pyquery 选择器模式

