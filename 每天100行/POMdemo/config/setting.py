__author__="Nightwish"
__title__="配置路径类"

import os
class Setting():
    current_path=os.path.abspath(os.path.dirname(__file__))
    print(current_path)

