
import pytest  #3.7.4
import requests
from functools import partial  #偏函数
import allure #pip install pytest-allure-adaptor  

def request_get(url):
    return requests.get(url).status_code

name_list =["4.12","4.10","4.13","4.14","4.15"]  #支持循环入参，支持全局以及下文的类变量


@allure.feature('测试开启')  #被测试功能的大类名称 报告体现
class TestDemo():

    #偏函数用法
    case1 =partial(request_get,url="https://mvnrepository.com/artifact/junit/junit/4.12")
    case2 =partial(request_get,url="https://mvnrepository.com/artifact/junit/junit/4.12")
    test_list =[case1(),case2()]

    @pytest.mark.parametrize("args",test_list)  #pytest支持参数化
    @allure.story('执行test_a1') #被测试子功能 报告体现
    def test_a1(self,args):
        assert args ==200

    @pytest.mark.parametrize("args",test_list)
    def test_a2(self,args):
        assert args ==200

    flag =10
    def test_a(self):
        r =requests.get("https://mvnrepository.com/artifact/junit/junit/4.12")
        assert r.status_code ==200
        print(hasattr(TestDemo,"flag"))
        if hasattr(TestDemo,"flag"):
            setattr(TestDemo,"flag",9)#修改test_b为不跳过

    def test_b(self):
        if TestDemo.flag ==9:
            #"4.12","4.10","4.13","4.14","4.15"
            r =requests.get("https://mvnrepository.com/artifact/junit/junit/4.12")
            assert r.status_code ==200
        elif TestDemo.flag ==10:
            return 0

    @pytest.mark.parametrize("args",name_list)
    def test_c(self,args):
        r =requests.get("https://mvnrepository.com/artifact/junit/junit/"+args)
        assert r.status_code ==200



