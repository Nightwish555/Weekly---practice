__author__="Nightwish"
__title__="测试主方法"

from util.command import Command
import pytest
import os
comd=Command(5,2)

class Test_main():

    def test_a(self):
        # try:
        A=comd.jia()
        assert 7 ==A
        # except Exception as error:
        #     print(format(error))

    def test_b(self):
        # try:
        B = comd.jian()
        assert 4 == B
        # except Exception as error:
        #         #     print(format(error))


if __name__ == '__main__':
    pytest.main("pytest")
    pytest.main(["-durations=2", comd.stuite_path+os.sep+"test_main.py"])