__author__="Nightwish"
__title__="GM 处理工具"


import re,time
from functools import partial
# add_item item_id, num 是一个增加道具的GM指令，如果我们想增加1001~1003这几个道具各10个，需要这么执行3次，如果要加大量的道具，那执行的次数就更多了

# add_item {{1001 to 1003}},10
# 解析为：
# add_item 1001,10
# add_item 1002,10
# add_item 1003,10

# add_item {{1001,1003,1006}},10
# 解析为：
# add_item 1001,10
# add_item 1003,10
# add_item 1006,10

# add_item {{1001 to 1005 not 1002,1003}},10
# 解析为：
# add_item 1001,10
# add_item 1004,10
# add_item 1005,10
s=r"add_item {{1001 to 1005 not 1002,1003}},10"
p1=r"{{.+}}"
pattern1=re.compile(p1)
mattern=re.search(pattern1,s)

prop_cmd=input("道具命令:").strip()
id_cmd=input("道具id:").strip()
num_cmd=input("数量:").strip()
class check_cmd():
    t = "to"
    n = "not"
    d = ","
    def check(self):
        if prop_cmd=="add_item":
            if self.n and self.t in id_cmd:
                self.check_id_t_d_n()
            elif self.t in id_cmd:
                self.check_id_t()
            else:
                self.check_id_d()
        else:
            print("命令不合法")



    def check_id_t(self):

        id_cmd_t=id_cmd.split(self.t)
        for i in range(int(id_cmd_t[0]),int(id_cmd_t[1])+1):
            L=[]
            L.append(i)
        return L
    def check_id_d(self):

        id_cmd_=id_cmd.split(self.d)
        for i in id_cmd_:
            L=[]
            L.append(int(i))
        return L

    def check_id_t_d_n(self):

        id_cmd_=re.split(r"to|,|not",id_cmd)
        for i in range(int(id_cmd_[0]),int(id_cmd_[1])+1):
            L=[]
            L.append(i)
        L_=L[2:]
        for i in L_:
            L.remove(int(L_(i)))

        return L


    def handle(self):
        M=self.check()
        for i in M:
            print("执行命令{} {},{}".format(prop_cmd,i,num_cmd))


s="1001 to 1003 not 1002,1003"
s2="1001,1003,1006"
s_=re.split(r"to|,|not",s)
print(s_)
print(s_[3])
