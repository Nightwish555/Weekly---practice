from testcase import Test  #路径

#反射全局方法
if hasattr(Test,"a"): #判断有没有这个方法
    func=getattr(Test,"a")
    func() #反射执行的Test文件下面的A方法
else:
    print("没有找到")

#反射成员函数
if hasattr(Test,"TestDemo"): #判断有无这个类
    func_1=getattr(Test,"TestDemo")
    func_1(name="ccy").run() #构造器需要实例化对象
else:
    print("类下没有找到此函数")

#反射类变量
if hasattr(Test,"TestDemo"):
    func_1=getattr(Test,"TestDemo")
    if hasattr(func_1,"tt"):
        print("修改前",getattr(func_1,"tt"))
        setattr(func_1,"tt","110")
        print("修改后",getattr(func_1,"tt"))
else:
    print("类下面没有找到此函数")
print("实际结果修改为",Test.TestDemo("ccy").tt)

#反射构造器
t=Test.TestDemo("ccy")
if getattr(t,"name"):
    setattr(t,"name","jyj")
    print(getattr(t,"name"))

