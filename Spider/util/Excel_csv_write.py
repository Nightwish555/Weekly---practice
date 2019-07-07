__author__="Nightwish"
__title__="xlwt工具类"

from config.Setting import Setting
import os,xlwt

set=Setting()


class Excel_xlr_write():

    def __init__(self,sheetName):
        """构造函数"""
        self.file=xlwt.Workbook(encoding='utf-8')
        self.table = self.file.add_sheet(sheetName)

    def _write_data(self,**kwargs):
        """写入数据"""
        nrow=0
        for i,k in kwargs.items():
            nrow=nrow+1
            self.table.write(nrow,0,i)
            self.table.write(nrow,1,k)

    def _write_row_col_data(self,nrow,ncol,data):
        """根据行列 写入数据"""
        self.table.write(nrow,ncol,data)

    def _save_excel(self):
        """保存文件"""
        self.file.save(set.data_path + os.sep + "Excel_data.xls")


