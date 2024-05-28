# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math,copy
import Test_setting
from Test_com import py_test_exit

'''
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字
'''
def py_test_1_4_1():
    gy_dict = {
        'python' : 95,
        'java'   : 99,
        'c'      : 100
    }
    print("0 gy_dict is ",gy_dict)
    print("The length of gy_dict is {0}".format(len(gy_dict)))
    gy_dict['java'] = 98
    print("1 gy_dict is ",gy_dict)
    #del gy_dict['c']
    gy_dict.pop('c')
    print("2 gy_dict is ",gy_dict)
    gy_dict['php'] = 90
    print("3 gy_dict is ",gy_dict)
    gy_dict_key_list = []
    gy_dict_val_list = []
    for i_key,i_val in gy_dict.items():
        gy_dict_key_list.append(i_key)
        gy_dict_val_list.append(i_val)
    print("gy_dict_key_list = ",gy_dict_key_list," gy_dict_val_list = ",gy_dict_val_list)
    print("javascript is {flag} the gy_dict".format(flag = 'in' if ('javascript' in gy_dict) else 'not in' ))
    gy_dict_vals = gy_dict.values()
    print("The sum of all values in gy_dict is ",sum(list(gy_dict_vals)))
    print("The max value in gy_dict is ",max(list(gy_dict_vals)))
    print("The min value in gy_dict is ",min(list(gy_dict_vals)))
    gy_dict1 = {'php' : 97}
    gy_dict.update(gy_dict1)
    print("4 gy_dict is ",gy_dict)
    return None

def py_test_1_4_2():
    gy_dict_fruit = {
        '苹果 ' : 32.8,
        '香蕉 ' : 22,
        '葡萄 ' : 15.5,
          4   : 22
    }
    print(" gy_dict_fruit is ",gy_dict_fruit)
    print(" gy_dict_fruit is ",gy_dict_fruit.keys())
    return None

def py_test_1_4_3():
    gy_dict_fruit = {
        '小明' : {"水果" : ['苹果','香蕉','草莓'],"费用" : 89},
        '小刚' : {"水果" : ['葡萄','橘子','樱桃'],"费用" : 87}
    }
    print(" gy_dict_fruit is ",gy_dict_fruit)
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_4_1.
    2.py_test_1_4_2.
    3.py_test_1_4_3.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_4_1,
        "2" : py_test_1_4_2,
        "3" : py_test_1_4_3

    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()


