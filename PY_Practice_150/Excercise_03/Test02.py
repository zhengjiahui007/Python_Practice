# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !usr/bin/env/ python3
# Date : 2024-06-11

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable


def gy_find(src:str,target:str,start:int = 0):
    try:
        if not isinstance(src,str) or not isinstance(target,str):
            return -1

        if (0 > start) or (start >= len(src)):
            return -1

        if (len(target) > len(src)):
            return -1

        target_index = 0
        i_dex = 0
        target_start_match = -1
        for i_dex in range(start,len(src),1):
            if (src[i_dex] == target[target_index]):
                #print("target_index = {},i_dex = {}".format(target_index,i_dex))
                target_index += 1
                if (target_index == len(target)):
                    target_start_match = i_dex - len(target) + 1
                    break
            else:
                target_index = 0
    except Exception as e:
        print("The exception is ",e)
        target_start_match = -1
    return target_start_match

def gy_replace(src:str,oldsub:str,newsub:str):
    try:
        if not isinstance(src,str) or not isinstance(oldsub,str) or not isinstance(newsub,str):
            return None

        # method in excercise file
        src_new = ""
        start_index = 0
        old_start_index = gy_find(src,oldsub,start_index)
        while (-1 != old_start_index):
            src_before_oldsub = src[start_index:old_start_index:1]
            src_new += src_before_oldsub + newsub
            start_index = old_start_index + len(oldsub)
            old_start_index = gy_find(src,oldsub,start_index)
        else:
            src_new += src[start_index::1]

        # my method
        # src_new = src
        # old_start_index = gy_find(src,oldsub,0)
        # while (-1 != old_start_index):
        #     src_before_oldsub = src_new[0:old_start_index:1]
        #     src_after_oldsub = src_new[old_start_index + len(oldsub)::1]
        #     src_new = src_before_oldsub + newsub + src_after_oldsub
        #     print("src_new = ",src_new)
        #     old_start_index = gy_find(src_new,oldsub,0)

        # Only can replace the first oldsub
        # if (-1 != old_start_index):
        #     src_before_oldsub = src[0:old_start_index:1]
        #     src_after_oldsub = src[old_start_index + len(oldsub)::1]
        #     src_new = src_before_oldsub + newsub + src_after_oldsub
        # else:
        #     return None
    except Exception as e:
        print("The exception is ",e)
    return src_new

def py_test_4_1():
    print(gy_find("fadkljf",'dkl'))
    print(gy_find("fadkljf",'dklj'))
    print(gy_find("fadkljf",'adk'))
    print(gy_find("fadkljf",'k',1))
    print(gy_find("f adk ljf",'kl',1))
    print(gy_find("I am GarryZheng",'rr',3))
    return None

def py_test_4_2():
    print(gy_replace("fadkljf",'dkl','kuuike'))
    print(gy_replace("fadkljf",'adkl','ku'))
    print(gy_replace("fadkljf",'adkl','kiou'))
    print(gy_replace("This is GarryisZheng !",'is','kiou'))
    print(gy_replace("This is GarryisZhenisg is OK is !",'is','kiou'))
    return None


if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_4_1.
    2.py_test_4_2.

    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_4_1,
        "2" : py_test_4_2,

    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()





