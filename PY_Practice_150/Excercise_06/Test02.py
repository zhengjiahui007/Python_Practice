# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-09-10"

import os,sys,time,datetime,calendar,re,pprint
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit


def gy_test_8_1():
    gy_lst = [0,0,0,0,2,2,3,3,3,3,3,3,4,4,4,7,7,8,8,9,11,11,11,11,11,11,11,13,13,14,14,15,15,15]
    gy_init_index = 0
    gy_lst_len = len(gy_lst)
    while(gy_init_index < gy_lst_len - 1):
        gy_lst_len = len(gy_lst)
        # print("gy_lst[{}] = {}".format(i,gy_lst[i]))
        print("gy_lst_len = ",gy_lst_len," gy_init_index = ",gy_init_index)
        for i in range(gy_init_index + 1,gy_lst_len,1):
            if (gy_lst[gy_init_index] == gy_lst[i]):
                del gy_lst[i]
                break
            else:
                gy_init_index += 1
                break
    print(" gy_lst = ",gy_lst)
    return

def combination_sum(gy_lst:list,gy_target:int):
    '''
    print(gy_lst,gy_target)
    gy_group_lst = []
    for i in gy_lst:
        if (i == gy_target):
            # print("i = ",i)
            gy_group_lst.append([i])
            print("1 gy_group_lst = ", gy_group_lst)
        elif (i > gy_target):
            continue
        else:
            gy_rest = gy_target - i
            gy_lst_rest = combination_sum(gy_lst,gy_rest)
            for tmp_lst in gy_lst_rest:
                tmp_lst.append(i)
            gy_group_lst.extend(gy_lst_rest)
            print("2 gy_group_lst = ", gy_group_lst)
    print(gy_group_lst)
    '''
    gy_group_lst = []
    for i in gy_lst:
        if (i == gy_target):
            gy_group_lst.append([i])
        elif (i > gy_target):
            continue
        else:
            gy_i_remainder = gy_target % i
            if  (0 == gy_i_remainder):
                gy_i_quotient = gy_target // i
                for 

    return gy_group_lst

def remove_duplicate(gy_lst:list):
    combination_set = set()
    for gy_item in gy_lst:
        gy_item.sort()
        combination_set.add(tuple(gy_item))
    return combination_set

def gy_test_8_2():
    gy_lst = [2,3,5]
    gy_set = remove_duplicate(combination_sum(gy_lst,8))
    for gy_i in gy_set:
        print("gy_i = ",gy_i)
    return


if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit,
    1 : gy_test_8_1(remove the duplicate)
    2 : gy_test_8_2(combination sum from a list)
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_8_1,
        "2" : gy_test_8_2
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
