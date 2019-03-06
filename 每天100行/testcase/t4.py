__author__="Nightwish"
__title__="3-4"
import os,time
import json
from functools import  partial
from config.setting import Setting as se
set=se()


#1.编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生
class Student():
    """
    学生类
    """
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count+=1

    def learn(self):
        print("{} is learning".format(self.name))
stu1 = Student("jack", 33)
stu2 = Student("amy", 24)
stu3 = Student("lucy", 22)
print("实例化了%s个学生" % Student.count)


#2.编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
class B():
    """
    类名B 父类
    """
    def __init__(self):
        pass
    def handle(self):
        a=1
        return a


class A(B):
    """
    类名A 继承B
    """
    def __init__(self):
        pass
    def handle(self):
        super().handle()

a=A()
a.handle()


#编写程序, 如下有三点要求：
#自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
#定义用户类，定义方法db，例如 执行obj.db可以拿到用户数据结构
#在该类中实现登录、退出方法, 登录成功将状态(status)修改为True,
# 退出将状态修改为False(退出要判断是否处于登录状态).
# 密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于30秒即不允许登录)

data={
    "egon":{"password":"123",'status':False,'timeout':0},
    "alex":{"password":"456",'status':False,'timeout':0},
}

class User():
    """
    用户类
    """
    def __init__(self):
        """
        实例化函数
        """
        self.user_dic =self.read() #当前用户所有状态信息
        self.usernam=" "   #当前登陆用户名称
    def write(self):
        """
        写入文件函数
        :return:
        """
        with open(set.current_path+os.sep+r"user_info.json","w",encoding="utf-8") as f:
            jd = json.dumps(data)  # 序列化
            f.write(jd)
            f.close()

    def read(self):
        """
        读取文件函数
        :return:
        """
        with open(set.current_path+os.sep+r"user_info.json","r",encoding="utf-8") as f:
            user_dic=json.load(f) #反序列化
            return user_dic
    def db(self):
        """
        打印当前用户状态
        :return:
        """
        print("用户数据结构：", self.user_dic)

    def login(self):
        """
        登陆函数 此处开始 卡顿 需要查看部分源码 写的 思路还是有卡顿
        :return:
        """
        i = 0
        while i < 3:
            username = input("username:").strip() #用于移除字符串头尾指定的字符（默认为空格或换行符）
            password = input("password:").strip()
            if username in self.user_dic and password == self.user_dic[username]["password"]:
                time_now = time.time()  # 获取当前时间
                period = time_now - self.user_dic[username]["timeout"]  # 时间差
                if period >= 30:  # 判断时间间隔是否满足登录条件
                    print("%s登陆成功" % username)
                    self.username = username
                    self.user_dic[username]["status"] = True  # 更改用户登录状态
                    self.write()  # 将修改保存到文件
                    break
                else:
                    print("用户处于锁定状态，请%s S后再试" % (30 - period))
                    break
                    print("用户名或密码错误！")
                    i += 1
                    if i == 3 and username in self.user_dic:
                        self.user_dic[username]["timeout"] = time.time()  # 记录3次登录失败的时间点
                        self.write()  # 将修改保存到文件
                        exit("退出")

    def exit(self):
        """
        退出 函数
        :return:
        """
        if self.username:
            self.user_dic[self.username]["status"] = False
            self.write()
            print("{}用户已退出".format(self.username))

    def help_info(self):
        """
        帮助命令函数
        :return:
        """
        print("""命令列表：
         查看数据结构：db
         登录：login
         退出登录：exit""")

    def handle(self):
        """
        处理用户输入
        :return:
        """
        while True:
            cmd = input("请输入命令:").strip()
            print(cmd)
            cmd = cmd.split()
            print(cmd)
            if hasattr(self, cmd[0]):  # 使用反射
                func = getattr(self, cmd[0])  # 拿到方法名
                func()
            else:
                self.help_info()  # 打印帮助信息

u=User()
if __name__=="__main__":
    u.handle()

#养成良好的代码习惯  结构化代码
#原版代码有问题 遇到无法执行的问题 自己尝试修改 已可以执行
