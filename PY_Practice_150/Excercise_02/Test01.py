# !_*_ coding : utf-8 _*_
# !__author__ : "Garry Zheng"
# !usr/bin/env python3


import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR1 is {BASE_DIR}")
sys.path.append(BASE_DIR)
from Test_com import py_test_exit



def py_test_2_1_1():
    gy_input = input("Please input an integer : ")
    gy_input_int = int(gy_input)
    print("The {value} input is {flag} number !".format(value = gy_input_int,flag = 'even' if (0 == gy_input_int%2) else 'odd'))
    return None

def py_test_2_1_1_1():
    '''
    https://geek-docs.com/python/python-ask-answer/54_tk_1701997639.html
    '''
    print(f"*{'-' * 5: >10s}*")
    return None

def py_test_2_1_3():
    dict_input = {
        'python' : 90,
        'java'   : 95,
        'PHP'    : 85
    }

    print(f"Please input a string in the list {list(dict_input.keys())} : ",end = "")
    gy_input_string = input()
    if gy_input_string in dict_input:
        print(dict_input[gy_input_string])
    else:
        print(0)
    return None

def py_test_2_1_4():
    gy_input_string = input("Please input an integer : ")
    try:
        if not gy_input_string.isdigit():
            print("Your input is not an integer,please input again!")
            return None

        gy_input_int = int(gy_input_string)
        if (1 == gy_input_int % 2):
            print("%d * 2 is %d " %(gy_input_int,gy_input_int*2))
        else:
            if (0 == gy_input_int % 4):
                print("%d/4 is %d " %(gy_input_int,gy_input_int / 4))
            else:
                if (20 < gy_input_int):
                    print("%d - 20 is %d" %(gy_input_int,gy_input_int - 20))
                else:
                    print("Your input is %d ." %(gy_input_int))
    except Exception as e:
        print("Error {} ! Your input is not an integer,please input again !".format(e))
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_1_1.
    2.py_test_2_1_1_1.
    3.py_test_2_1_3.
    4.py_test_2_1_4.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_1_1,
        "2" : py_test_2_1_1_1,
        "3" : py_test_2_1_3,
        "4" : py_test_2_1_4
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()





