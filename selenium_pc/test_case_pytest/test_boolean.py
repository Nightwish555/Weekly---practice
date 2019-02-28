
#import pytest
import os
debug =False

# from genericpath import exists
#
# def exists(path):
#     try:
#         os.stat(path)
#     except OSError:
#         return False
#     return 111

#from temp.path_test import get_dir_src_filename
#from Conf.Setting import Setting as sett

print(sett().temp_path+"__init__.py")

class TestBoolean():

    def setup_class(self):
        if debug:print(1)

    def test_exist_file(self):
        file_name =os.path.exists(sett().temp_path+"__init__.py")
        assert file_name == True

    def test_obj_bool(self):
        w = list(i for i in ["", None, 0, -1])
        for i in w:
            if debug:print(i, "=", bool(i))
            if not i:
                assert not i
            else:
                assert i
