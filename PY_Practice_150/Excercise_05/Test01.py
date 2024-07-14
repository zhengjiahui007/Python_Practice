# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-07-11"

import os,sys,time,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable
from Excercise_04 import Test02

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

########################### Triangle S and Perimeter####################################################
def gy_test_6_2():
    gy_lens_str = input("Please input 3 lengths of a triangle with an example as 3 4 5 : ")
    gy_len_lst = gy_lens_str.split(" ")
    if (3 != len(gy_len_lst)):
        print("The number of length is not 3 , please input again !")
        return None

    if ((not gy_len_lst[0].isdigit()) or (not gy_len_lst[1].isdigit()) or (not gy_len_lst[2].isdigit()) ):
        print("Input a wrong paramter , exit !")
        return None
    
    gy_a = int(gy_len_lst[0])
    gy_b = int(gy_len_lst[1])
    gy_c = int(gy_len_lst[2])
    gy_P = 0
    gy_S = 0
    if ((gy_a < (gy_b + gy_c)) and (gy_b < (gy_a + gy_c)) and (gy_c < (gy_b + gy_a))):
        gy_P = (gy_a + gy_b + gy_c)
        gy_p_half = gy_P/2
        gy_S = (gy_p_half * (gy_p_half - gy_a) * (gy_p_half - gy_b) * (gy_p_half - gy_c)) ** 0.5
        print("The P = {} and S = {} .".format(gy_P,gy_S))
        return (gy_P,gy_S)
    else:
        print("The 3 numbers can not construct a triangle , please input again !")

    return None

def gy_test_6_3():
    gy_str0 = "AbCdF"
    gy_str1 = "FbCDf"
    letter_lst = []
    for s in gy_str0:
        if (('A' <= s) and ('Z' >= s)) or (('a' <= s) and ('z' >= s)):
            pass
        else:
            print("The strings are not correct !")
            return False

    for s in gy_str1:
        if (('A' <= s) and ('Z' >= s)) or (('a' <= s) and ('z' >= s)):
            pass
        else:
            print("The strings are not correct !")
            return False

    if (len(gy_str0) != len(gy_str1)):
        print("The strings are not correct !")
        return False

    is_same = True
    for i in range(0,len(gy_str0),1):
        if (gy_str0[i] == gy_str1[i]) or (32 == abs(ord(gy_str0[i]) - ord(gy_str1[i]))):
            is_same = True
        else:
            is_same = False
            break

    print("The result is {result} !".format(result = "the same" if is_same else "not the same"))
    return is_same

def gy_test_6_4():
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    '''
    若step为负
    则表示从索引start开始取，直到索引end为止，但不包括索引end.
    如果start<= end,结果为空；
    　　解释: step为负数时，因为start + step < end .
    　　所以, 计算的索引肯定不在[start, end)区间内所以，结果为空([])
    如果start缺省，默认为len(str)-1；
    如果end缺省，默认小于0但不是-1(因为-1表示最后一位即-1表示索引为 len(str) - 1)
    '''
    gy_min,gy_max = gy_lst[0],gy_lst[0]
    for i_val in gy_lst:
        if (i_val > gy_max):
            gy_max = i_val
        if (i_val < gy_min):
            gy_min = i_val
    print(" gy_min = {} gy_max = {} .".format(gy_min,gy_max))
    return 

def gy_test_6_5():
    gy_lst = [1, 12, 32, 45, 54, 67, 90, 342,332,221,123]
    i = 0
    for i in range(0,len(gy_lst) - 1,1):
        if (gy_lst[i] > gy_lst[i + 1]):
            break
    print("The max value is %d "%(gy_lst[i]))
    return

def gy_test_6_6():
    gy_lst0 = [1, 12, 32, 45, 54]
    gy_lst1 = ['a','b','c','d','e']
    gy_lst_matrix = []
    for i_1 in gy_lst1:
        tmp_lst = []
        for i_0 in gy_lst0:
            tmp_lst.append(str(i_0) + i_1)
        gy_lst_matrix.append(tmp_lst)

    print("The gy_lst_matrix is  ",gy_lst_matrix)
    for i in range(0,len(gy_lst_matrix),1):
        for j in range(0,len(gy_lst_matrix[i]),1):
            print(gy_lst_matrix[i][j],end = " ")
        print()
    return

def gy_test_6_7():
    gy_lst = [
        [1, 12, 32],
        [121, 142, 532],
        [31, 132, 832]
    ]
    gy_lst_diagonal_sum = 0
    for i in range(0,len(gy_lst),1):
        gy_lst_diagonal_sum += gy_lst[i][i]
    print("gy_lst_diagonal_sum = ",gy_lst_diagonal_sum)
    return


if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit,
    1 : gy_test_6_1(Print Yang Hui Triangle)
    2 : gy_test_6_2(Triangle S and Perimeter)
    3 : gy_test_6_3(Is same ignore case)
    4 : gy_test_6_4(find_max_min)
    5 : gy_test_6_5(find max)
    6 : gy_test_6_6(creat matrix)
    7 : gy_test_6_7(diagonal sum)
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_6_1,
        "2" : gy_test_6_2,
        "3" : gy_test_6_3,
        "4" : gy_test_6_4,
        "5" : gy_test_6_5,
        "6" : gy_test_6_6,
        "7" : gy_test_6_7
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
