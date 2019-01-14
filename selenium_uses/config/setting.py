import os

class Setting():

    _path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    _xlsx_path =_path + os.sep + "test_data" + os.sep + "data.xlsx"
    debug =True