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

def practice_evday_14():
    try:
        a = '20'
        b = '24'
        print(f'a + b = {a + b},{type(a + b)}')
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_15():
    try:
        a = 0
        b = 5
        print(f'a or (b and 10) = {a or (b and 10)},{type(a or (b and 10))}')
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_16():
    try:
        for i in range(0,3,1):
            if (i == 5):
                break
        else:
            print("Done !")
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_17():
    try:
        funcs = []
        for i in range(0,3,1):
            funcs.append(lambda : i)
        print(f"funcs = {funcs}")
        print([f() for f in funcs])
        funcs1 = []
        f = lambda a : a
        print(f(4))
        for k in range(0,3,1):
            funcs1.append(lambda x = k : x)
            # "默认参数就像给lambda拍了一张快照，把当前瞬间永远定格"

        print(f"funcs1 = {funcs1}")
        print([f() for f in funcs1])
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_18():
    try:
        print(bool(2) + 3)
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_19():
    try:
        s = {1,2}
        x = s.add(3)
        print(f'x is {x} , s is {s}.')
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_20():
    try:
        s = [3,5,7,9]
        s[1] = s[0] + s[2]
        s[3] = s[1] * 2
        print(f's[3] is {s[3]} , s is {s}.')
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_21():
    try:
        gy_l = [i * i + 1 for i in range(1,10,3)]
        print("gy_l is {} ".format(gy_l))
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_22():
    try:
        gy_l = [10,20]
        gy_b = gy_l * 2
        print("gy_b is {} ".format(gy_b))
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

def practice_evday_23():
    try:
      gy_a = 3
      gy_b = 3
      print(f"gy_a is {hex(id(gy_a))} , gy_b is {hex(id(gy_b))}")
      if (gy_a is gy_b):
        print("The same , ram address is the same !")
      elif (gy_a == gy_b):
        print("The value equal !")
      else:
        print("Different !")
    except Exception as e:
      print('Something went wrong e is : ',e)
    finally:
      print('The try except is finished')
    return None

import json
from pathlib import Path

def practice_evday_24():
    try:
      gy_dict = {
          "job" : "Software engineer",
          "name": "GarryZheng",
          "age" : 39,
          "info": { "job" : "Software engineer","name": "GarryZheng","age" : 39}
      }
      gy_file = "./gy_con_dict.json"
      with open(gy_file,"w",encoding = 'utf-8') as f:
        # write the data as json format to file
        json.dump(gy_dict,f,indent = 4, ensure_ascii = False)

      #  create path object
      config_path = Path(gy_file)
      with config_path.open() as gy_f:
        # read the json file to python data
        gy_config = json.load(gy_f)
        print(gy_config.get('info'),gy_config.get('job'),gy_config.get('info').get('job'),sep = "\n",)
    
      gy_l = [1,2,3,4,5,6,5,4,3,3,2,3,4]
      gy_file_l = "./gy_con_list.json"
      con_file_l = Path(gy_file_l)
      with con_file_l.open('w',encoding = 'utf-8') as gy_f_l:
        json.dump(gy_l,gy_f_l,indent = 4, ensure_ascii = False)
    except Exception as e:
      print('Something went wrong e is : ',e)
    return None

def practice_evday_25():
    try:
      vegatible = "Tomato"
      print(vegatible.replace("a","s"))
    except Exception as e:
      print('Something went wrong e is : ',e)
    return None

def practice_evday_26():
    try:
        gy_x_dic = {"x":3}
        gy_b_dic = gy_x_dic
        gy_x_dic.update({"x":4})
        gy_x_dic = {"x":5}
        print(f"gy_b_dic = {gy_b_dic}")
    except Exception as e:
      print('Something went wrong e is : ',e)
    return None

def practice_evday_27():
    try:
      class Cat:
        def mnew(self):
         print("menow")
    
      gy_c = Cat()
      gy_c.mnew()
    except Exception as e:
      print('Something went wrong e is : ',e)
    return None

def practice_evday_28():
    try:
      gy_a_l = [1,2,3]
      gy_b_l = gy_a_l
      gy_a_l[0] = 9
      print(f"gy_b_l = {gy_b_l}")
    except Exception as e:
      print('Something went wrong e is : ',e)
    return None

def practice_evday_29():
    try:
        '''
        Python 的默认参数值在函数定义时只创建一次，
        而不是每次调用时重新创建。
        当默认参数是可变对象（如列表、字典）时，所有函数调用都会共享这个对象。
        危险的默认参数
        • 列表:def func(x=[])
        • 字典:def func(x={})
        • 集合:def func(x=set())
        '''
        def gy_func(x,y = [])->list:
            y.append(x)
            return y

        print(gy_func(1))
        print(gy_func(3))
    except Exception as e:
        print('Something went wrong e is : ',e)
    return None

def practice_evday_30():
    try:
        word = 'So'
        ch = 'ftware'
        print(word * 2 + 'Love')
    except Exception as e:
        print('Something went wrong e is : ',e)
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
    14.practice_evday_14.
    15.practice_evday_15.
    16.practice_evday_16.
    17.practice_evday_17.
    18.practice_evday_18.
    19.practice_evday_19.
    20.practice_evday_20.
    21.practice_evday_21.
    22.practice_evday_22.
    23.practice_evday_23.
    24.practice_evday_24.
    25.practice_evday_25.
    26.practice_evday_26.
    27.practice_evday_27.
    28.practice_evday_28.
    29.practice_evday_29.
    30.practice_evday_30.
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
        "13": practice_evday_13,
        "14": practice_evday_14,
        "15": practice_evday_15,
        "16": practice_evday_16,
        "17": practice_evday_17,
        "18": practice_evday_18,
        "19": practice_evday_19,
        "20": practice_evday_20,
        "21": practice_evday_21,
        "22": practice_evday_22,
        "23": practice_evday_23,
        "24": practice_evday_24,
        "25": practice_evday_25,
        "26": practice_evday_26,
        "27": practice_evday_27,
        "28": practice_evday_28,
        "29": practice_evday_29,
        "30": practice_evday_30
    }
    print(dis_playmessage)
    while True:
        try:
            gy_choice = input("Please input the test choice : ")
            test_dict[gy_choice]()
        except Exception as e:
          print('An exception occurred is ',e)
