__author__="Nightwish"
__title__="命令行工具"

import enum
import configparser
import os,time
from functools import partial
import subprocess
import prettytable as pt
import subprocess
from config.setting import Setting

set=Setting()

cf=configparser.ConfigParser()
cf.read(set.current_path+os.sep+"config.ini")
trunk_folder=cf.get("tool_svn","trunk_folder")
trunk_client = r'E:/Nz_/Brines/TGameRelease - client-A-D.exe'
class svn_tool():
    def windows_tool(self):
        global num
        tb=pt.PrettyTable()
        tb.field_names=(["ID","指令"])
        tb.add_row(["1","SVN更新主干"])
        tb.add_row(["2","SVN还原主干"])
        tb.add_row(["3","启动游戏客户端"])
        tb.add_row(["4","打开主干目录"])
        print(tb)
        num=input("选择指令：").strip()
        self.run_tool()

    def run_tool(self):
        if int(num)==1:
            self.svn_update()
        elif int(num)==2:
            self.svn_revert()
        elif int(num)==3:
            self.game_start()
        elif int(num)==4:
            self.open_main()
        else:
            print("无此命令格式")
            self.windows_tool()


    def svn_update(self):
        subprocess.Popen(r'TortoiseProc.exe /command:update '+'/path:'+trunk_folder+'/closeonend:0')
    def svn_revert(self):
        subprocess.Popen(r'TortoiseProc.exe /command:revert '+'/path:'+trunk_folder+' /closeonend:0')
    def game_start(self):
        subprocess.Popen(trunk_client)
    def open_main(self):
        os.startfile(trunk_folder)

if __name__ == '__main__':
    svn_tool=svn_tool()
    svn_tool.windows_tool()
    # print(enum.__file__)
