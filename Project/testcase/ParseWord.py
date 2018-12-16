
class ParseWord():
    def __init__(self,s):
        self.s = s
        self.l = len(self.s)

    def find_index(self,n):
        for i in range(self.l):
            if self.s[i] == n:
                return i

    def get_word(self):
        s = self.finds('[')
        e = self.finds(']')
        name = self.s[s+1+1:e-1] # 去掉引号，取nama
        print(name)



# name = '["name"]'
# name1 = 'asdfas["name"]asdfasd'
# s = ParseWord(name1)
# s.getname()

h = ["a","b","c","d"]
s = h[0] + '+' + h[1] + '+' + h[2] + '+' + h[3]
s1 = '+'.join(h)
print(s1)

import tkinter
root = tkinter.Tk()
root.title('BackUp')
root.geometry("800x600")

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
