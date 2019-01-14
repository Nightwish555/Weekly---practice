
from openpyxl import load_workbook
import pytest,os
from util import ReadOpenData
from util.command import Command
cmd =Command()

class TestCase():
    c = ReadOpenData.ReadOpenData()
    path = os.path.abspath(os.path.dirname(__file__))
    def setup_class(self):
        self.workbook = load_workbook(self.path + '/../test_data/data.xlsx')  # 读取的是上层目录的test_data
        print("只执行一次")

    def test_get_cell_by_row_equals(self):
        "验证get_cell_by_row返回数据是否正确"
        print("执行行为",self.c.get_cell_by_row(0, 0))
        assert self.c.get_cell_by_row(0, 0)=="caseID" #,msg="对象返回数据等于caseID"


if __name__ == '__main__':
    pytest.main([cmd.stuite_path+os.sep+"test1.py"])