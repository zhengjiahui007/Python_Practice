# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3
# __Date__ : "2025-01-04"

#_*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3
# __Date__ : "2025-01-04"

import turtle

def gy_draw_square(pen_size:int,pen_color:str,len0:int,angle0:int,len1:int,angle1:int,len2:int,angle2:int,len3:int,angle3:int,keep_win:bool = True):
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.forward(len0)
    turtle.right(angle0)
    turtle.forward(len1)
    turtle.right(angle1)
    turtle.forward(len2)
    turtle.right(angle2)
    turtle.forward(len3)
    turtle.right(angle3)
    if keep_win:
        turtle.mainloop()
    return

if ("__main__" == __name__):
    print("Draw a square : ")
    gy_draw_square(4,'red',100,40,100,60,100,90,190,100)
