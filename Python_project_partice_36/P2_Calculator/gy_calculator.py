
# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3
# __Date__ : 2025-08-25


import tkinter,math

'''
root = tkinter.Tk()
root.resizable(width=False, height=False)

# 是否按下了运算符
IS_CALC = False
# 存储数字
STORAGE = []
# 显示框最多显示多少个字符
MAXSHOWLEN = 18
# 当前显示的数字
CurrentShow = tkinter.StringVar()
CurrentShow.set('0')
'''


'''
root.minsize(320, 420)
root.title('Calculator')
# 布局
# --文本框
label = tkinter.Label(root, textvariable=CurrentShow, bg='black', anchor='e', bd=5, fg='white', font=('楷体', 20))
label.place(x=20, y=50, width=280, height=50)
'''

class GY_Calculator:
    def __init__(self,title:str,x:int,y:int,w:int,h:int) -> None:
        self.ptitle = title
        self.px = x
        self.py = y
        self.pw = w
        self.ph = h
        self.root_sc = tkinter.Tk()
        self.root_sc.title(title)
        #self.root_sc.minsize(w,h)
        #self.CurrentShow = tkinter.StringVar()
        #self.CurrentShow.set('0')
        return None

    def gy_button_print(self):
        print("gy_button_print !")
        return None

    def gy_cal_demo(self):
        gy_label = tkinter.Label(self.root_sc,bg='green',anchor='e', bd=5, fg='white', font=('楷体', 20))
        gy_label.place(x=20, y=50, width=280, height=50)
        button1_1 = tkinter.Button(self.root_sc,text='MC', bg='#666', bd=2,command=self.gy_button_print)
        button1_1.place(x=0, y=0, width=50, height=35)
        return None

    def gy_button2_print(self):
        print("gy_button_print 2!")
        return None

    def gy_second_win(self):
        gy_win_2 = tkinter.Toplevel(self.root_sc)
        gy_win_2.title("Second WIN")
        gy_label = tkinter.Label(gy_win_2,text = "The second Win!",bg='white',anchor='e', bd=5, fg='white', font=('楷体', 20))
        gy_label.place(x=20, y=50, width=280, height=50)
        button2_1 = tkinter.Button(gy_win_2,text = "Test", command = self.gy_button2_print)
        button2_1.place(x=0, y=0, width=50, height=35)
        return None

    def gy_win_show(self):
        self.root_sc.mainloop()
        return None

if "__main__" == __name__:
    gy_calu_0 = GY_Calculator("GY CALCU",100,100,500,500)
    gy_calu_0.gy_cal_demo()
    gy_calu_0.gy_second_win()
    gy_calu_0.gy_win_show()



