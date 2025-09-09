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
        self.max_show_len = 18
        self.is_calc = False
        self.gz_storage = []
        self.gz_CurrentShow = tkinter.StringVar()
        self.gz_CurrentShow.set('0')
        self.gz_cal_screen()
        return None

    '''clean all'''
    def gz_cal_clearAll(self):
        self.is_calc = False
        self.gz_storage.clear()
        self.gz_CurrentShow.set('0')
        return None

    '''clean one'''
    def gz_cal_clearOne(self) -> None:
        if self.is_calc:
            self.is_calc = False
            self.gz_storage.clear()
            self.gz_CurrentShow.set('0')

        if ('0' != self.gz_CurrentShow.get()):
            if (len(self.gz_CurrentShow.get()) > 1):
                self.gz_CurrentShow.set(self.gz_CurrentShow.get()[0 : -1 : 1])
            else:
                self.gz_CurrentShow.set('0')
        return None

    '''clean all number'''
    def gz_cal_clearCurrent(self) -> None:
        self.gz_CurrentShow.set('0')
        return None

    def gz_cal_show(self) -> None:
        self.root_sc.mainloop()
        return None

    def gz_cal_pressOperator(self,oper:str) -> None:
        print("gz_cal_pressOperator : ",oper)
        return None

    def gz_cal_pressNumber(self,number:str) -> None:
        if self.is_calc:
            self.gz_CurrentShow.set('0')
            self.is_calc = False
        if self.gz_CurrentShow.get() == '0':
            self.gz_CurrentShow.set(number)
        else:
            if len(self.gz_CurrentShow.get()) < self.max_show_len:
                self.gz_CurrentShow.set(self.gz_CurrentShow.get() + number)
        return None


    def gz_cal_screen(self):
        # layout 
        # --Text label , 在 Python 的 tkinter 模块中，textvariable 是一个用于动态绑定控件文本内容的参数
        # 当前显示的数字
        label = tkinter.Label(self.root_sc,textvariable = self.gz_CurrentShow, anchor='e', bd=5, fg='black', font=('Arial',20),width = self.max_show_len)
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
            command_button = None
            if ("C" == b_txt):
                command_button = partial(self.gz_cal_clearAll)
            elif ("del" == b_txt):
                command_button = partial(self.gz_cal_clearOne)
            elif ("CE" == b_txt):
                command_button = partial(self.gz_cal_clearCurrent)
            else:
                command_button = partial(self.gz_cal_pressOperator,b_txt)

            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = command_button)
            button1.place(x = button_x, y = button2_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 3
        button3_txt_lst = ["7","8","9","/","%"]
        button_x = 20
        button3_1_y = button2_1_y + button_h_interval
        for b_txt_i in range(0,len(button3_txt_lst),1):
            b_txt = button3_txt_lst[b_txt_i]
            command_button = None
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
                command_button = partial(self.gz_cal_pressNumber,b_txt)
            else:
                button_bg = '#708069'
                command_button = partial(self.gz_cal_pressOperator,b_txt)
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = command_button)
            button1.place(x = button_x, y = button3_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval

        # line 4
        button4_txt_lst = ["4","5","6","X","1/x"]
        button_x = 20
        button4_1_y = button3_1_y + button_h_interval
        for b_txt_i in range(0,len(button4_txt_lst),1):
            b_txt = button4_txt_lst[b_txt_i]
            command_button = None
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
                command_button = partial(self.gz_cal_pressNumber,b_txt)
            else:
                button_bg = '#708069'
                command_button = partial(self.gz_cal_pressOperator,b_txt)
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = command_button)
            button1.place(x = button_x, y = button4_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 5
        button5_txt_lst = ["3","2","1","-","="]
        button_x = 20
        button5_1_y = button4_1_y + button_h_interval
        for b_txt_i in range(0,len(button5_txt_lst),1):
            b_txt = button5_txt_lst[b_txt_i]
            command_button = None
            if(2 >= b_txt_i):
                button_bg = '#bbbbbb'
                command_button = partial(self.gz_cal_pressNumber,b_txt)
            else:
                button_bg = '#708069'
                command_button = partial(self.gz_cal_pressOperator,b_txt)
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = command_button)
            button1.place(x = button_x, y = button5_1_y, width = button_w, height = button_h)
            button_x = button_x + button_w_interval
        
        # line 6
        button6_txt_lst = ["0",".","+"]
        button_x = 20
        button6_1_y = button5_1_y + button_h_interval
        for b_txt_i in range(0,len(button6_txt_lst),1):
            b_txt = button6_txt_lst[b_txt_i]
            command_button = None
            if(0 >= b_txt_i):
                button_bg = '#bbbbbb'
                button_w = 3 * button_w + 10
                command_button = partial(self.gz_cal_pressNumber,b_txt)
            else:
                button_bg = '#708069'
                button_w = 87
                command_button = partial(self.gz_cal_pressOperator,b_txt)
            button1 = tkinter.Button(self.root_sc,text = b_txt, bg = button_bg, bd = button_bd,command = command_button)
            button1.place(x = button_x, y = button6_1_y, width = button_w, height = button_h)
            if(0 >= b_txt_i):
                button_x = button_x + button_w_interval * 3
            else:
                button_x = button_x + button_w_interval
        return None




if __name__ == "__main__":
    gz_cal_0 = GZ_Calculator("Cal",200,200,500,500)
    gz_cal_0.gz_cal_show()