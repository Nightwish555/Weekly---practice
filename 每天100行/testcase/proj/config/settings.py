"""
定义常量
"""
import os
class Settings():
    """
    配置常量类
    """
    base_path= os.path.dirname(os.getcwd())
    teacher_file = os.path.join(base_path, "db", "teacher_info")  # 教师文件路径