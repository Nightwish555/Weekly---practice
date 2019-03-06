__title__="程序运行主入口"

from testcase.proj.src.manager import Manage
m=Manage()
class Main():

    def main(self):
        """
        入口主函数
        :return:
        """
        kk = Manage.shuju_table
        for i in range(len(kk)):
            print(i + 1, kk[i][0])
        while True:
            ch = input("输入序号进行操作：").strip()
            getattr(m, kk[int(ch) - 1][1])()  # 反射， 找到对象相应的方法并执行 需要断点看