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

def gy_split(src:str,seq:str = "",maxsplit:int = -1):
    lst_split = []
    if not isinstance(src,str) or not isinstance(seq,str):
        return lst_split

    start_index = 0
    if (-1 != maxsplit):
        for i in range(0,maxsplit,1):
            seq_index = gy_find(src,seq,start_index)
            if (-1 != seq_index):
                lst_split.append(src[start_index:seq_index:1])
                start_index = (seq_index + len(seq))
            else:
                lst_split.append(src[start_index::1])
                break
        else:
            lst_split.append(src[start_index::1])
    else:
        seq_index = gy_find(src,seq,start_index)
        while (-1 != seq_index):
            seq_index = gy_find(src,seq,start_index)
            if (-1 != seq_index):
                lst_split.append(src[start_index:seq_index:1])
                start_index = (seq_index + len(seq))
            else:
                lst_split.append(src[start_index::1])
                break
        else:
            lst_split.append(src[start_index::1])

    return lst_split

def gy_lower(src:str)->str:
    new_str = ""
    if not isinstance(src,str):
        return new_str

    for i_val in src:
        if (('A' <= i_val) and ('Z' >= i_val)):
            new_str += chr(ord(i_val) + 32)
        else:
            new_str += i_val
    return new_str


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

def py_test_4_3():
    print(gy_split("This is GarryisZheng"," ",4))
    print("This is GarryisZheng".split(" ",4))
    print(gy_split("This is GarryisZheng","is"))
    print("This is GarryisZheng".split("is"))
    print(gy_split("I am gz hello how are you,i am ok oww !","o",2))
    print("I am gz hello how are you,i am ok oww !".split("o",2))
    print(gy_split("I am gz hello how are you,i am ok oww !","b",2))
    print("I am gz hello how are you,i am ok oww !".split("b",2))
    return None

def py_test_4_4():
    print(gy_lower("YUDSjsdUBXKJ"))
    print(gy_lower("5459=YUDSjsdU12&%**BXKJ"))
    return None

def gy_islower(src:str) -> bool:
    all_lower = True
    if not isinstance(src,str):
        return False

    for i_val in src:
        if (('a' > i_val) or ('z' < i_val)):
            all_lower = False
            break
    return all_lower

def py_test_4_5():
    print(gy_islower('fldjfkdsIO'))
    print(gy_islower('fldjfkdsuih'))
    print(gy_islower('fld456jfkdsuih'))
    return None

def gy_isdigit(src:str) -> bool:
    all_digit = True
    if not isinstance(src,str):
        return False

    for i_val in src:
        if (('0' > i_val) or ('9' < i_val)):
            all_digit = False
            break
    return all_digit

def py_test_4_6():
    print(gy_isdigit('fldjf34kdsIO'))
    print(gy_isdigit('fldjfk21dsuih'))
    print(gy_isdigit('434546767824524'))
    return None

def gy_isstartwith(src:str,substr:str) -> bool:
    try:
        if not isinstance(src,str) or not isinstance(substr,str):
            return False

        if (len(substr) > len(src)):
            return False

        isstartwith = True
        for s_index in range(0,len(substr),1):
            if (substr[s_index] != src[s_index]):
                isstartwith = False
                break

    except Exception as e:
        print("The exception is ",e)
        isstartwith = False
    return isstartwith

def py_test_4_7():
    print(gy_isstartwith("fjdkjf",'fj'))
    print(gy_isstartwith("fjdkjf",'efj'))
    return None

def gy_isendwith(src:str,substr:str) -> bool:
    try:
        if not isinstance(src,str) or not isinstance(substr,str):
            return False

        if (len(substr) > len(src)):
            return False

        isendwith = True
        start_index = len(src) - len(substr)
        for s_index in range(start_index,len(src),1):
            if (substr[s_index - start_index] != src[s_index]):
                isendwith = False
                break

    except Exception as e:
        print("The exception is ",e)
        isendwith = False
    return isendwith

def py_test_4_8():
    print(gy_isendwith("fjdkjf",'fj'))
    print(gy_isendwith("fjdkjf",'kjf'))
    return None

def gy_capitalize(src:str) -> str:
    new_str = ""
    if not src:
        return src

    # if (not (('A' <= src[0]) and ('Z' >= src[0]))) and (not (('a' <= src[0]) and ('z' >= src[0]))):
    #     print("The first word is not an English letter")
    #     return new_str

    if (('A' <= src[0]) and ('Z' >= src[0])):
        new_str = src[0] + gy_lower(src[1::1])
    elif (('a' <= src[0]) and ('z' >= src[0])):
        new_str = chr(ord(src[0]) - 32) + gy_lower(src[1::1])
    else:
        print("The first word is not an English letter")
    return new_str

def py_test_4_9():
    print(gy_capitalize("3fjdkjf"))
    print(gy_capitalize("fdfsa34jdkjf"))
    return None

def gy_count(src:str,subsr:str,start:int,end:int) -> int:
    subsr_count = 0
    if not src or not subsr:
        return subsr_count

    if (start >= end):
        return subsr_count

    temp_src = src[start:end:1]
    start_index = gy_find(temp_src,subsr,0)
    while (-1 != start_index):
        subsr_count += 1
        if (start_index + len(subsr)) < len(temp_src):
            temp_src = temp_src[start_index + len(subsr)::1]
            start_index = gy_find(temp_src,subsr,0)
        else:
            break
    return subsr_count

def py_test_4_10():
    print(gy_count("3fjdkdfadfadsfgadfjf",'f',0,len("3fjdkdfadfadsfgadfjf") - 5))
    print(gy_count("My name is GZ , is an engineer,working in Harman,is a man !",'is',0,len("My name is GZ , is an engineer,working in Harman,is a man !")))
    return None

if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_4_1.
    2.py_test_4_2.
    3.py_test_4_3.
    4.py_test_4_4.
    5.py_test_4_5.
    6.py_test_4_6.
    7.py_test_4_7.
    8.py_test_4_8.
    9.py_test_4_9.
    10.py_test_4_10.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_4_1,
        "2" : py_test_4_2,
        "3" : py_test_4_3,
        "4" : py_test_4_4,
        "5" : py_test_4_5,
        "6" : py_test_4_6,
        "7" : py_test_4_7,
        "8" : py_test_4_8,
        "9" : py_test_4_9,
        "10" : py_test_4_10
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()





