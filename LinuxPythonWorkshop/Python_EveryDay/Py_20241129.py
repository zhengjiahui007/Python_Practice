# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
# !usr/bin/env python3
# __Date__ : "2025-02-20"

import tkinter
import tkinter.messagebox

Gy_flag = True
Gy_top = tkinter.Tk()
Gy_label = tkinter.Label(Gy_top,text = 'Hello,world!',font = 'Arial-32',fg = 'red')

def gy_change_label_text():
    global Gy_flag
    Gy_flag = not Gy_flag
    gy_color,gy_msg = ('red','Hello world!') if Gy_flag else ('blue','Goodbye world!')
    Gy_label.config(text = gy_msg,fg = gy_color)
    return

def gy_confirm_to_quit():
    if tkinter.messagebox.askokcancel('Warm Hint','Confirm to exit?'):
        Gy_top.quit()
    return

def gy_main():
    Gy_flag = True
    Gy_top.geometry('500x500')
    Gy_top.title('Small Game')
    Gy_label.pack(expand = 1)
    gy_panel = tkinter.Frame(Gy_top)
    button1 = tkinter.Button(gy_panel,text = 'Change',command = gy_change_label_text)
    button1.pack(side = 'left')
    button2 = tkinter.Button(gy_panel,text = 'Exit',command = gy_confirm_to_quit)
    button2.pack(side = 'right')
    gy_panel.pack(side = 'bottom')
    tkinter.mainloop()

if "__main__" == __name__:
    gy_main()

'''
def gy_main():
    gy_flag = True

    def gy_change_label_text():
        nonlocal gy_flag
        gy_flag = not gy_flag
        gy_color,gy_msg = ('red','Hello world!') if gy_flag else ('blue','Goodbye world!')
        label.config(text=gy_msg,fg=gy_color)
        return

    def gy_confirm_to_quit():
        if tkinter.messagebox.askokcancel('Warm Hint','Confirm to exit?'):
            top.quit()
        return
    
    top = tkinter.Tk()
    top.geometry('2400x1600')
    top.title('Small Game')
    label = tkinter.Label(top,text = 'Hello,world!',font = 'Arial-32',fg = 'red')
    label.pack(expand = 1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text = 'Change',command = gy_change_label_text)
    button1.pack(side = 'left')
    button2 = tkinter.Button(panel,text = 'Exit',command = gy_confirm_to_quit)
    button2.pack(side = 'right')
    panel.pack(side = 'bottom')
    tkinter.mainloop()

if "__main__" == __name__:
    gy_main()
'''