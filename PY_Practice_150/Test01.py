# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3

import os,sys,time,math
from Test_com import py_test_exit

def py_test_1_1_1():
    ## == 用来比较两个变量的值是否相等，而 is 则用来比对两个变量引用的是否是同一个对象
    print((4.0 == 4),type(4.0),type(4))
    print("4.0" == 4)
    print(bool("1"),bool("0"))
    print(str(32))
    print(int(6.26))
    print(float(32))
    print(float("3.21"))
    print(int("434"))
    # print(int("3.42"))
    print(bool(-1))
    print(bool(""))
    print(bool(0))
    print("wrqq" > "acd")
    print("ttt" == "ttt ")
    print("sd" * 3)
    print("wer" + "2322")
    return None

def py_test_1_1_2():
    print('The type of "True" is ',type("True"))
    print('The type of "False" is ',type("False"))
    print('The type of 4 >= 5 is ',type(4 >= 5))
    print('The type of 5 is ',type(5))
    print('The type of 5.0 is ',type(5.0))
    print('The type of True is ',type(True))
    return None

def py_test_1_1_3():
    print(' 3的5次方 is ',3**5)
    print(' 7对2求模 is ',7%2)
    print(' 9除5,要求有⼩数部分 is ',9/5)
    print(' 9除5,要求没有⼩数部分 is ',9//5)
    print(' ⽤程序计算根号16,也就是16的2分之⼀次⽅ is ',16 ** 0.5)
    print(' ⽤函数计算根号16,也就是16的2分之⼀次⽅ is ',math.sqrt(16))
    return None


if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_1_1.
    2.py_test_1_1_2.
    3.py_test_1_1_3.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_1_1,
        "2" : py_test_1_1_2,
        "3" : py_test_1_1_3
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()




















