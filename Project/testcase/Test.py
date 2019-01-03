#-*- coding:utf-8 -*-
def a():
    """
    #全局方法a()
    :return:
    """
    print('执行了函数a')

def b():
    print('执行了函数b')

def c():
    print('执行了函数c')

class TestDemo():
    tt=100 #类变量

    def __init__(self,name):#类构造器
        self.name=name

    def run(self): #类成员方法
        a()#调用全局方法，12层看1层的
        b()
        c()


