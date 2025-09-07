# -*- coding : utf-8 -*-
# __author__ : GarryZheng
# !/usr/bin/env python3
# __Date__ : 2025-09-06


import tkinter,math,os,sys
from functools import partial

class GZ_Calculator:
    def __init__(self,title:str,x:int,y:int,w:int,h:int) -> None:
        self.ptitle = title
        self.px = x
        self.py = y
        self.pw = w
        self.ph = h
        self.root_sc = tkinter.Tk()
        self.root_sc.title(title)
        self.root_sc.minsize(w,h)
        self.gz_cal_screen()
        return None

    def gz_cal_show(self):
        self.root_sc.mainloop()
        return None

    def gz_cal_pressOperator(self,oper:str) -> None:
        print("gz_cal_pressOperator : ",oper)
        return None

    def gz_cal_screen(self):
        # layout 
        # --Text label , 在 Python 的 tkinter 模块中，textvariable 是一个用于动态绑定控件文本内容的参数
        gz_CurrentShow = tkinter.StringVar()
        gz_CurrentShow.set('0')
        label = tkinter.Label(self.root_sc,textvariable = gz_CurrentShow, anchor='e', bd=5, fg='black', font=('Arial',20))
        label.place(x = 20,y = 10,width = 460,height = 65)

        button_bg = '#666'
        button_bd = 2
        button_w = 87
        button_h = 65
        button_x = 20
        button_w_interval = 92
        button_h_interval = button_h + 5
        # line 1
        button1_txt_lst = ["MC","MR","MS","M+","M-"]
        button1_1_y = 65

        for b_txt in button1_txt_lst:
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button1_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval

        # line 2
        button2_txt_lst = ["del","CE","C","+/-","sqt"]
        button_x = 20
        button2_1_y = button1_1_y + button_h_interval
        for b_txt in button2_txt_lst:
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button2_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 3
        button3_txt_lst = ["7","8","9","/","%"]
        button_x = 20
        button3_1_y = button2_1_y + button_h_interval
        for b_txt_i in range(0,len(button3_txt_lst),1):
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
            else:
                button_bg = '#708069'
            b_txt = button3_txt_lst[b_txt_i]
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button3_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval

        # line 4
        button4_txt_lst = ["4","5","6","*","1/x"]
        button_x = 20
        button4_1_y = button3_1_y + button_h_interval
        for b_txt_i in range(0,len(button4_txt_lst),1):
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
            else:
                button_bg = '#708069'
            b_txt = button4_txt_lst[b_txt_i]
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button4_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 5
        button5_txt_lst = ["3","2","1","-","="]
        button_x = 20
        button5_1_y = button4_1_y + button_h_interval
        for b_txt_i in range(0,len(button5_txt_lst),1):
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
            else:
                button_bg = '#708069'
            b_txt = button5_txt_lst[b_txt_i]
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button5_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 6
        button6_txt_lst = ["0",".","+"]
        button_x = 20
        button6_1_y = button5_1_y + button_h_interval
        for b_txt_i in range(0,len(button6_txt_lst),1):
            if(0 >= b_txt_i):
                button_bg = '#bbbbbb'
                button_w = 3 * button_w + 10
            else:
                button_bg = '#708069'
                button_w = 87
            b_txt = button6_txt_lst[b_txt_i]
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = partial(self.gz_cal_pressOperator,b_txt))
            button1.place(x = button_x, y = button6_1_y, width = button_w, height = button_h)
            if(0 >= b_txt_i):
                button_x = button_x + button_w_interval * 3
            else:
                button_x = button_x + button_w_interval
        return None




if __name__ == "__main__":
    gz_cal_0 = GZ_Calculator("Cal",200,200,500,500)
    gz_cal_0.gz_cal_show()