import tkinter
import os
import time
def backup():
    #global entry_source
    #global entry_target
    source = entry_source.get()
    target_dir = entry_target.get()
    print(type(target_dir))
    today_dir = target_dir + time.strftime('%Y%m%d')
    time_dir = time.strftime("%H%M%S")

    #只能用于linux
    zip_file = today_dir + os.sep + time_dir + '.zip'
    #zip_cmd = "zip -qr " + zip_file +' '+ source
    zip_cmd ="tasklist11 |findstr cmd"
    print(zip_cmd)
    print(source) #打印的是视图1的文本
    print(target_dir) #打印视图2
    if os.path.exists(today_dir)==0:
        os.mkdir(today_dir)
    print(os.system(zip_cmd))
    if os.system(zip_cmd)==0:
        print("Success backup Up")
    else:
        print("Failed backup")

#从这里开始呢，则是开始界面的编写及布局
root = tkinter.Tk()
root.title('BackUp')
root.geometry("200x200")
#第一行的两个控件
lbl_source = tkinter.Label(root, text='Source')
lbl_source.grid(row=0, column=0)
entry_source = tkinter.Entry(root)
entry_source.grid(row=0,column=1)
#第二行的两个控件
lbl_target = tkinter.Label(root, text='Target')
lbl_target.grid(row=1, column=0)
entry_target = tkinter.Entry(root)
entry_target.grid(row=1,column=1)
#第三行的一个按钮控件
but_back = tkinter.Button(root,text='BackUp')
but_back.grid(row=3, column=0)
but_back["command"] = backup
#界面的开始
root.mainloop()