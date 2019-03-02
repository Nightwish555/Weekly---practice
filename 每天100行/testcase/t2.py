__author__="Nightwish"
__title__="3-2"

import os,time
from functools import partial

#斐波那契数列 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。
class Fiseq():
    """
    斐波那契数列 递归最方便
    """
    def calculation(self,n):
        if n==1 or n==2:
            return 1
        return self.calculation(n-1)+self.calculation(n-2)
i=Fiseq()
print(i.calculation(10))

#九九乘法表
def Multiplication_table():
    """
    九九乘法表
    :return:
    """
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}x{}={}\t".format(j,i,i*j),end="")
        print()

Multiplication_table()

#十进制转二进制、八进制、十六进制
class Bconf():
    """
    十进制转二进制、八进制、十六进制
    """
    def __init__(self,num):
        self.num=num
    def bin_(self):
        return bin(self.num)
    def oct_(self):
        return oct(self.num)
    def hex_(self):
        return hex(self.num)
bc=Bconf(5)
bc.bin_()
bc.oct_()
bc.hex_()


#约瑟夫生者死者小游戏 30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

class Games():
    people = {}
    for x in range(1, 31):
        people[x] = 1
    print(people)
    def games(self):
        """
        题意理解不通透，有人下船后，报数是在下船后的人开始重新报数
        :return:
        """
        check = 0
        i = 1
        j = 0
        while i <= 31:
            if i == 31:
                i = 1
            elif j == 15:
                break
            else:
                if self.people[i] == 0:
                    i += 1
                    continue
                else:
                    check += 1
                    if check == 9:
                        self.people[i] = 0
                        check = 0
                        print("{}号下船了".format(i))
                        j += 1
                    else:
                        i += 1
                        continue

g=Games()
g.games()

# 这次没用递归 下次用递归

#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def Threed():
    count=0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=j and i!=k and j!=k:
                    print(i*100+j*10+k)
                    count+=1
    print(count)
Threed()




