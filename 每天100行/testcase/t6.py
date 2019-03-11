__author__="Nightwish"
__title__="3-8"

import os
import time
import random
import pickle
import re
# 5、定义MySQL类
# 要求：
# 1.对象有id、host、port三个属性
# 2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
# 3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
# 4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号
# 保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
class Setting():
    DB_PATH=os.path.join(os.getcwd(), "db")
    HOST = "127.0.0.1"
    PORT = 8080
set=Setting()
class MySQL():
    def __init__(self,host=set.HOST, port=set.PORT):
        self.host=host
        self.port=port
        self.id=self.create_id()

    def create_id(self):
        """
        创建唯一ID
        :return:
        """
        id_=random.randint(1,10000)
        L=[]
        L.append(id_)
        while id_ in L:
            id_=random.randint(1,10000)
        return  id_

    def save(self):
        """
        将对象序列化到文件中
        """
        if not os.path.isfile(os.path.join(set.DB_PATH, str(self.id))):  # 判断文件是否存在
            with open(os.path.join(set.DB_PATH, str(self.id)), "wb") as f:
                pickle.dump(self, f)
        else:
            raise AttributeError("the id has already existed")

    def get_obj_by_id(self, obj_id):
        """
        反序列化对象
        """
        with open(os.path.join(set.DB_PATH, str(obj_id)), "rb") as f:
            mysql_obj = pickle.load(f)
        print(mysql_obj)
        print(mysql_obj.id,mysql_obj.host, mysql_obj.port)



# mysql = MySQL()  # 默认从配置文件中读取host和port
# mysql1 = MySQL("192.168.0.11", 8089)  # 用户传入host和port
# mysql1.save()
# mysql.get_obj_by_id(1528189434)

#更改 用json序列化 数据















