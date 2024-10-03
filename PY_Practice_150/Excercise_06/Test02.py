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



if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit,
    1 : gy_test_8_1(remove the duplicate)
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_8_1
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
