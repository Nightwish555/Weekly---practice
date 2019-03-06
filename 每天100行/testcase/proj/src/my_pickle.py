__title__="处理文件类"

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
        with open(self.filename,"ab") as f:
            pickle.dump(data,f)

    def read(self):
        """
        读取文件函数 pickle 模块第一见 pickle与json 一样都是正反序列化
        但是pickle只能在python内使用 且不同版本python不兼容
        而json可以在不同语言之间交互 且效率更高
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
        :param name:指定name 进行删除
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





