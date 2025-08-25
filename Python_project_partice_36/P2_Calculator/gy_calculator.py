
# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3
# __Date__ : 2025-08-25


import tkinter,math

class GY_Calculator:
    def __init__(self,title:str,x:int,y:int,w:int,h:int) -> None:
        self.ptitle = title
        self.px = x
        self.py = y
        self.pw = w
        self.ph = h
        self.root_sc = tkinter.Tk()
        self.root_sc.title(title)
        self.root_sc.minsize(w,h)
        self.root_sc.mainloop()
        return None




if "__main__" == __name__:
    gy_calu_0 = GY_Calculator("GY CALCU",100,100,500,500)


