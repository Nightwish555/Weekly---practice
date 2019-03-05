__title__="处理文件类"

import json
import pickle
import os,time
class My_pickle():

    def __init__(self,filename):
        """
        初始化文件函数
        :param filename:
        """
        self.filename=filename

    def write(self,data):
        """
        写入文件函数
        :param data:
        :return:
        """
        with open(self.filename,"ab",encoding="utf-8") as f:
            json.dump(data,f)

    def read(self):
        """
        读取文件函数 pickle 模块第一见 第2天继续学习
        :return:
        """
        with open(self.filename, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    yield data
                except:
                    break
    def delete(self,name):
        """
        删除文件函数  .bak备份文件,为文件格式扩展名
        :param name:
        :return:
        """
        f2 = My_pickle(self.filename + ".bak")  # 新建一个文件
        for item in self.read():
            if item.name==name:
                pass
            else:
                f2.write(name)
        os.remove(self.filename)  # 删除旧文件
        os.rename(self.filename + ".bak", self.filename)  # 新文件名重命名为旧文件名





