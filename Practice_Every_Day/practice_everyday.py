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

def practice_evday_05():
    car_brands = ['Honda','Toyota','BYD','Ford']
    with open('cars.csv', 'w',encoding = 'utf-8') as gy_f:
        gy_f.write(' '.join(car_brands) + '\n')# join used to separator.join(iterable)
        gy_f.write('-'.join(car_brands) + '\n')
        gy_f.write('*'.join(car_brands) + '\n')
    return None

import random
def practice_evday_06():
    gy_l = [0] * 6
    print("gy_l = ",gy_l)
    for i in range(0,6,1):
        gy_n = random.randint(1,10)
        if ((gy_n % 2) == 0):
            gy_l[i] = gy_n
    print("gy_l = ",gy_l)
    return None

def practice_evday_07():
    gy_tuple = ('apple','banana','orange','watermelon','strawberry')
    print(gy_tuple[1:3])
    # del gy_tuple[2]
    print(gy_tuple + ('pineapple','durian'))
    return None

def practice_evday_08():
    # map(func, iterable) → 把 func 依次喂给 iterable 的每个元素
    gy_l = list(map(float,(1,2,3,4)))
    print(gy_l)
    gy_l = list(map(lambda a , b : (a * b),(1,2,3,4),(5,6,7,8)))
    print(gy_l)
    return None

def practice_evday_09():
    gy_s = 0
    for k in range(0,3,1):
        if (k == 1):
            break
        gy_s += k
    print("gy_s = {} ".format(gy_s))
    return None

def practice_evday_10():
    '''
    某个字符或子串到底出现了多少次
    str.count(sub, start=0, end=len(str))
    '''
    gy_txt = "hbhhhhhbbbbhbbbhbbbbbhhhhhhhhbhbh"
    a = gy_txt.count('h',0,len(gy_txt))
    b = gy_txt.count('b',0,len(gy_txt))
    c = a - b
    print(f'a is {a} , b is {b} , c is {c} .')
    return None

def practice_evday_11():
    try:
        gy_info = ["一九","二九","三九"]
        '''
        delete element in list
        '''
        print(f" gy_info = {gy_info} .")
        gy_info.remove('一九')
        print(f" gy_info = {gy_info} .")
        gy_info = ["一九","二九","三九"]
        gy_info.pop(1)
        print(f" gy_info = {gy_info} .")
    except Exception as e:
      print('Something went wrong e ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_12():
    try:
        print(10 / 0)
    except ZeroDivisionError:
      print('Something went wrong !')
    finally:
      print('The try except is finished')
    return None

def practice_evday_13():
    try:
        gy_l1 = ['a','b','c']
        gy_l2 = list()
        gy_l1 += gy_l2
        gy_l1.clear()
        print(f'gy_l1 = {gy_l1}.')

        gy_l3 = [1,2,3]
        gy_l4 = gy_l3
        gy_l4[1] = 4
        print(f'gy_l3 = {gy_l3}')
        del gy_l4[::]
        print(f'gy_l3 = {gy_l3} , gy_l4 = {gy_l4}')

        gy_l5 = [1,2,3]
        gy_l6 = gy_l5
        gy_l6[1] = 7
        print(f'gy_l5 = {gy_l5}')
        gy_l6 *= 0
        print(f'gy_l5 = {gy_l5} , gy_l6 = {gy_l6}')

        gy_l7 = [1,2,3]
        gy_l8 = gy_l7
        gy_l7 = []
        print(f'gy_l7 = {gy_l7} , gy_l8 = {gy_l8}')
    except Exception:
      print('Something went wrong !')
    finally:
      print('The try except is finished')
    return None

if ('__main__' == __name__):
    dis_playmessage = """
    0.Exit.
    1.practice_evday_01.
    2.practice_evday_02.
    3.practice_evday_03.
    4.practice_evday_04.
    5.practice_evday_05.
    6.practice_evday_06.
    7.practice_evday_07.
    8.practice_evday_08.
    9.practice_evday_09.
    10.practice_evday_10.
    11.practice_evday_11.
    12.practice_evday_12.
    13.practice_evday_13.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : practice_evday_01,
        "2" : practice_evday_02,
        "3" : practice_evday_03,
        "4" : practice_evday_04,
        "5" : practice_evday_05,
        "6" : practice_evday_06,
        "7" : practice_evday_07,
        "8" : practice_evday_08,
        "9" : practice_evday_09,
        "10": practice_evday_10,
        "11": practice_evday_11,
        "12": practice_evday_12,
        "13": practice_evday_13
    }
    print(dis_playmessage)
    while True:
        try:
            gy_choice = input("Please input the test choice : ")
            test_dict[gy_choice]()
        except Exception as e:
          print('An exception occurred is ',e)
