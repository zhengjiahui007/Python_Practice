# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math,copy
from Test_com import py_test_exit

'''
集合（set）是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
tup1 = () 创建空元组
'''

def py_test_1_5_1():
    gy_lst_0 = [1,2,3,5,6,3,2]
    gy_lst_1 = [2,5,7,9]

    gy_set_0 = set(gy_lst_0)
    gy_set_1 = set(gy_lst_1)
    print("gy_set_0 = ",gy_set_0," gy_set_1 = ",gy_set_1)
    print("The intersection of gy_set_0 and gy_set_1 is {0} , {1} ".format(gy_set_0.intersection(gy_set_1),gy_set_0 & gy_set_1))
    print("The difference set of gy_set_0 and gy_set_1 is  {0} , {1} ".format(gy_set_0.difference(gy_set_1),gy_set_0 - gy_set_1))
    print("The union set of gy_set_0 and gy_set_1 is {0} , {1} ".format(gy_set_0 | gy_set_1,gy_set_0.union(gy_set_1)))
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_5_1.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_5_1
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()







