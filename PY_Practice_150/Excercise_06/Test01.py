# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-07-26"

import os,sys,time,datetime,calendar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit


def gy_test_7_1():
    return

def gy_test_7_2():
    return

if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit
    1 : gy_test_7_1
    2 : gy_test_7_2
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_7_1,
        "2" : gy_test_7_2,
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
