__author_="Nightwish"
__title__="json处理"

from config.Setting import Setting
import os,json

set=Setting()

class Json_handle():

    def check_exists_json(self):
        """
        判断json是否存在和合法
        :return:
        """
        with open(set.config_path+os.sep+"config.json","r",encoding="utf-8") as file:
            res=json.load(file)
            return res


