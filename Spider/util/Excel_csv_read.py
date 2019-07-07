__author__="Nightwish"
__title="xlrd工具类"

import xlrd,time,sys,os
import datetime
from config.Setting import Setting

set=Setting()


class Excel_xlr_read():

    def __init__(self):
        """构造函数"""
        self.filename=set.data_path+os.sep+"Excel_data.xls"

    def get_format_date(self):
        now = datetime.datetime.now()
        return "{0}-{1}-{2}".format(now.year, now.month, now.day)

    def get_format_time(self,flag=False):
        """
        根据falg布尔值切换显示时间
        :param flag: True获得年月日
        :return:
        """
        if flag:
            return time.strftime("%Y%m%d")
        else:
            return time.strftime("%H%M%S")

    def load_time(self):
        """
        写入时间
        :return:
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def _open_sheet(self,sheetname):
        """
        根据sheet Name打开相应的sheet
        :param sheetname:sheet名称
        :return:
        """
        try:
            data=xlrd.open_workbook(self.filename)
            table=data.sheet_by_name(sheet_name=sheetname)
            nrows=table.nrows #获取该表中有效行数
            ncols=table.ncols #获取该表中有效列数
            return table
        except Exception as e:
            print(e)

    def _get_col_index(self,table,colName):
        """
        跟列名返回列的索引
        :param table: 表
        :param colName: 列名
        :return:
        """
        colindex=None
        for i in range(table.ncols):
            if (table.cell_value(0,i)==colName):
                colindex=i
                break
        return colindex

    def _table_value(self,table,nrow,ncol):
        """
        根据行列 读取数据
        :param table: 表
        :param nrow: 行
        :param ncol: 列
        :return:
        """
        table=self._open_sheet()
        value=table.cell_value(nrow,ncol)
        return value

    def read_row_data(self,rowNum):
        """
        根据列 读取行数据
        :param rowNum: 行索引
        :return:
        """
        table=self._open_sheet()
        if rowNum<table.nrows:
            title=table.cell_value(rowNum,self._get_col_index(table,"Title"))
            score=table.cell_value(rowNum,self._get_col_index(table,"Score"))
        else:
            print("数据 越界")







