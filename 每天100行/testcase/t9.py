__author__="Nightwish"
__title__="上下文管理器"


#基本语法
# with Expr as VAR:
#     BLOCK

# with open('test.txt') as f:
#     print(f.readlines())

#1.上下文表达式：with open('test.txt') as f:
#2.上下文管理器: open('test.txt')
#3.f 不是上下文管理器，应该是资源对象


class Resource():
    """
    上下管理器类
    """
    def __enter__(self):
        """
        进入函数 第一层执行逻辑
        :return: 类本身
        """

        print("===open the Resource===")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开函数 第三层执行逻辑
        :param exc_type:异常类型
        :param exc_val:异常值
        :param exc_tb:异常的错误栈信息
        :return:
        """
        print("===exit===")

    def operate(self):
        """
        第二层执行逻辑
        :return:
        """
        print("===Working===")

with Resource() as f:
    f.operate()

class Resource_():
    def __enter__(self):
        print("1")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        异常捕获 __exit__ 里返回 True（没有return 就默认为 return False），就相当于告诉 Python解释器，
        这个异常我们已经捕获了，不需要再往外抛了
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print("3")
        return True

    def operaa(self):
        1 / 0

def a():
    1 / 0
# a()
with Resource_() as f2:
    f2.operaa()


import contextlib


@contextlib.contextmanager
def open_func(file_name):
    #__enter__方法
    print('open file:',file_name,'in __enter__')
    file_handler=open(file_name,'r')


    #重点:yield
    yield file_handler

    #__exit__方法
    print('close file',file_name,'in __exit__')
    file_handler.close()
    return
with open_func(r'D:\Program Files\Projectgit\python_socket\config\2.txt') as o:
    for line in o:
        print(line)




@contextlib.contextmanager
def open_func_(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return

with open_func(r'D:\Program Files\Projectgit\python_socket\config\2.txt') as file_in:
    for line in file_in:
        1/0
        print(line)

# 使用上下文管理器有三个好处：,.m ,,,
# 提高代码的复用率；
# 提高代码的优雅度；
# 提高代码的可读性；