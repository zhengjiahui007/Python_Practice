# -*-coding : utf-8-*-
# !usr/bin/env/ python3
# __author__ : "Garry Zheng"
# __Date__ : 2024-07-21

import os,time,sys,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Test_com import py_test_exit
from collections.abc import Iterable

def py_test_sort_1():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    for i_count in range(0,len(gy_lst),1):
        for i in range(0,len(gy_lst) - i_count - 1,1):
            if (gy_lst[i] > gy_lst[i + 1]):
                gy_lst[i],gy_lst[i + 1] = gy_lst[i + 1],gy_lst[i]
    print("gy_lst = ",gy_lst)
    return

def py_test_sort_2():
    return

def py_test_sort_3():
    return

def py_test_sort_4():
    return

def py_test_sort_5():
    return

def py_test_sort_6():
    return

def py_test_sort_7():
    return

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_sort_1.(pop sort)
    2.py_test_sort_2.(quick sort)
    3.py_test_sort_3.(insert sort)
    4.py_test_sort_4.(Shell's sort)
    5.py_test_sort_5.(merge sort)
    6.py_test_sort_6.(select sort)
    7.py_test_sort_7.(heap sort)
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_sort_1,
        "2" : py_test_sort_2,
        "3" : py_test_sort_3,
        "4" : py_test_sort_4,
        "5" : py_test_sort_5,
        "6" : py_test_sort_6,
        "7" : py_test_sort_7
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()