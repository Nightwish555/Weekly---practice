# -*- coding:utf-8 -*-
__author__="Nightwish"

from functools import partial
import os
import hashlib
import shutil
path=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
class Test_1:
    #(dirname,filename)形参列表
    def check_dir(self,dirname,dirname_):
        """
        检查上面的文件夹和文件是否存在，如果不存在就创建
        :param dirname:
        :param filename:
        :return:
        """
        dirpath=path+os.sep+dirname_
        if os.path.exists(dirpath):
            print()
        else:
            os.makedirs(dirpath)
        if os.path.exists(dirpath+os.sep+dirname):
            print("文件夹和文件已经存在")
        else:
            os.makedirs(dirpath+os.sep+dirname)
            file=open(dirpath+os.sep+dirname+os.sep+ "1.html",'w')
            file.close()#关闭句柄

    def build_dir(self,dirname):
        """
        创建3级目录
        :param dirname:
        :return:
        """
        check_dir1=partial(self.check_dir,dirname_=dirname)
        check_dir1("new")
        check_dir1("old")



    def md5_get(self,filename):
        """
        获取文件的md5，并返回一个值
        :param filename: 文件名
        :return: 文件的md5值
        """
        file = open(filename,'rb')
        md5 = hashlib.md5(file.read()).hexdigest()
        file.close()
        return md5

    def md5_compare(self,filename):
        """
        对比3级目录下的.html文件的md5 如果相同删除new目录下的.html 如果不同输出到新的目录下
        :param filename:
        :return:
        """
        m1=self.md5_get(r'E:/Gitproject/Project'+ os.sep + filename +os.sep+ 'new/1.html')
        m2=self.md5_get(r'E:/Gitproject/Project'+ os.sep + filename + os.sep+ 'old/1.html')
        if m1==m2:
            os.remove(r'E:/Gitproject/Project'+ os.sep + filename +os.sep+ 'new/1.html')
        else:
            shutil.move(r'E:/Gitproject/Project'+ os.sep + filename +os.sep+ 'new/1.html','E:\Gitproject\Project\Aew_html')

T=Test_1()
T.build_dir("C")
T.build_dir("java")

