# !/usr/bin/env python3
# -*- coding : utf-8 -*-
# __author__ : GarryZheng
# __date__ : 2026-01-05

def py_test_exit():
    exit()
    return None


def practice_evday_01()->int:
    gy_result = 0
    for i in range(5):
        gy_result += i
        i += 5
    print(gy_result)
    return gy_result

def practice_evday_02():
    gy_dict = {"a" : 1}
    gy_dict_backup = gy_dict
    gy_dict['b'] = 2
    print(gy_dict_backup)
    print(len(gy_dict_backup))
    return None


def practice_evday_03():
    print(0.1 + 0.2 == 0.3)
    return None

def practice_evday_04():
    A = 5
    B = 8
    print(A + B)
    return None



if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.practice_evday_01.
    2.practice_evday_02.
    3.practice_evday_03.
    4.practice_evday_04.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : practice_evday_01,
        "2" : practice_evday_02,
        "3" : practice_evday_03,
        "4" : practice_evday_04
    }
    print(dis_playmessage)
    while True:
        try:
            gy_choice = input("Please input the test choice : ")
            test_dict[gy_choice]()
        except Exception as e:
          print('An exception occurred is ',e)
