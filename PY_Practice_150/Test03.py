# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3


import os,sys,time,math

def py_test_1_2_2():
    gy_str = "Python is good"

    print(gy_str[1:20])
    # print(gy_str[20])
    print(gy_str[3:-4])
    print(gy_str[-10:-3])
    print(gy_str[-3:-10:-1])
    return None

def py_test_1_3_1():
    gy_str = "Python is good"

    print(gy_str[1:20])
    # print(gy_str[20])
    print(gy_str[3:-4])
    print(gy_str[-10:-3])
    print(gy_str[-3:-10:-1])
    return None

def py_test_1_3_1():
    gy_list = [1,3,2,5,7,6]
    print("gy_list is {0}".format(gy_list))
    print("The length of gy_list is : ",len(gy_list))
    print("6 is {pos} gy_list!".format(pos = "in" if 6 in gy_list else "not in"))
    
    print("gy_list + [6,7,8] = {0}".format(gy_list + [6,7,8]))
    print("gy_list * 2 = {0}".format(gy_list * 2))
    print("The max value in gy_list is {}".format(max(gy_list)))
    print("The min value in gy_list is {}".format(min(gy_list)))
    gy_list_sum = 0
    for x in gy_list:
        gy_list_sum += x
    print("The sum0 of  gy_list is {}".format(gy_list_sum))
    print("The sum1 of  gy_list is {}".format(sum(gy_list)))    
    gy_list_cp = gy_list[::]
    gy_list_cp.insert(2,10)
    print("gy_list_cp is {0}".format(gy_list_cp))
    print("gy_list is {0}".format(gy_list))
    gy_list.append(20)
    print("gy_list is {0}".format(gy_list))
    return None

def py_test_exit():
    exit()
    return None

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_1_2_2.
    2.py_test_1_3_1.
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_1_2_2,
        "2" : py_test_1_3_1,
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()







