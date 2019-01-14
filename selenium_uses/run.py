# -*- coding: utf-8 -*-
'a practice of ...'
"入口函数文件"
try:
    import unittest
    from util.Base import TimeUtil
    import time
    from util import ReadOpenData,HTMLTestRunner,ClientSelenium
    from config import setting

except ImportError as error:
    raise error

if __name__ == '__main__':
    utime = TimeUtil()
    suite = unittest.defaultTestLoader.discover(setting.TestDir,pattern='test_*.py')
    fb = open(utime.get_report_path(), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='本次测试数据', description='结论:')
    runner.run(suite)
    fb.close()