import pytest
import time,os
from util.command import Command
cmd =Command()

class TestNoComm():

    def test_a(self):
        a =1
        assert a==1
        print(1)


    def test_Z(self):
        a = 1
        assert a == 1
        print(2)


    def test_b(self):
        a = 1
        assert a == 1
        print(3)

if __name__ == '__main__':
    pytest.main(['-s',cmd.stuite_path + os.sep + "test_no_action.py"])
    print(ord("Z"))
    print(ord("a"))


# @pytest.fixture(scope='function') #作用到函数
# def resource():
#     x = ["123"]
#     return x
#
#
# def test_a(resource):
#     time.sleep(1)
#     assert resource ==["1123"]
#
#
# def test_2(resource):
#     time.sleep(1)
#     assert "123" in resource
#
# def test_3(resource):
#     time.sleep(1)
#
#
# def test_4(resource):
#     time.sleep(1)
#
# @pytest.mark.parametrize('x', list(range(10))) #第1个区域是入参，第2个区域是list区域
# def test_something(x):
#     time.sleep(1)


    #pytest.main(["--maxfail=2", cmd.stuite_path + os.sep + "test_no_action.py"])