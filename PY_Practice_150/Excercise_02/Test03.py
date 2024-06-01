# !/usr/bin/env python3
# -*- coding : utf-8 -*-
# !__author__ : "GarryZheng"
# Date : 2024-06-01

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit

def py_test_2_3_1():
    while True:
        gy_input_str = input("Please input an integer : ")
        if gy_input_str.isdigit():
            gy_input_int = int(gy_input_str)
            print("Your input {val} is {flag} integer !".format(val = gy_input_int,flag = "an even" if (0 == gy_input_int % 2) else "an odd"))
        else:
            if ("quit" == gy_input_str):
                break
            else:
                print("Your input is wrong ! Please input again !")
                continue
    return None

def py_test_2_3_2():
    gy_lst = [2,3,4]
    for i_val in gy_lst:
        while True:
            print("Please input an integer which is Multiple of %d : " %(i_val),end = " ")
            gy_input_str = input("")
            if gy_input_str.isdigit():
                gy_input_int = int(gy_input_str)
                print("Your input {val} is {flag} !".format(val = gy_input_int,flag = "correct" if (0 == gy_input_int % i_val) else "wrong"))
            else:
                if ("quit" == gy_input_str):
                    break
                else:
                    print("Your input is wrong ! Please input again !")
                    continue
    return None

def py_test_2_3_3():
    while True:
        gy_input_str = input("Please input an integer : ")
        if gy_input_str.isdigit():
            gy_input_int = int(gy_input_str)
            if (10 > gy_input_int):
                print("Your input {val} is {flag} integer !".format(val = gy_input_int,flag = "an even" if (0 == gy_input_int % 2) else "an odd"))
            else:
                print("Your input {} is greater than 10 , not judge odd - even !".format(gy_input_int))
        else:
            if ("quit" == gy_input_str):
                break
            else:
                print("Your input is wrong ! Please input again !")
                continue
    return None

if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_3_1.
    2.py_test_2_3_2.
    3.py_test_2_3_3.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_3_1,
        "2" : py_test_2_3_2,
        "3" : py_test_2_3_3
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()