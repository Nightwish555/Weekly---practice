#os.sep 根据系统不同处理/ \
#os.path.exists()
# 要备份的文件夹：source = ["/../"]
#
# 保存备份信息的文件夹：target_dir = "/.../"
#
# 文件夹名(日期)： today_dir = target_dir + time.strftime('%Y%m%d')
#
# 文件名(时间)：time_dir = time.strftime('%H%M%S')
#
# 检查文件夹命令：os.path.exist(today_dir)
#
# 文件夹路径：file_zip = today_dir + os.sep + time_dir + '.zip'
#
# 创建压缩文件命令： cmd = "zip -qr " + file_zip + ' ' + ' '.join(source)


# if 今天日期文件夹存在:
#     创建时间压缩文件
# else:
#     创建今日日期文件夹
#     创建时间压缩文件


import os
import time
#基本变量
source = ["/.../"]
target_dir = "/.../"

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime("%H%M%S")

file_zip = today_dir + os.sep + time_dir + '.zip'
cmd = "zip -qr " + file_zip +' '+ ' '.join(source)

#逻辑思路判断
if os.path.exists(today_dir)==0:
    os.mkdir(today_dir)
if os.system(cmd)==0:
    print("backup pass")
else:
    print("backup Failed")