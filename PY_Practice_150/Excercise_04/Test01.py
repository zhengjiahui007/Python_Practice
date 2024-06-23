# -*- coding : utf-8 -*-
# !usr/bin/env/ python3
# __author__ : "GarryZheng"
# __Date__ : 2024-06-17

import os,sys,time,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit
from collections.abc import Iterable




#pop_sort
def gy_pop_sort(lst:list):
    if not isinstance(lst,list):
        return lst

    for i in range(0,len(lst),1):
        print(lst)
        for j in range(i,len(lst),1):
            #if (lst[i] > lst[j]):
            if (lst[i] < lst[j]):
                lst[i],lst[j] = lst[j],lst[i]
    return lst

#pop_sort
def py_test_2_1():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221]
    print(gy_pop_sort(gy_lst))
    return

#quick_sort
def gy_quick_sort(lst:list,start_index:int,end_index:int):
    if (start_index >= end_index):
        return

    i_start = start_index
    j_end = end_index
    pivot = lst[i_start]
    #print("pivot = ",pivot)
    while (i_start < j_end):
        while ((i_start < j_end) and (lst[j_end] >= pivot)):#The first value is the base value, so compare from the last
            j_end -= 1
        #print("j_end = ",j_end)
        lst[i_start] = lst[j_end]
        #print("2 lst = ",lst)
        while ((i_start < j_end) and (lst[i_start] <= pivot)):
            i_start += 1
        #print("i_start = ",i_start)
        lst[j_end] = lst[i_start]
        #print("1 lst = ",lst)

    lst[i_start] = pivot
    print("lst = ",lst)
    gy_quick_sort(lst,start_index,i_start - 1)
    gy_quick_sort(lst,i_start + 1,end_index)


    """ 
    i_start = start_index
    j_end = end_index
    #pivot = lst[start_index]
    pivot = start_index
    while (i_start < j_end):
        # while ((i_start < j_end) and (lst[j_end] >= pivot)):
        #     j_end -= 1
        # lst[i_start] = lst[j_end]
        # print("2 lst = ",lst)
        # while ((i_start < j_end) and (lst[i_start] <= pivot)):
        #     i_start += 1
        # lst[j_end] = lst[i_start]
        # print("1 lst = ",lst)

        # print("1 i_start = ",i_start," j_end = ",j_end)

        while ((i_start < j_end) and (lst[i_start] <= lst[pivot])):
            i_start += 1
        while ((i_start < j_end) and (lst[j_end] > lst[pivot])):
            j_end -= 1
        if (i_start < j_end):
            lst[j_end],lst[i_start] = lst[i_start],lst[j_end]
        print("2 lst = ",lst)

        print("1 i_start = ",i_start," j_end = ",j_end)

    print("i_start = ",i_start," j_end = ",j_end)
    #lst[pivot],lst[j_end] = lst[j_end],lst[pivot]
    lst[j_end],lst[pivot] = lst[pivot],lst[j_end]

    print("lst = ",lst)
    gy_quick_sort(lst,start_index,i_start - 1)
    gy_quick_sort(lst,i_start + 1,end_index)
    """
    return

#quick_sort
def py_test_2_2():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221]
    gy_quick_sort(gy_lst,0,len(gy_lst) - 1)
    print(gy_lst)
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    gy_quick_sort(gy_lst,0,len(gy_lst) - 1)
    print(gy_lst)
    return

'''
算法思想

插入排序的基本思想是将待排序的元素看作一个有序表和一个无序表。
开始时，有序表中只包含一个元素，而无序表中包含有n-1个元素。
在排序过程中，每次从无序表中取出第一个元素，
将其与有序表中的元素的排序码进行比较，
然后将其插入到有序表中的适当位置，形成新的有序表。

算法原理
开始排序：从数组的第二个元素开始，这是因为单个元素默认已排序。
选择元素：选择当前元素，与前面的元素进行比较。
寻找位置：如果当前元素小于它前面的元素，则将前面的元素向后移动。
插入元素：重复步骤3直到找到当前元素的正确位置，然后将它插入。
重复过程：对数组中的每个未排序元素重复步骤2-4。
完成排序：当所有元素都被考虑过，数组排序完成。
'''
def gy_insert_sort(lst:list):

    for i_index in range(1,len(lst),1):#unsorted list
        insert_val = lst[i_index]
        temp_index = -1
        #print("insert_val = ",insert_val)
        for j_index in range(i_index - 1,-1,-1):
            #print("j_index = ",j_index)
            if (insert_val < lst[j_index]):
                lst[j_index + 1] = lst[j_index]
                temp_index = j_index
            else:
                break
        if (-1 != temp_index):
            lst[temp_index] = insert_val
        #print(lst)
    return

#insert sort
def py_test_2_3():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221]
    gy_insert_sort(gy_lst)
    print(gy_lst)
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    gy_insert_sort(gy_lst)
    print(gy_lst)
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532]
    gy_insert_sort(gy_lst)
    print(gy_lst)
    return

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_1.(pop_sort)
    2.py_test_2_2.(quick sort)
    3.py_test_2_3.(insert sort)
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_1,
        "2" : py_test_2_2,
        "3" : py_test_2_3
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()