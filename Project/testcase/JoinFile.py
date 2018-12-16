#coding:utf-8
import os
dir = os.path.abspath(os.path.dirname(__file__))
config = dir + './../config6'
#E:\Gitproject\Project\config2
class JoinFile():

    #Text ="1"
    def __init__(self,flag = False):
        self.flag = flag
        self.Text = "1"
        #self.Text = Text

    def make_dir(self):
        self.flag = os.path.exists(config)
        print(self.flag)
        text = "1"
        if self.flag:
            print('目录已存在')
        else:
            #os.path.join(a,)
            os.mkdir(os.path.join(config+str(text)))
            print(JoinFile().Text)

c = JoinFile()
c.make_dir()