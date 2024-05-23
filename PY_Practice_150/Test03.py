# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math,copy
from Test_com import py_test_exit
#import Test_com

def py_test_1_2_2():
    gy_str = "Python is good"

    print(gy_str[1:20])
    # print(gy_str[20])
    print(gy_str[3:-4])
    print(gy_str[-10:-3])
    print(gy_str[-3:-10:-1])
    return None

def py_test_1_3_1():
    gy_str = "Python is good"

    print(gy_str[1:20])
    # print(gy_str[20])
    print(gy_str[3:-4])
    print(gy_str[-10:-3])
    print(gy_str[-3:-10:-1])
    return None

def py_test_1_3_1():
    gy_list = [1,3,2,5,7,6]
    print("gy_list is {0}".format(gy_list))
    print("The length of gy_list is : ",len(gy_list))
    print("6 is {pos} gy_list!".format(pos = "in" if 6 in gy_list else "not in"))
    
    print("gy_list + [6,7,8] = {0}".format(gy_list + [6,7,8]))
    print("gy_list * 2 = {0}".format(gy_list * 2))
    print("The max value in gy_list is {}".format(max(gy_list)))
    print("The min value in gy_list is {}".format(min(gy_list)))
    gy_list_sum = 0
    for x in gy_list:
        gy_list_sum += x
    print("The sum0 of  gy_list is {}".format(gy_list_sum))
    print("The sum1 of  gy_list is {}".format(sum(gy_list)))    
    gy_list_cp = gy_list[::]
    gy_list_cp.insert(2,10)
    print("gy_list_cp is {0}".format(gy_list_cp))
    print("gy_list is {0}".format(gy_list))
    gy_list.append(20)
    print("gy_list is {0}".format(gy_list))
    return None

def py_test_multiply_2(lst:list):
    for li_index,li_val in enumerate(lst):
        if isinstance(li_val,list):
            py_test_multiply_2(li_val)
        if isinstance(li_val,bool):
            continue
        if isinstance(li_val,int):
            lst[li_index] = li_val * 2
    return


def py_test_1_3_2():
    gy_list = [1,[4,6],True]
    print(enumerate(gy_list))
    for list_index,list_val in enumerate(gy_list):
        print(list_index,list_val)
    print("Before mul by 2 : ",gy_list)
    py_test_multiply_2(gy_list)
    print("After mul by 2 : ",gy_list)
    return None

def py_test_1_3_3_copy():
    print("直接赋值,all are shallow copy : ")
    gy_list = [1,[4,6],True,'hello',(1,2,5)]
    gy_list_cp0 = gy_list
    print(id(gy_list),id(gy_list_cp0))
    gy_list_cp0[4] = (1,12,5)
    print(gy_list,gy_list_cp0)
    print()

    print("切片赋值 , 第一层deep copy,其他层 shallow copy : ")
    gy_list_new = [1,[4,6],True,'hello',(1,2,5)]
    gy_list_cp1 = gy_list_new[::]
    gy_list_cp1[4] = (1,2,15)
    print(gy_list_new,gy_list_cp1)
    print(id(gy_list_new),id(gy_list_cp1))
    print()

    print("list copy,第一层deep copy,其他层 shallow copy : ")
    gy_list_new1 = [1,[4,6],True,'hello',(1,2,5)]
    gy_list_cp2 = gy_list_new1.copy()
    print(id(gy_list_new1),id(gy_list_cp2))
    gy_list_cp2[1][0] = 23
    gy_list_cp2[4] += (23,)
    print(gy_list_new1,gy_list_cp2)
    print()

    print("copy.copy,第一层deep copy,其他层 shallow copy : ")
    gy_list_new2 = [1,[4,6],True,'hello',(1,2,5)]
    gy_list_cp3 = copy.copy(gy_list_new2)
    print(id(gy_list_new2),id(gy_list_cp3))
    gy_list_cp3[1][0] = 43
    gy_list_cp3[4] += (123,)
    print(gy_list_new2,gy_list_cp3)
    print()

    print("copy.deepcopy,all are deep copy : ")
    gy_list_new3 = [1,[4,6],True,'hello',(1,2,5)]
    gy_list_cp4 = copy.deepcopy(gy_list_new3)
    print(id(gy_list_new3),id(gy_list_cp4))
    gy_list_cp4[1][0] = 43
    gy_list_cp4[4] += (123,)
    print(gy_list_new3,gy_list_cp4)
    print()
    return None


if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_2_2.
    2.py_test_1_3_1.
    3.py_test_1_3_2.
    4.py_test_1_3_3_copy.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_2_2,
        "2" : py_test_1_3_1,
        "3" : py_test_1_3_2,
        "4" : py_test_1_3_3_copy
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()







