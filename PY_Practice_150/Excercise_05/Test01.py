# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-07-11"

import os,sys,time,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable

###########################Print YangHui Triangle####################################################
'''
Please input an integer : 10
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
   1 6 15 20 15 6 1
  1 7 21 35 35 21 7 1
1 9 36 84 126 126 84 36 9 1

'''
def gy_print_Yanghui(lst:list,total_line:int):
    current_line = len(lst)
    print(" "*(total_line - current_line),end="")
    for i in range(0,len(lst),1):
        print(lst[i],end = " ")
    print()
    return None

def gy_yanghui_triangle_recursive(N_INT:int,N_Total:int):
    current_line_lst = []
    if (1 == N_INT):
        current_line_lst = [1]
    elif (2 == N_INT):
        current_line_lst = [1,1]
        gy_yanghui_triangle_recursive(N_INT - 1,N_Total)
    else:
        last_line_lst = gy_yanghui_triangle_recursive(N_INT - 1,N_Total)
        # print("last_line_lst = ",last_line_lst," N_INT = ",N_INT)
        for j in range(0,N_INT,1):
            if ((0 == j) or (j == (N_INT - 1))):
                current_line_lst.append(1)
            else:
                current_line_lst.append(last_line_lst[j - 1] + last_line_lst[j])
    # print("current_line_lst = ",current_line_lst)
    gy_print_Yanghui(current_line_lst,N_Total)
    return current_line_lst

def gy_test_6_1():
    gy_N_str = input("Please input an integer : ")
    if (not gy_N_str.isdigit()):
        print("Input a wrong paramter , exit !")
        return None

    gy_N = int(gy_N_str)
    gy_yanghui_triangle_recursive(gy_N,gy_N)
    # temp_list_N_1 = [1,1]
    # temp_list_N = []
    # for i in range(0,gy_N,1):
    #     for j in range(0,i + 1,1):
    #         if (0 == j) or (i == j):
    #             temp_list_N.append(1)
    #         else:
    #             temp_list_N.append(temp_list_N_1[j - 1] + temp_list_N_1[j])
    #     #print("temp_list_N = ",temp_list_N)
    #     gy_print_Yanghui(temp_list_N,gy_N)
    #     del temp_list_N_1[::]
    #     temp_list_N_1 = copy.deepcopy(temp_list_N)
    #     del temp_list_N[::]

    return None

if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit,
    1 : gy_test_6_1(Print Yang Hui Triangle)
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_6_1
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
