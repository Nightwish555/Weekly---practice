__author__="Nightwish"
__title__="3-6"

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
        将对象序列化到文件中 这段代码有问题
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

#这段代码有问题 必须自行修改



#GM指令模版解析
#add_item item_id, num 是一个增加道具的GM指令
#如果我们想增加1001~1003这几个道具各10个，需要这么执行3次，如果要加大量的道具，那执行的次数就更多了
# 为了提升效率，设计GM指令模版，需要满足以下几种形式
# add_item {{1001 to 1003}},10
# 解析为：
# add_item 1001,10
# add_item 1002,10
# add_item 1003,10

# add_item {{1001,1003,1006}},10
# 解析为：
# add_item 1001,10
# add_item 1003,10
# add_item 1006,10

# add_item {{1001 to 1005 not 1002,1003}},10
# 解析为：
# add_item 1001,10
# add_item 1004,10
# add_item 1005,10
s="add_item {{1001 to 1003}},10"

# 卡住了目前思路是用正则做
def check_cmd(str):
    if re.match("add_item",str).span():
        print(1)
        return True

    else:
        print(2)
        return False

check_cmd(s)









