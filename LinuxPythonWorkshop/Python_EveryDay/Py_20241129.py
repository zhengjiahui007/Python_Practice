# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
# !usr/bin/env python3
# __Date__ : "2025-02-20"

'''
use the tkinter GUI
'''
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

'''
use the Pygame
'''
import pygame,random

def gy_py_main():
    print(pygame.__version__)
    pygame.init()
    gy_screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Big ball eats small ball!")
    gy_screen.fill((242,242,242))
    # pygame.draw.circle(gy_screen,(255,0,0,),(100,100),30,0)
    gy_ball_image = pygame.image.load('./pic_file/ball.png')
    gy_screen.blit(gy_ball_image,(100,100))
    pygame.display.flip()
    gy_running = True
    while gy_running:
        for gy_event in pygame.event.get():
            #print("The event type is = {}".format(gy_event.type))
            if (pygame.QUIT == gy_event.type):
                gy_running = False
    return

def gy_pymove_main():
    print(pygame.__version__)
    pygame.init()
    gy_screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Big ball eats small ball!")
    gy_x,gy_y = 50,50
    gy_running = True
    while gy_running:
        for gy_event in pygame.event.get():
            #print("The event type is = {}".format(gy_event.type))
            if (pygame.QUIT == gy_event.type):
                gy_running = False
        gy_screen.fill((242,242,242))
        pygame.draw.circle(gy_screen,(0,0,255),(gy_x,gy_y),30,0)
        gy_x,gy_y = 50,50
        pygame.display.flip()
        pygame.time.delay(500)
        gy_num_x = random.randint(0,600)
        gy_num_y = random.randint(0,500)
        gy_x,gy_y = gy_x + gy_num_x,gy_y + gy_num_y

    return

if "__main__" == __name__:
    #gy_main()
    #gy_py_main()
    gy_pymove_main()

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