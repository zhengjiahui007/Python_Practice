#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# !__author__ : "Garry Zheng"
# Date: 2024-05-31

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR1 is {BASE_DIR}")
sys.path.append(BASE_DIR)
from Test_com import py_test_exit


def py_test_2_2_1():
    gy_range_list = [range(3,20,4),range(10,-3,-4),range(10,5),range(2,12)]
    for gy_list in gy_range_list:
        for i in gy_list:
            print(i,end = ",")
        print(" ")
    return None

def py_test_2_2_2():
    gy_range_list = [1,3,5,2,7,9]
    for gy_list_index in range(0,len(gy_range_list),1):
        if (gy_list_index == (len(gy_range_list) - 1)):
            print(gy_range_list[gy_list_index])
        else:
            print(gy_range_list[gy_list_index],end = ",")
    print(" ")

    for gy_list_index in range(-1,-len(gy_range_list) - 1,-1):
        if (gy_list_index == (-len(gy_range_list))):
            print(gy_range_list[gy_list_index])
        else:
            print(gy_range_list[gy_list_index],end = ",")
    print(" ")

    gy_range_list = [1,3,5,2,7,9]
    for gy_list_index in range(0,len(gy_range_list),1):
        if (0 == (gy_range_list[gy_list_index] % 2)):
            print(gy_range_list[gy_list_index],end = " ")
    print(" ")

    gy_range_list = [1,3,5,2,7,9]
    for gy_list_index in range(0,len(gy_range_list),1):
        if (3 < gy_range_list[gy_list_index]) and (1 == (gy_range_list[gy_list_index] % 2)):
            print(gy_range_list[gy_list_index],end = " ")
    print(" ")
    return None

def py_test_2_2_3():
    gy_dict_lesson = {
        'python' : 90,
        'java'   : 95,
        'PHP'    : 85
    }
    for i_key in gy_dict_lesson:
        print(i_key," : ",gy_dict_lesson[i_key])
    print("*********************************")
    for i_key,i_value in gy_dict_lesson.items():
        print(i_key," : ",i_value)
    return None

def py_test_2_2_5():
    gy_range_list = [1,3,5,2,7,9,10]
    for i_val in gy_range_list:
        if (0 == i_val % 2):
            print(i_val)
            break
    return None

def py_test_2_2_6():
    gy_range_list = [3,6,1,8,1,9,2]
    max_val = gy_range_list[0]
    for i_val in gy_range_list:
        if max_val < i_val:
            max_val = i_val
    print("The max value in {} is {} .".format(gy_range_list,max_val))

    min_val = gy_range_list[0]
    for i_val in gy_range_list:
        if min_val > i_val:
            min_val = i_val
    print("The min value in {} is {} .".format(gy_range_list,min_val))

    gy_even_list = []
    for i_val in gy_range_list:
        if (0 == i_val % 2):
            gy_even_list.append(i_val)

    min_val = gy_even_list[0]
    for i_val in gy_even_list:
        if min_val > i_val:
            min_val = i_val
    print("The min even value in {} is {} .".format(gy_range_list,min_val))

    gy_odd_list = []
    for i_val in gy_range_list:
        if (1 == i_val % 2):
            gy_odd_list.append(i_val)

    max_val = gy_odd_list[0]
    for i_val in gy_odd_list:
        if max_val < i_val:
            max_val = i_val
    print("The max even value in {} is {} .".format(gy_range_list,max_val))
    return None

def py_test_2_2_7():
    gy_range_list_0 = [3,6,1,8,1,9,2]
    gy_range_list_1 = [3,1,2,6,4,8,7]
    for i_0 in gy_range_list_0:
        for i_1 in gy_range_list_1:
            if (10 == (i_0 + i_1)):
                print((i_0,i_1))

    print("*********************************")
    for i_0 in gy_range_list_0:
        for i_1 in gy_range_list_1:
            if (2 == abs(i_0 - i_1)):
                print((i_0,i_1))

    print("*********************************")
    max_val = gy_range_list_0[0] * gy_range_list_1[0]
    for i_0 in gy_range_list_0:
        for i_1 in gy_range_list_1:
            if (max_val < (i_0 * i_1)):
                max_val = (i_0 * i_1)
    print(max_val)
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_2_1.
    2.py_test_2_2_2.
    3.py_test_2_2_3.
    4.py_test_2_2_5.
    5.py_test_2_2_6.
    6.py_test_2_2_7
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_2_1,
        "2" : py_test_2_2_2,
        "3" : py_test_2_2_3,
        "4" : py_test_2_2_5,
        "5" : py_test_2_2_6,
        "6" : py_test_2_2_7
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()
