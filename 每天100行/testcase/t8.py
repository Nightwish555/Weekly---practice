__author__="Nightwish"
__title__="命令行工具"

import os,time
from functools import partial
import subprocess
import prettytable as pt
import subprocess

trunk_folder = 'E:/NZ'
trunk_client = 'E:/NZ/Brines/TGame.exe'
class svn_tool():
    def windows_tool(self):
        global num
        tb=pt.PrettyTable()
        tb.field_names=(["ID","指令"])
        tb.add_column([1,"SVN更新主干"])
        tb.add_column([2,"SVN还原主干"])
        tb.add_column([3,"启动游戏客户端"])
        tb.add_column([4,"打开主干目录"])
        num=input("选择指令：").strip()
        self.run_tool()

    def run_tool(self):
        if num==1:
            self.svn_update()
        elif num==2:
            self.svn_revert()
        elif num==3:
            self.game_start()
        elif num==4:
            self.open_main()
        else:
            print("无此命令格式")


    def svn_update(self):
        subprocess.Popen(r'TortoiseProc.exe /command:update /path:"" /closeonend:0')
    def svn_revert(self):
        subprocess.Popen(r'TortoiseProc.exe /command:revert /path:"" /closeonend:0')
    def game_start(self):
        os.startfile("trunk_client")
    def open_main(self):
        os.startfile(trunk_folder)

if __name__ == '__main__':
    svn_tool=svn_tool()
    svn_tool.windows_tool()