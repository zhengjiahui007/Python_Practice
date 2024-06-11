# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !usr/bin/env/ python3
# Date : 2024-06-11

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable


def gy_find(src:str,target:str,start:int = 0):
    return

def py_test_4_1():

    return None

def py_test_4_2():

    return None


if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_4_1.
    2.py_test_4_2.

    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_4_1,
        "2" : py_test_4_2,

    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()





