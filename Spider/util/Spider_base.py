__author__="Nightwish"
__title__="Spider类"

from config.Setting import Setting
from util.Json_handle import Json_handle
import time,asyncio,requests,aiohttp,json,os
from lxml import etree

set=Setting()
js_handle=Json_handle()


class SpiderBase():

    def __init__(self,url,q):
        # #重写父类方法__init__
        # super().__init__()
        self.url=url
        self.q=q
        self.headers=js_handle.check_exists_json()

    async def get(self,url,headers):
        """
        异步协程 get()
        :param url:
        :param headers:
        :return:
        """
        session=aiohttp.ClientSession()
        response=await session.get(url=url,headers=headers)
        result=await response.text()
        await session.close()
        return result

    async def send_request(self,url):
        """
        发送请求方法
        :param url:
        :return:
        """
        #请求3次
        i=0
        if i<=3:
            try:
                print(u"[INFO]请求url:"+url)
                status=await self.get(url,self.headers)
                return status
            except Exception as e:
                print(u'[INFOG] %s%s' % (e,url))
                i+=1

    def parse_page(self):
        """
        解析网站源码 采用xpath提取
        :return:
        """
        coroutine = self.send_request(self.url)
        loop = asyncio.get_event_loop()
        task = loop.create_task(coroutine)
        response = loop.run_until_complete(task)
        # loop.close()
        html = etree.HTML(response)

        # 获取一页的电影数据
        node_list = html.xpath("//div[@class='info']")

        for move in node_list:
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]

            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

            # 将每一步电影的名称跟评分加入到字典
            self.q[title] = score


