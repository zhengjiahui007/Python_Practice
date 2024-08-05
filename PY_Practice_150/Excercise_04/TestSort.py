# -*-coding : utf-8-*-
# !usr/bin/env/ python3
# __author__ : "Garry Zheng"
# __Date__ : 2024-07-21

import os,time,sys,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Test_com import py_test_exit
from collections.abc import Iterable

def py_test_sort_1():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    for i_count in range(0,len(gy_lst),1):
        for i in range(0,len(gy_lst) - i_count - 1,1):
            if (gy_lst[i] > gy_lst[i + 1]):
                gy_lst[i],gy_lst[i + 1] = gy_lst[i + 1],gy_lst[i]
    print("gy_lst = ",gy_lst)
    return

# (quick sort)
def gy_quick_sort(lst:list,start_index:int,end_index:int):
    if (start_index >= end_index):
        # print(f" start_index = {start_index} , end_index = {end_index} ")
        return
    # print(f" start_index = {start_index} , end_index = {end_index} ")
    key_val = lst[start_index]
    i,j = start_index,end_index
    if (start_index < end_index):
        while (i < j):
            while (key_val < lst[j]):
                j -= 1
            lst[i],lst[j] = lst[j],lst[i]
            # print(f"0 lst = {lst} , i = {i} , j = {j} ")
            while (key_val > lst[i]):
                i += 1
            lst[i],lst[j] = lst[j],lst[i]
            # print(f"1 lst = {lst} , i = {i} , j = {j} ")
        # print(f"3 lst = {lst} , i = {i} , j = {j} ")
        # if (i == j):
        #     lst[i] = key_val
    gy_quick_sort(lst,start_index,i - 1)
    gy_quick_sort(lst,i + 1,end_index)
    return

def py_test_sort_2():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    gy_quick_sort(gy_lst,0,len(gy_lst) - 1)
    print(gy_lst)
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    gy_quick_sort(gy_lst,0,len(gy_lst) - 1)
    print(gy_lst)
    return

def gy_insert_sort(lst:list):
    for i in range(1,len(lst),1):
        need_insert_val = lst[i]
        need_insert_index = i
        for j in range((i - 1),-1,-1):
            if (need_insert_val < lst[j]):
                lst[j + 1] = lst[j]
                need_insert_index = j
            else:
                break
        lst[need_insert_index] = need_insert_val
    return lst

def py_test_sort_3():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    print(gy_insert_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_insert_sort(gy_lst))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_insert_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_insert_sort(gy_lst))
    return

# (Shell's sort)
def py_test_sort_4():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,21]
    interal_gap = len(gy_lst)//2
    while (interal_gap >= 1):
        for j in range(0,interal_gap,1):
            temp_lst = []
            for i in range(j,len(gy_lst),interal_gap):
                temp_lst.append(gy_lst[i])
            print("0 temp_lst = ",temp_lst)
            gy_insert_sort(temp_lst)
            print("1 temp_lst = ",temp_lst)
            for k in range(0,len(temp_lst),1):
                gy_lst[j + k * interal_gap] = temp_lst[k]
            del temp_lst[::]
        interal_gap //= 2
        print("gy_lst = ",gy_lst)
    return

# merge sort
def gy_merge_lst(l_lst:list,r_lst:list):
    print(f" l_lst = {l_lst} r_lst = {r_lst} ")
    merge_sorted_lst = []
    l_len = len(l_lst)
    r_len = len(r_lst)
    l_index,r_index = 0,0
    while ((l_index < l_len) and (r_index < r_len)):
        if (l_lst[l_index] < r_lst[r_index]):
            merge_sorted_lst.append(l_lst[l_index])
            l_index += 1
        else:
            merge_sorted_lst.append(r_lst[r_index])
            r_index += 1
    if (l_index == l_len):
        merge_sorted_lst.extend(r_lst[r_index::1])
    elif (r_index == r_len):
        merge_sorted_lst.extend(l_lst[l_index::1])
    print(" merge_sorted_lst = ",merge_sorted_lst)
    return merge_sorted_lst

def gy_merge_sort(lst:list):
    if len(lst) <= 1:
        return lst
    
    mid_index = len(lst)//2
    left_lst = gy_merge_sort(lst[:mid_index:1])
    print("left_lst = ",left_lst," mid_index = ",mid_index)
    right_lst = gy_merge_sort(lst[mid_index::1])
    print("right_lst = ",right_lst," mid_index = ",mid_index)
    return gy_merge_lst(left_lst,right_lst)

def py_test_sort_5():
    gy_lst = [1122,908,1123,61,3,9,12,10,78]
    print(gy_merge_sort(gy_lst))
    # gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    # print(gy_merge_sort(gy_lst))
    # gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    # print(gy_merge_sort(gy_lst))
    # gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    # print(gy_merge_sort(gy_lst))
    # gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    # print(gy_merge_sort(gy_lst))
    return

def py_test_sort_6():
    gy_lst = [1122,908,1123,61,3,9,12,10]
    for i in range(0,len(gy_lst),1):
        for j in range(i,len(gy_lst),1):
            if (gy_lst[i] > gy_lst[j]):
                gy_lst[i],gy_lst[j] = gy_lst[j],gy_lst[i]
    print("gy_lst = {}".format(gy_lst))
    return

def gy_heap_modify(lst:list,p_index:int,end_index:int):
    l_child = 2*p_index + 1
    r_child = 2*p_index + 2
    # print(f"modify , l_child = {l_child},r_child = {r_child} ,end_index = {end_index}")
    if (l_child <= end_index):
        if (lst[p_index] < lst[l_child]):
            lst[p_index],lst[l_child] = lst[l_child],lst[p_index]
            gy_heap_modify(lst,l_child,end_index)
    if (r_child <= end_index):
        if (lst[p_index] < lst[r_child]):
            lst[p_index],lst[r_child] = lst[r_child],lst[p_index]
            gy_heap_modify(lst,r_child,end_index)
    return

def gy_heap_sort(lst:list):
    gy_N = len(lst)
    # build heap
    for i in range((gy_N//2 - 1),-1,-1):
        # print("i = ",i)
        gy_heap_modify(lst,i,gy_N - 1)
    lst[0],lst[gy_N - 1] = lst[gy_N - 1],lst[0]
    # print("lst = ",lst)
    for i in range(1,gy_N,1):
        # print("i = ",i)
        gy_heap_modify(lst,0,gy_N - i - 1)
        lst[0],lst[gy_N - i - 1] = lst[gy_N - i - 1],lst[0]
        # print("lst = ",lst)
    return lst

def py_test_sort_7():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,1560]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,43,3248,674,21,90,3,12]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_heap_sort(gy_lst))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_heap_sort(gy_lst))
    return

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_sort_1.(pop sort)
    2.py_test_sort_2.(quick sort)
    3.py_test_sort_3.(insert sort)
    4.py_test_sort_4.(Shell's sort)
    5.py_test_sort_5.(merge sort)
    6.py_test_sort_6.(select sort)
    7.py_test_sort_7.(heap sort)
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_sort_1,
        "2" : py_test_sort_2,
        "3" : py_test_sort_3,
        "4" : py_test_sort_4,
        "5" : py_test_sort_5,
        "6" : py_test_sort_6,
        "7" : py_test_sort_7
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()