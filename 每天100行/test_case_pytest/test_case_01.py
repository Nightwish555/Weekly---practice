__author__="Nightwish"
__title__="3-1"

import pytest
import os,time
import sys
from testcase.t1 import Ip as ip
i=ip()

class Test_01():

    def test_01(self):
        p=i.split("asd")
        assert i.Judege(p)==True

    def test_02(self):
        p=i.split("0.2.5.6")
        assert i.Judege(p)==True

    def test_03(self):
        p=i.split("1.2.5.6")
        assert i.Judege(p)==True

