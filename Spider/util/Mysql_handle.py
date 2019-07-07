__author__="Nightwish"
__title__="Mysql 操作"

import pymysql
import contextlib

class Mysql_handle():

    def __init__(self):
        pass
    def _mysql(self):
        # 打开数据库
        db = pymysql.connect(host="localhost", user="root", password="root123", db="my_base", port=3306)
        return db
    @contextlib.contextmanager
    def open_mysql(self):
        """打开数据库"""
        #鼠标游标
        cur=self._mysql().cursor()
        try:
            yield cur
        except Exception as e:
            raise e
        finally:
            self._mysql().close()

