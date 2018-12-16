import tkinter,os

class TkWin():
    def __init__(self,title = 'title',size = '200x200'):
        self.title = title
        self.size = size

    def back_up(self):
        pass

    def test_path(self):
        source ="E:\Gitproject\Project\config"
        target_path ="E:\Gitproject\Project\Module"
        import time
        today_dir =target_path+time.strftime("%Y%m%d")
        second_dir =time.strftime("%H%M%S")
        time_dir =today_dir+os.sep+"a"+os.sep+second_dir+".zip"
        print(time_dir)
        #os.mkdir(today_dir)
        return today_dir

    def run(self):
        root = tkinter.Tk()
        root.title(self.title)
        root.geometry(self.size)
        lb1_source = tkinter.Label(root,text = 'Source')
        lb1_source.grid(row=0,column=0)
        entry_source = tkinter.Entry(root)
        entry_source.grid(row=0,column=1)

        lb1_target = tkinter.Label(root, text='Target')
        lb1_target.grid(row=1, column=0)
        entry_source = tkinter.Entry(root)
        entry_source.grid(row=1, column=1)

        but_back = tkinter.Button(root,text='BackUp')
        but_back.grid(row=3,column=0)
        but_back['command'] = self.back_up

        root.mainloop()


title = 'Backup'
size = '800x600'
w = TkWin(title)
w.test_path()

