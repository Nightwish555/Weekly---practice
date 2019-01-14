import pytest,os
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