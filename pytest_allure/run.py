__author__="Nightwish"
__title__="入口主函数"

import pytest
import os,sys
debug=False
testdir =os.path.abspath(os.path.dirname(__file__)+os.sep+"test_case_pytest") #
resultdir =os.path.abspath(os.path.dirname(__file__)+os.sep+"allure-result")#
reportdir =os.path.abspath(os.path.dirname(__file__)+os.sep+"Report")#


if debug:print("路径",os.path.abspath(os.path.dirname(__file__)))


def gen_report(resultdir,reportdir):#形参列表
    """
    生成报告文件
    :param resultdir: str
    :param report: str
    :return: 布尔
    """
    try:
        if isinstance(resultdir,str) and isinstance(reportdir,str):
            res =os.system("allure generate "+resultdir+os.sep+" -o "+ reportdir)
            if res ==0:
                return True #None
            else:
                return False
        else:
            return "args input error"
    except Exception as err:
        print(err)

if __name__ == '__main__':
    pytest.main([testdir, '-s', '-q', '--alluredir', "./allure-result"])
    if gen_report(resultdir, reportdir):
        print("等待几秒后，发送邮件")
    os.popen("allure generate" + resultdir + os.sep + "-o " + reportdir + os.sep)