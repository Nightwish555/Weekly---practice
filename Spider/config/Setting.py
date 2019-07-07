__author__="Nightwish"
__title__="路径配置类"

import os
class Setting():
    path=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    config_path=path + os.sep + "config"
    data_path=path + os.sep + "data"
    report_path=path + os.sep + "report"





