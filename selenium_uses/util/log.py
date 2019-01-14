#! python3
# -*- coding: utf-8 -*-
'a practice of ...'

from config import config #替换成from config import setting
import logging
import time
import os

path = os.path.abspath(os.path.dirname(__file__))
path = path + config.lcmTest_log_path  #这个变成path = path +setting.log_path  在setting.py里面建立1个常量叫log_path

# 获得一个记录器
_logger = logging.getLogger('lcmTest')
# 设置等级
_logger.setLevel(logging.DEBUG)
# 文件输出在文件上
fh = logging.FileHandler(path, encoding='UTF-8')
fh.setLevel(logging.INFO)
# 创建一个格式化对象，用于将日志记录转化为指定格式的字符串
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
# 为指定程序设置格式化
fh.setFormatter(formatter)
# 分别和status按位与运算，将指定的处理程序添加到记录器_logger中
_logger.addHandler(fh)

def debug(msg):
    _logger.debug(" DEBUG " + str(msg))

def info(msg):
    _logger.info(" INFO " + str(msg))

def error(msg):
    _logger.error(" ERROR " + str(msg))

def warn(msg):
    _logger.warning(" WARNING " + str(msg))

def close_logger():
    h_list = _logger.handlers
    for h in h_list:
        _logger.removeHandler(h)