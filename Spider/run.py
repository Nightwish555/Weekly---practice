__author__="Nightwish"
__title__="入口函数"

from util.Spider_base import SpiderBase
from util.Excel_csv_write import Excel_xlr_write
from util.Mysql_handle import Mysql_handle
import time

#创建一个字典用来保存异步协程获取到的数据
dic={}
time_=time.strftime("%Y%m%d-%H%M%S")
def main():
    """
    执行函数
    :return:
    """
    base_url = "https://movie.douban.com/top250?start="

    #构造所需url
    url_list=[base_url+str(num) for num in range(0,225+1,25)]

    #创建并启动协程
    for url in url_list:
        s=SpiderBase(url,dic)
        s.parse_page()

    #遍历字典输出数据
    # for k,v in dic.items():
    #     print(k,v)

def _Excel_write():
    Excel = Excel_xlr_write("Sheet1")
    Excel._write_row_col_data(0, 0, "Title")
    Excel._write_row_col_data(0, 1, "Score")
    Excel._write_data(**dic)
    Excel._save_excel()

def _Mysql_write():
    m=Mysql_handle()
    cur=m._mysql()
    with cur as db:
        for k,v in dic.items():
            sql="INSERT INTO spider_tbl(spider_title,spider_score)VALUES('%s','%s')" %(k,v)
            db.execute(sql)
        cur.commit()#执行commit操作，插入语句才能生效
if __name__ == '__main__':
    main()
    # _Excel_write()
    _Mysql_write()

