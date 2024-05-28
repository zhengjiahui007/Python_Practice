# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


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

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_1_1.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_1_1
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()





