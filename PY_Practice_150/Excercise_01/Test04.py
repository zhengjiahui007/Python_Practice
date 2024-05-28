# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math,copy
import Test_setting
from Test_com import py_test_exit


def py_test_1_3_3():
    print("(1,2) * 2 = {} ".format((1,2) * 2))
    print("(1,) * 2 = {0}".format(((1,) * 2)))
    print("(1) * 2 = ",(1) * 2)
    return None

def py_test_1_3_4():
    gy_list = [1,2,3]
    print(id(gy_list))
    gy_list1 = [4,5,6]
    # for i in gy_list1:
    #     gy_list.append(i)
    gy_list.extend(gy_list1)
    print(gy_list,id(gy_list))# no new list
    return None

def py_test_1_3_5():
    gy_str = "1,2,3"
    print(id(gy_str))
    gy_str1 = "4,5,6"
    # gy_str2 = ",".join([gy_str,gy_str1]
    # print(gy_str2,id(gy_str2))# a new string
    gy_str = gy_str + "," + gy_str1
    print(gy_str,id(gy_str))
    return None

def py_test_1_3_6():
    gy_list = [2,5,6,7,8,9,2,9,9]
    print("The max value in {0} is {1}".format(gy_list,max(gy_list)))
    print("The min value in {0} is {1}".format(gy_list,min(gy_list)))
    print("The count of max value {2} in {0} is {1}".format(gy_list,gy_list.count(max(gy_list)),max(gy_list)))
    print("The average value of {0} is {1}".format(gy_list,sum(gy_list)/len(gy_list)))
    print("The length of {0} is {1} .".format(gy_list,len(gy_list)))
    print("The index of 6 in {0} is {1} .".format(gy_list,gy_list.index(6)))
    return None

def py_test_1_3_6_1():
    gy_list = [2,5,6,7,8,9,2,9,9]
    print("gy_list is ",gy_list)    
    print("gy_list[2:4] is ",gy_list[2:4])
    print("gy_list[1:-3] is ",gy_list[1:-3])
    print("gy_list[-5] is ",gy_list[-5])
    print("gy_list[ : -4] is ",gy_list[ : -4])
    print("gy_list[-4 : ] is ",gy_list[-4 : ])
    return None

def py_test_1_3_7():
    gy_list = [2,5,6,7,8,9,2,9,9]
    print("gy_list is ",gy_list)
    gy_list_c = gy_list.copy()
    gy_list_c.append(15)
    print("gy_list_c is ",gy_list_c)
    gy_list_c = gy_list.copy()
    gy_list_c.insert(4,20)
    print("gy_list_c is ",gy_list_c)
    gy_list_c = gy_list.copy()
    gy_list_c.extend([2,5,6])
    print("gy_list_c is ",gy_list_c)
    gy_list_c = gy_list.copy()
    gy_list_c.pop(3)
    print("gy_list_c is ",gy_list_c)
    gy_list.reverse()
    print("Reverse gy_list is ",gy_list)
    gy_list.sort(reverse = False)
    print("Sort gy_list from small to big is ",gy_list)
    gy_list.sort(reverse = True)
    print("Sort gy_list from big to small is ",gy_list)      
    return None

def py_test_1_3_8():
    gy_list = [1,4,5,[1,3,5,6,[8,9,10,12]]]
    print("gy_list is ",gy_list)
    print("The length of {0} is {1} .".format(gy_list,len(gy_list)))
    print("The count of {0} is {1} .".format(gy_list,len(gy_list)))
    print("The type of gy_list[1] is ",type(gy_list[1]))
    print("The type of gy_list[3] is ",type(gy_list[3]))
    print("The gy_list[3][4] is ",(gy_list[3][4]))
    print("The gy_list[3][4][1] is ",(gy_list[3][4][1]))
    gy_list_c = copy.deepcopy(gy_list)
    gy_list_c[3][4].append([5,6])
    print("The gy_list_c is ",(gy_list_c))
    print("The gy_list[-1][-1][-2] is ",(gy_list[-1][-1][-2]))
    print("The gy_list[-2] is ",(gy_list[-2]))
    print("The length of len(gy_list[-1]) is ",len(gy_list[-1]))
    print("The length of len(gy_list[-1][-1]) is ",len(gy_list[-1][-1]))
    print("The gy_list[-1][1:3] is ",(gy_list[-1][1:3]))
    print("The gy_list[-1][-1][1:-2] is ",(gy_list[-1][-1][1:-2]))
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_3_3.
    2.py_test_1_3_4.
    3.py_test_1_3_5.
    4.py_test_1_3_6.
    5.py_test_1_3_6_1.
    6.py_test_1_3_7.
    7.py_test_1_3_8.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_3_3,
        "2" : py_test_1_3_4,
        "3" : py_test_1_3_5,
        "4" : py_test_1_3_6,
        "5" : py_test_1_3_6_1,
        "6" : py_test_1_3_7,
        "7" : py_test_1_3_8
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()