import tkinter,os
from selenium import webdriver

wb=webdriver.Chrome(executable_path="E:\Gitproject\Project\chromedriver.exe")

#默认广告书
ads_num_require=8


class TkWin():
    def __init__(self,title,size):
        """
        对创建窗口的2个参数进行初始化
        :param title:
        :param size:
        """
        self.title = title
        self.size = size

    def back_up(self):
        pass

    # def test_path(self):
    #     source ="E:\Gitproject\Project\config"
    #     target_path ="E:\Gitproject\Project\Module"
    #     import time
    #     today_dir =target_path+time.strftime("%Y%m%d")
    #     second_dir =time.strftime("%H%M%S")
    #     time_dir =today_dir+os.sep+"a"+os.sep+second_dir+".zip"
    #     print(time_dir)
    #     #os.mkdir(today_dir)
    #     return today_dir

    def build_windows(self):
        """
        创建工具窗口
        :return:
        """
        global entry_url
        global entry_content
        global root
        root = tkinter.Tk()

        root.title(self.title)
        root.geometry(self.size)
        lb1_source = tkinter.Label(root,text = 'url')
        lb1_source.grid(row=0,column=0)
        entry_url = tkinter.Entry(root)
        entry_url.grid(row=0,column=1)


        lb1_target = tkinter.Label(root, text='search_content')
        lb1_target.grid(row=1, column=0)
        entry_content = tkinter.Entry(root)
        entry_content.grid(row=1, column=1)
        search_content=entry_content.get()

        but_back = tkinter.Button(root,text='open_url')
        but_back.grid(row=8,column=1)
        but_back['command'] = self.open_window

        but_back = tkinter.Button(root, text='search')
        but_back.grid(row=10, column=1)
        but_back['command'] = self.open_window_handle

        but_back = tkinter.Button(root, text='close')
        but_back.grid(row=12, column=1)
        but_back['command'] = self.quit_window
        root.mainloop()

    def open_window(self):
        """
        获取用户输入url 并调起 打开百度
        :return:
        """
        url=entry_url.get()
        wb.get(url)
        pass

    def open_window_handle(self):
        """
        获取用户输入 进行搜索
        :return:
        """
        content=entry_content.get()
        wb.find_element_by_id("kw").send_keys(content)
        wb.find_element_by_id("su").clear()
        pass


    def get__all__advert(self):
        all_adv_li=wb.find_element_by_css_selector('#e_idea_pp li')
        pass

    def quit_window(self):
        """
        关闭工具和浏览器
        :return:
        """
        root.quit()
        wb.close()
        pass


t=TkWin("Tool","400x400")
t.build_windows()







