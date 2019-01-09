# -*- coding:utf-8 -*-
__author__="Ngihtwish"

# 这个结合之前学的去改成
# 读1个文件夹把整个文件夹的
# 给转换xlsx -->csv
# 目前文件是一个叫Data
# 一个叫testdata
# 如果mode = True就是单个文件
# 如果等于fasle
# 就做1个文件夹把整个文件夹的
# 给转换xlsx -->csv
import pandas as pd
import os
def excel_to_csv(self, filename, mode=True):
    """
    excel转换 单个文件csv
    :param filename:
    :param mode:
    :return:
    """
    case_path = self.path + os.sep + "Data" + os.sep + filename + ".xlsx"
    src_path = self.path + os.sep + "testdata" + os.sep + filename + ".csv"
    if mode and os.path.isfile(case_path):
        data = pd.read_excel(case_path, index_col=0)
        data.to_csv(src_path, encoding='utf-8')
        if os.path.isfile(src_path):
            return True


