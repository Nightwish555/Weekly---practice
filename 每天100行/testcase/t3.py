__author__="Nightwish"
__title__="3-3"

import os,time
import logging
from functools import partial

#wrapper适合用变参作为输入参数，这样就不会阻碍被装饰函数参数的变动了。
#wrap中使用变参，修改函数，只要修改被装饰函数自己就可以了
#装饰器
def log(func):
    """
    装饰器
    :param func: 函数做参数 传入
    :return: 内嵌函数wrapper
    """
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log #等价于 now=log(now)
def now():
    """
    被修饰函数
    :return:
    """
    print(time.localtime())

now()


#题目 杨辉三角 :把每一行看做一个list，试写一个generator，不断输出下一行的list
#生成器 列表生成式

def triangles():
    """
    杨辉三角 规律 每个数字等于上前一行2数字相加
    :return:
    """
    L=[1]
    n=1
    while n<=10:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
        n+=1
def check_t():
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
check_t()

#迷你聊天机器人|生成器的高级用法
class small_robot_chat():
    def chat_robot(self):
        """
        生成器 高级用法 类似于一个协程函数
        :return:
        """
        res=""
        while True:
            #执行到 yield res 时，chat_robot 函数就返回一个迭代值，
            #下次迭代时，代码从 yield res 的下一条语句继续执行，
            #而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield
            receive=yield res  #循环执行到这一步 挂起
            if "hi" in receive or "hello" in receive:
                res="nihao"
            elif "name" in receive:
                res="yangtuo"
            elif "age" in receive:
                res="1"
            elif "hobby" in receive:
                res="dayouxi"
            elif "country" in receive:
                res="China"
            elif "woqu" in receive:
                res="nima"
            else:
                res="Sorry, I can't understand your input"

    def window_chat(self):
        """
        前台不断的获取用户的输入,然后利用协程发送给后台处理
        :return:
        """

        Chat=self.chat_robot()
        next(Chat) #返回下一个可迭代的对象

        while True:
            input_=input("Please input :")
            if input_=="q" or input_=="Q":
                print("Robot is exit")
                break
            Response=Chat.send(input_)
            print("Robot:{}".format(Response))
        Chat.close()  #关闭生成器

src=small_robot_chat()
src.window_chat()










