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
from enum import Enum,unique
from math import sqrt
from random import randint

@unique
class Gy_color(Enum):
    gy_Red = (255,0,0)
    gy_Green = (0,255,0)
    gy_Blue = (0,0,255)
    gy_Black = (0,0,0)
    gy_White = (255,255,255)
    gy_Grey = (242,242,242)

    @staticmethod
    def gy_random_color() -> tuple:
        gy_red = randint(0,255)
        gy_green = randint(0,255)
        gy_blue = randint(0,255)
        return (gy_red,gy_green,gy_blue)

class GY_Ball(object):
    def __init__(self,x,y,radius,sx,sy,color = Gy_color.gy_Red) -> None:
        self.gy_x = x
        self.gy_y = y
        self.gy_r = radius
        self.gy_sx = sx
        self.gy_sy = sy
        self.gy_color = color
        self.gy_alive = True
        return

    def gy_move(self,screen) -> None:
        self.gy_x += self.gy_sx
        self.gy_y += self.gy_sy
        return

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

def gy_ballmove_main():
    pygame.init()
    gy_screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Big ball eats small ball!")
    gy_ball = GY_Ball(50,50,20,10,5,Gy_color.gy_random_color())
    gy_running = True
    while gy_running:
        for gy_event in pygame.event.get():
            #print("The event type is = {}".format(gy_event.type))
            if (pygame.QUIT == gy_event.type):
                gy_running = False
        gy_screen.fill((242,242,242))
        pygame.draw.circle(gy_screen,gy_ball.gy_color,(gy_ball.gy_x,gy_ball.gy_y),gy_ball.gy_r,0)
        pygame.display.flip()
        pygame.time.delay(500)
        gy_ball.gy_move(gy_screen)

    return

if "__main__" == __name__:
    #gy_main()
    #gy_py_main()
    #gy_pymove_main()
    gy_ballmove_main()

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