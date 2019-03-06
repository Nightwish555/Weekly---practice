__title__="管理教师类"

"""
创建教师，删除教师，查看教师
"""
from testcase.proj.src.my_pickle import My_pickle
from testcase.proj.config.settings import Settings as sets
from testcase.proj.src.teacher import Teacher
set=sets()
class Manage():
    """
    管理员类
    """

    shuju_table=[("查看教师", "show_teacher"),("创建教师", "create_teacher"),
            ("删除教师", "delete_teacher"), ("退出", "exit")]
    def __init__(self):
        """
        实例化 处理 实例My_pickle
        """
        self.teacher_pickle_obj = My_pickle(set.teacher_file)  # 实例化MyPickle类，teacher_file是settings中的教师文件路径

    def show(self, pickle_obj):
        """
        查看教师方法 此函数完全照搬
        :param pickle_obj:
        :return:
        """
        pick_obj = getattr(self, pickle_obj)  #这个写法 不太懂
        data_g = pick_obj.read()  # 读取对象信息
        for teacher_obj in data_g:
            for key in teacher_obj.__dict__:
                print(key, teacher_obj.__dict__[key])  # 打印对象信息
            print("-" * 50)

    def show_teacher(self):
        """
        查看教师
        :return:
        """
        print("教师信息".center(45, "-"))
        self.show("teacher_pickle_obj")

    def create_teacher(self):
        """
        创建教师
        :return:
        """
        name=input("教师名称:").strip()
        type=input("教师所教科目:").strip()
        teacher=Teacher(name,type)
        self.teacher_pickle_obj.write(teacher)

    def delete_teacher(self):
        """
        删除教师
        :return:
        """
        self.show_teacher()
        teacher_del = input("输入要删除的教师姓名：").strip()
        self.teacher_pickle_obj.delete(teacher_del)  # 删除
        print("删除成功！")
    def exit(self):
        """
        退出
        :return:
        """
        exit()
