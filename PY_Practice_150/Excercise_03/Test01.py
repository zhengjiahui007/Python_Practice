# !/usr/bin/env python3
# -*- coding : utf-8 -*-
# !__author__ : "GarryZheng"
# Date : 2024-06-01

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable

def gy_abs(number):
    if isinstance(number,(int,float)):
        if (0 <= number):
            return number
        else:
            return (-1*number)
    else:
        print("The number is not correct !")
    return None

def gy_sum(lst):
    list_sum = 0
    if isinstance(lst,list):
        for i_val in lst:
            if isinstance(i_val,(int,float)):
                list_sum += i_val
    return list_sum

def gy_max(sequence):
    if ((0 == len(sequence)) or (not isinstance(sequence,(list,tuple)))):
        print("The sequence is empty or not a sequence !")
        return None

    list_digit = []
    for i_val in sequence:
        if isinstance(i_val,(int,float)):
            list_digit.append(i_val)

    if (0 == len(list_digit)):
        print("The list_digit is empty !")
        return None

    max_val = list_digit[0]
    for i_val in list_digit:
        if (i_val > max_val):
            max_val = i_val
    return max_val

def gy_min(sequence):
    '''
    The same as gy_max
    '''
    pass
    return None

def gy_int(str_val:str):
    if not isinstance(str_val,(str,)):
        print(f"The val {str_val} in not a string !")
        return None

    if not str_val.isdigit():
        print(f"The val {str_val} in not a digital string !")
        return None        
    #如果步长为负数 , 其起始下标索引 要 大于 结束下标索引 ,当你使用步长-1时，默认的起始值是列表的最后一个元素
    #print(str_val[ : -len(str_val) - 1  :-1])
    int_dic = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9
    }
    int_val = 0
    for i_val in str_val:
        int_val *= 10
        int_val += int_dic[i_val]
    return int_val

def gy_str(int_val:int):
    if not isinstance(int_val,(int,)):
        print(f"The val {int_val} in not an int !")
        return None
    temp_val = int_val
    str_val = ""
    temp_int_unit = 0
    while temp_val:
        temp_int_unit = temp_val%10
        temp_val = temp_val//10
        #print(temp_int_unit,temp_val,chr(temp_int_unit + 0x30))
        str_val += chr(temp_int_unit + 0x30)

    return str_val[::-1]

def gy_float(str_val:str):
    if not isinstance(str_val,(str,)):
        print(f"The val {str_val} in not a string !")
        return None

    int_val_str,float_val_str = str_val.split('.')
    print(int_val_str,float_val_str)
    int_val = gy_int(int_val_str)
    float_val = gy_int(float_val_str)
    print(int_val,float_val)

    temp_val = float_val
    temp_float_unit = 0
    temp_float = 0.0
    # while temp_val:
    #     temp_float_unit = temp_val%10
    #     temp_float += temp_float_unit
    #     temp_float *= 0.1
    #     temp_val = temp_val//10
    while (temp_val > 1):
        temp_val *= 0.1

    return (int_val + temp_val)

def gy_len(obj):
    obj_len = 0
    if not isinstance(obj,Iterable):
        return None

    for i in obj:
        obj_len += 1

    return obj_len

def py_test_3_1():
    print(gy_abs(0.4))
    print(gy_abs(23))
    print(gy_abs(-56))
    print(gy_abs(-0.4))
    return None

def py_test_3_2():
    print(gy_sum([1,67,32,'2',23,"sw"]))
    return None

def py_test_3_3():
    print(gy_max([1,67,32,'2',23,"sw"]))
    print(gy_max([-1,167,32,'12',0,"sw"]))
    print(gy_max(['-1',"167","32",'12',"0","sw"]))
    print(gy_max("fda"))
    return None

def py_test_3_4():
    num_result = gy_int("54893")
    print(num_result,type(num_result))
    num_result = gy_int("12231")
    print(num_result,type(num_result))    
    num_result = gy_int("5")
    print(num_result,type(num_result))    
    return None

def py_test_3_6():
    str_result = gy_str(54893)
    print(str_result,type(str_result))  
    return None

def py_test_3_7():
    float_result = gy_float("134.89809")
    print(float_result,type(float_result))
    float_result = gy_float("780.824809")
    print(float_result,type(float_result))      
    return None

def py_test_3_8():
    len_result = gy_len("134.89809")
    print(len_result,type(len_result))
    len_result = gy_len([1,2,3,5])
    print(len_result,type(len_result))
    len_result = gy_len((1,2,3,5,'w'))
    print(len_result,type(len_result))
    len_result = gy_len({1,2,3,5,'w',9})
    print(len_result,type(len_result))
    len_result = gy_len({1:2,3:5,'w':9})
    print(len_result,type(len_result))
    return None

if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_3_1.
    2.py_test_3_2.
    3.py_test_3_3.
    4.py_test_3_4.
    5.py_test_3_6.
    6.py_test_3_7.
    7.py_test_3_8.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_3_1,
        "2" : py_test_3_2,
        "3" : py_test_3_3,
        "4" : py_test_3_4,
        "5" : py_test_3_6,
        "6" : py_test_3_7,
        "7" : py_test_3_8
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()