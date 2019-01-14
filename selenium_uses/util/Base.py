import os,datetime
import time
import configparser
import openpyxl,xlrd #操作excel读和写
from config.setting import Setting as set #文件路径类


class MyConf(configparser.ConfigParser):
    '''
    因为configparser读取的数据会自动转换为小写字母，自己抽取出来修改configparser
    作用是不影响源码
    '''

    def __init__(self):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

conf =MyConf()

class Base(object):

    path = set._path #其他类导入
    BaseDir = path+os.sep+"Report"
    iniDir = path+os.sep+"config" #预防linux和wins / \
    xlsx_path = set._xlsx_path

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

    def get_report_path(self,get_ini_date):
        """
        创建Report-年月日文件夹 Report-20180706
        :return: 返回文件夹下面的 Report_小时分钟.html
        """
        "格式月日/单位时间格式的.html，只用到time"
        nowtime = time.localtime()
        dir_date = time.strftime('-%Y%m%d', nowtime) #Report-年月日
        if not os.path.exists(self.BaseDir + dir_date):
            os.mkdir(self.BaseDir + dir_date)
            print("路径===》",self.BaseDir + dir_date)
        day_file = time.strftime('%H%M', nowtime)
        return self.BaseDir + dir_date + os.sep + 'Report_' + day_file + '.html'

    def chrome_path(self):
        "谷歌的浏览器驱动"
        return self.get_ini_date("config","Driver", "chrome")

    def firefox_path(self):
        "火狐的浏览器驱动"
        return self.get_ini_date("config","Driver", "firefox")

    def get_ini_date(self,ininame,sections, item):
        """
        关键字驱动
        :param sections: ini类型文件.sections
        :param item: get.item =>value
        :return: str字符串
        """
        try:
            iniconf = self.iniDir+os.sep+str(ininame)+".ini"  # .read()特性问题不接收拼接
            conf.read(iniconf, encoding="utf-8")
        except Exception as error:
            raise (error)
        return conf.get(sections, item)

    def load_time(self):
        """
        写入时间
        :return:
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def _get_cols_index(self, table, columnName):
        """
        读取列数据 不直接使用
        :param table:
        :param columnName:
        :return:
        """
        columnIndex = None  # 初始值
        for i in range(table.ncols):
            if (table.cell_value(0, i) == columnName):
                columnIndex = i
                break
        return columnIndex

    def _read_data_byName(self, fileName, sheetName):
        """
        读取excel的sheet数据 不直接使用
        :param fileName:
        :param sheetName:
        :return:
        """
        table = None
        errorMsg = ""
        try:
            data = xlrd.open_workbook(fileName)
            table = data.sheet_by_name(sheetName)
        except Exception as msg:
            errorMsg = msg
        return table, errorMsg

    def read_data_byIndex(self, fileName, sheetIndex):
        table = None
        errorMsg = ""
        try:
            data = xlrd.open_workbook(fileName)
            table = data.sheet_by_index(sheetIndex)
        except Exception as msg:
            errorMsg = msg
        return table, errorMsg

    def read_row_data(self, rowNum):
        """
        直接excel数据 按行row读取对应列数据
        :return:
        """
        table = self._read_data_byName(self.xlsx_path, 'Sheet1')[0]
        if rowNum < table.nrows:
            caseId = table.cell_value(rowNum, self._get_cols_index(table, "caseID"))  # 根据列读取行的内容
            start_time = table.cell_value(rowNum, self._get_cols_index(table, "startTime"))
            response = table.cell_value(rowNum, self._get_cols_index(table, "response"))
            result = table.cell_value(rowNum, self._get_cols_index(table, "最终结果"))
            return int(caseId), int(start_time), response, result
        else:
            return "row越界，请检查"


    def read_dict_data(self, rowNum,key):
        """
        * 读取行数据拿到对应列的value
        :param rowNum: 行数据
        :param key:对应列
        :return: str
        """
        col_dict = {}
        try:
            wb = xlrd.open_workbook(self.xlsx_path)
            table = wb.sheet_by_index(0)
            for i in range(table.ncols):  # 列表
                col_dict[i] = table.cell_value(rowNum, i)  # 1,0
                res =col_dict.get(key) #变量拦截
                if type(res) is float: #type(res).__name__ is "float"
                    return int(res)
            return res
        except Exception as error:
            print(format(error))


    def response_ms(self,start):
        """
        返回时间
        :param start:
        :return:
        """
        end =time.clock() -start
        return str(int(end*1000))+" ms"


    def get_yaml_data(self): #获取yaml的数据
        pass

u =Base()


