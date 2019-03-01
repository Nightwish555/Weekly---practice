__author__="Nightwish"
__title__="3-1"
import os,time
import shutil

# 题目：完成一个函数，实现功能为判断一个字符串是否是一个合法的ip地址
# 输入：任意字符串
# 输出：如果是一个合法ip地址，返回true；否则，返回false
# 举例：输入10.0.0.1，输出true；输入aaaa，输出false
#用pytest 测试框架 做测试用例
class Ip():

    def split(self,ip):
        if isinstance(ip,str):
            ip_=ip.split(".",3)
            return ip_

    def Judege(self,str):
        if len(str)!=4:
            return False
        for i in range(len(str)):
            try:
                if str[0]==0:
                    print("0开头不合法")
                    return False
                if isinstance(int(str[i]),int):
                    if int(str[i])>=0 and int(str[i])<256:
                        pass
                    else:
                        print("不合法")
                        return False
                else:
                    return False
            except Exception as e:
                print(format(e))

        return True
# i=Ip()
# p=i.split("asd")
# print(i.Judege(p))

#代码思量：if判断过多 感觉应该有更好的实现方法 之后会重写

#题目：A文件夹下有多个子文件夹（a1 b1 c1）,每个子文件夹下有好几张jpg图片，需要把这个这些图片全部拷贝并存在B文件夹下。

class Check_file():

    path=os.path.abspath(os.path.dirname(__file__))

    def check_dir(self,path,suffix):
        file=os.listdir(path) #返回path指定的文件夹包含的文件或者文件夹的名字的列表
        for i in file:
            p=os.path.join(path,i) #把目录和文件名拼接为一个路径
            s=p.split(os.sep)[-1]
            if os.path.isdir(p):
                self.check_dir(p, suffix)
            elif s.split(".")[-1] == suffix:
                print("File:",s)
                shutil.copy(s,"E:\Gitproject\每天100行\C")

c=Check_file()
c.check_dir("E:\Gitproject\每天100行","py")
#代码思量：同模块下 相同名字的PNG 或者TXT文件未考虑进去 之后考虑加进去


#3.实现一个单例模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls,"_instance"):
            cls._instance=object.__new__(cls,*args,**kwargs)
            return cls._instance

class Testclass(Singleton):
    a = 1
test1 = Testclass()
test2 = Testclass()
print (test1.a, test2.a)

test1.a = 2
print(test1.a, test2.a)

print(id(test1), id(test2))
#代码思量：照着别人写了一个 目前对此还一知半解 理解了 要添加相应的注释