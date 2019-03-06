__title__="程序启动"

import os
import sys
Base_path = os.path.dirname(os.getcwd())
sys.path.insert(0, Base_path)  # 将proj的路径添加到模块搜索路径中  新知识点
from testcase.proj.src.main import Main
m=Main()

if __name__ == "__main__":
    m.main()
