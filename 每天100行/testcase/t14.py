__author__="Nightwish"
__title__="async"


import requests
import asyncio
async  def execute(x):
    print('Number:',x)
    return x

coroutine=execute(1) #返回一个coroutine协程对象
print('Coroutine',coroutine)
print('After calling execute')

loop=asyncio.get_event_loop()  #创建一个事件循环loop
task=loop.create_task(coroutine)
print('Task',task)
loop.run_until_complete(task)  #调用run_until_complete将方法注册到loop中并启动
print('Task',task)
print('After calling loop')

import time
import aiohttp
start=time.time()

async def gets(url):
    sessionn=aiohttp.ClientSession()
    response=await sessionn.get(url)
    result=await response.text()
    sessionn.close()
    return result

async def request():
    url="https://www.baidu.com"
    status=await gets(url)
    return status

def callback(task):
    print('Status:',task.result())

coroutine=request()
task=asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task',task)

loop=asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task',task)

tasks=[asyncio.ensure_future(request()) for _ in range(10)]
print('Tasks',tasks)

loop.run_until_complete(asyncio.wait(tasks))
for t in tasks:
    print('Tasks Result',task.result())

end=time.time()
print('Current time:',end-start)