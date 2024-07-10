# -*-coding : utf-8-*-
# !usr/bin/env/ python3
# __author__ : "Garry Zheng"
# __Date__ : 2024-07-06

import os,time,sys,math,copy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Test_com import py_test_exit
from collections.abc import Iterable


'''
https://blog.csdn.net/The_emperoor_man/article/details/131704398
'''

##########################pop_sort##########################################
def gy_pop_sort(lst:list,sort_flag:bool = True):
    for j in range(0,len(lst),1):
        for i in range(0,len(lst) - 1 - j,1):
            if ((True == sort_flag) and (lst[i] > lst[i + 1])):
                lst[i],lst[i + 1] = lst[i + 1],lst[i]
            elif ((False == sort_flag) and (lst[i] < lst[i + 1])):
                lst[i],lst[i + 1] = lst[i + 1],lst[i]
    return lst

def py_test_5_1():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    print(gy_pop_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    print(gy_pop_sort(gy_lst,False))
    return

##########################quick_sort##########################################
def gy_quick_sort_recursive(lst:list,start_index:int,end_index:int,sort_flag:bool = True):
    if (start_index >=  end_index):
        # print("@@@@@ start_index = {} end_index = {}".format(start_index,end_index))
        return
    pivot_index = start_index
    pivot = lst[start_index]
    left_index = start_index
    right_index = end_index
    # print("0 left_index = {} right_index = {} pivot = {} pivot_index = {}".format(left_index,right_index,pivot,pivot_index))
    # print("0 lst = ",lst)
    while (left_index < right_index):
        if (True == sort_flag):
            while ((left_index < right_index) and (pivot <= lst[right_index])):
                right_index -= 1
            while ((left_index < right_index) and (pivot >= lst[left_index])):
                left_index += 1
        elif (False == sort_flag):
            while ((left_index < right_index) and (pivot >= lst[right_index])):
                right_index -= 1
            while ((left_index < right_index) and (pivot <= lst[left_index])):
                left_index += 1
        if (left_index < right_index):
            lst[right_index],lst[left_index] = lst[left_index],lst[right_index]
        # print("left_index = {} right_index = {}".format(left_index,right_index))
        # print("1 lst = ",lst)
    #if ((left_index == right_index) and (lst[pivot_index] > lst[right_index])):
    lst[pivot_index],lst[right_index] = lst[right_index],lst[pivot_index]
    # print("2 left_index = {} right_index = {}".format(left_index,right_index))
    # print(" end1 2 lst = ",lst)
    # print("&&&&&&&&& start_index = {} left_index = {}".format(start_index,left_index))
    gy_quick_sort_recursive(lst,start_index,left_index - 1,sort_flag)
    # print(" end2 left_index = {} end_index = {}".format(left_index,end_index))
    gy_quick_sort_recursive(lst,left_index + 1,end_index,sort_flag)
    return lst

def py_test_5_2():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    print(gy_quick_sort_recursive(gy_lst,0,len(gy_lst) - 1))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_quick_sort_recursive(gy_lst,0,len(gy_lst) - 1,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_quick_sort_recursive(gy_lst,0,len(gy_lst) - 1))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_quick_sort_recursive(gy_lst,0,len(gy_lst) - 1,False))
    return


##########################insert_sort##########################################
def gy_insert_sort(lst:list,sort_flag:bool = True):
    #sort_flag : False -->ascending(升序) True---> descending(降序)
    for i in range(1,len(lst),1):
        insert_index = -1
        insert_val = lst[i]
        # print("insert_val = ",insert_val)
        # print("00 lst = ",lst)
        for j in range(i - 1,-1,-1):
            # print("lst[{}] = {}".format(j,lst[j]))
            if ((True == sort_flag) and (insert_val < lst[j])):
                #lst[j + 1],lst[j] = lst[j],lst[j + 1]
                lst[j + 1] = lst[j]
                insert_index = j
                # print("11 lst = ",lst," j = ",j)
                continue
            elif ((False == sort_flag) and (insert_val > lst[j])):
                #lst[j + 1],lst[j] = lst[j],lst[j + 1]
                lst[j + 1] = lst[j]
                insert_index = j
                # print("11 lst = ",lst," j = ",j)
                continue
            else:
                #lst[j + 1] = insert_val
                # print("22 lst = ",lst," j = ",j)
                break
        # print("22 insert_index = ",insert_index)
        if (-1 != insert_index):
            lst[insert_index] = insert_val
        # print("33 lst = ",lst," j = ",j)
    return lst

def py_test_5_3():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
    # gy_lst = [1122,908,1123,61,3,62]
    print(gy_insert_sort(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_insert_sort(gy_lst,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_insert_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_insert_sort(gy_lst,False))
    return

##########################Shell's_sort##########################################
def gy_shell_sort(lst:list,sort_flag:bool = True):
    len_lst = len(lst)
    interval_lst = len_lst//2
    while (0 < interval_lst):
        # print("0 lst = ",lst)
        for j in range(0,interval_lst,1):
            temp_lst = []
            for i in range(j,len(lst),interval_lst):
                temp_lst.append(lst[i])
            # print("0 temp_lst = ",temp_lst)
            gy_insert_sort(temp_lst,sort_flag)
            # print("1 temp_lst = ",temp_lst)
            for i in range(j,len(lst),interval_lst):
                lst[i] = temp_lst[i // interval_lst]
            del temp_lst[::]
        # print("1 lst = ",lst)    
        interval_lst //= 2

    return lst

def py_test_5_4():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_shell_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_shell_sort(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_shell_sort(gy_lst,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_shell_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_shell_sort(gy_lst,False))
    return

########################## Merge_sort##########################################
def gy_merge_sort_loop(lst:list,sort_flag:bool = True):
    gy_lst_len = len(lst)
    gy_sorted_lst = []
    for i in lst:
        gy_sorted_lst.append([i])
    # print("0 gy_sorted_lst = ",gy_sorted_lst)
    gap_n = 1
    while (gap_n < gy_lst_len):
        temp_sorted_lst = []
        for i_index in range(0,len(gy_sorted_lst),2):
            if (len(gy_sorted_lst) == (i_index + 1)):
                temp_sorted_lst.append(gy_sorted_lst[i_index])
                break
            merged_sorted_tmp_lst = []
            i,j = 0,0
            # for k in range(0,len(gy_sorted_lst[i_index]),1):
            while ((i < len(gy_sorted_lst[i_index])) and (j < len(gy_sorted_lst[i_index + 1]))):
                # print("i = %d j = %d "%(i,j))
                if (True == sort_flag):
                    if (gy_sorted_lst[i_index][i] < gy_sorted_lst[i_index + 1][j]):
                        merged_sorted_tmp_lst.append(gy_sorted_lst[i_index][i])
                        i += 1
                    else:
                        merged_sorted_tmp_lst.append(gy_sorted_lst[i_index + 1][j])
                        j += 1
                elif (False == sort_flag):
                    if (gy_sorted_lst[i_index][i] > gy_sorted_lst[i_index + 1][j]):
                        merged_sorted_tmp_lst.append(gy_sorted_lst[i_index][i])
                        i += 1
                    else:
                        merged_sorted_tmp_lst.append(gy_sorted_lst[i_index + 1][j])
                        j += 1
            if (i == len(gy_sorted_lst[i_index])):
                merged_sorted_tmp_lst.extend(gy_sorted_lst[i_index + 1][j::1])
            elif (j == len(gy_sorted_lst[i_index + 1])):
                merged_sorted_tmp_lst.extend(gy_sorted_lst[i_index][i::1])
            temp_sorted_lst.append(copy.deepcopy(merged_sorted_tmp_lst))
            # print(" merged_sorted_tmp_lst = ",merged_sorted_tmp_lst)
            # print(" temp_sorted_lst = ",temp_sorted_lst)
            del merged_sorted_tmp_lst[::]
        del gy_sorted_lst[::]
        gy_sorted_lst = copy.deepcopy(temp_sorted_lst)
        del temp_sorted_lst[::]
        gap_n *= 2
    del lst[::]
    lst = gy_sorted_lst[0]
    return lst

def gy_merge_list(l_lst:list,r_lst:list,sort_flag:bool = True):

    merged_sorted_tmp_lst = []
    i,j = 0,0
    while ((i < len(l_lst)) and (j < len(r_lst))):
        # print("i = %d j = %d "%(i,j))
        if (True == sort_flag):
            if (l_lst[i] < r_lst[j]):
                merged_sorted_tmp_lst.append(l_lst[i])
                i += 1
            else:
                merged_sorted_tmp_lst.append(r_lst[j])
                j += 1
        elif (False == sort_flag):
            if (l_lst[i] > r_lst[j]):
                merged_sorted_tmp_lst.append(l_lst[i])
                i += 1
            else:
                merged_sorted_tmp_lst.append(r_lst[j])
                j += 1
    if (i == len(l_lst)):
        merged_sorted_tmp_lst.extend(r_lst[j::1])
    elif (j == len(r_lst)):
        merged_sorted_tmp_lst.extend(l_lst[i::1])

    # print(" merged_sorted_tmp_lst = ",merged_sorted_tmp_lst)
    return merged_sorted_tmp_lst

def gy_merge_sort_recursive(lst:list,sort_flag:bool = True):
    if (len(lst) <= 1):
        return lst

    lst_mid = len(lst)//2
    # print(" lst =  ",lst)
    left_lst = gy_merge_sort_recursive(lst[:lst_mid:1],sort_flag)
    # print(" left_lst =  ",left_lst)
    right_lst = gy_merge_sort_recursive(lst[lst_mid::1],sort_flag)
    # print(" right_lst =  ",right_lst)
    return gy_merge_list(left_lst,right_lst,sort_flag)

def py_test_5_5():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_merge_sort_loop(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_merge_sort_loop(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_merge_sort_loop(gy_lst,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_merge_sort_loop(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_merge_sort_loop(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_merge_sort_recursive(gy_lst,True))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_merge_sort_recursive(gy_lst,False))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_merge_sort_recursive(gy_lst,True))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_merge_sort_recursive(gy_lst,False))
    return

########################## Select_sort##########################################
def gy_select_sort(lst:list,sort_flag:bool = True):
    for i in range(0,len(lst),1):
        pivot_index = i
        for j in range(i,len(lst),1):
            if (True == sort_flag):
                if (lst[pivot_index] > lst[j]):
                    # lst[i],lst[j] = lst[j],lst[i]
                    pivot_index = j
            elif (False == sort_flag):
                if (lst[pivot_index] < lst[j]):
                    # lst[i],lst[j] = lst[j],lst[i]
                    pivot_index = j
        lst[i],lst[pivot_index] = lst[pivot_index],lst[i]
    return lst


def py_test_5_6():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_select_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34]
    print(gy_select_sort(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_select_sort(gy_lst,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_select_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_select_sort(gy_lst,False))
    return


########################## Heap_sort##########################################
# https://blog.csdn.net/hehedadaq/article/details/111714669
# index : 0 - (n - 1) , n is the length of list 
# parent i --- > left : 2*i + 1, right : 2*i + 2 , i is 0 --- n/2 - 1
'''
line k (start from 1),the index in k is J (start from 1) , the index in list is P:
The total nodes in k line 2 ** (k - 1) , 
The index of the node k in the list is P = ((2 ** (k - 1) - 1) - 1) + (J) = 2 ** (k - 1) - 2 + J
left_child_index = P + (2 ** (k - 1) - J) + 2 * (J - 1) + 1 = P + 2 ** (k - 1) - J + 2 * J - 2 + 1
                 = P + 2 ** (k - 1) + J - 1 = P + P + 2 - 1 = 2 * P + 1
so :
left_child_index = 2 * P + 1
right_child_index = 2 * P + 2
The last index of node is n - 1,
so the index of the first non-leaf-node : n - 1 = 2 * P + 1 ---> P = (n/2) - 1
'''

def gy_adjust_heap(lst:list,p_index:int,lst_size:int,sort_flag:bool = True):
    if (p_index > (lst_size//2 - 1)):
        # print(" p_index = ",p_index," lst_size = ",lst_size)
        return

    l_child_index = 2 * p_index + 1
    r_child_index = 2 * p_index + 2
    # print("p_index = {} l_child_index = {} r_child_index = {} ".format(p_index,l_child_index,r_child_index))
    if sort_flag:
        if ((l_child_index < lst_size) and (lst[l_child_index] > lst[p_index])):
            lst[l_child_index],lst[p_index] = lst[p_index],lst[l_child_index]
            gy_adjust_heap(lst,l_child_index,lst_size,sort_flag)
        if ((r_child_index < lst_size) and (lst[r_child_index] > lst[p_index])):
            lst[r_child_index],lst[p_index] = lst[p_index],lst[r_child_index]
            gy_adjust_heap(lst,r_child_index,lst_size,sort_flag)
    elif not sort_flag:
        if ((l_child_index < lst_size) and (lst[l_child_index] < lst[p_index])):
            lst[l_child_index],lst[p_index] = lst[p_index],lst[l_child_index]
            gy_adjust_heap(lst,l_child_index,lst_size,sort_flag)
        if ((r_child_index < lst_size) and (lst[r_child_index] < lst[p_index])):
            lst[r_child_index],lst[p_index] = lst[p_index],lst[r_child_index]
            gy_adjust_heap(lst,r_child_index,lst_size,sort_flag)
    """ 
    max_index = p_index
    if sort_flag:
        if ((l_child_index < lst_size) and (lst[l_child_index] > lst[max_index])):
            max_index = l_child_index
        if ((r_child_index < lst_size) and (lst[r_child_index] > lst[max_index])):
            max_index = r_child_index
    elif not sort_flag:
        if ((l_child_index < lst_size) and (lst[l_child_index] < lst[max_index])):
            max_index = l_child_index
        if ((r_child_index < lst_size) and (lst[r_child_index] < lst[max_index])):
            max_index = r_child_index

    if (max_index != p_index):
        lst[max_index],lst[p_index] = lst[p_index],lst[max_index]
        # adjust the below sub tree , only the max_index has been changed,so need build heap again with the max_index
        gy_adjust_heap(lst,max_index,lst_size,sort_flag)
    """
    return

def gy_heap_sort(lst:list,sort_flag:bool = True):
    # 1. build heap
    lst_size = len(lst)
    for i in range(((lst_size//2) - 1),-1,-1):
        gy_adjust_heap(lst,i,lst_size,sort_flag)
    # print(" 00 lst = ",lst)
    #gy_adjust_heap(lst,0,lst_size,sort_flag)
    # 2. adjust heap
    for i in range(lst_size - 1,0,-1):
        lst[i],lst[0] = lst[0],lst[i]
        # the 0 node has been changed, so heapify the 0 node again
        gy_adjust_heap(lst,0,i,sort_flag)
        # print(" 11 lst = ",lst)
    return lst

def py_test_5_7():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,1560]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,43,3248,674,21,90,3,12]
    print(gy_heap_sort(gy_lst,False))
    gy_lst = [1122,908,1123,61,3,9,12,10]
    print(gy_heap_sort(gy_lst,False))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_heap_sort(gy_lst,False))
    return


if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_5_1.(pop sort)
    2.py_test_5_2.(quick sort)
    3.py_test_5_3.(insert sort)
    4.py_test_5_4.(Shell's sort)
    5.py_test_5_5.(merge sort)
    6.py_test_5_6.(select sort)
    7.py_test_5_7.(heap sort)
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_5_1,
        "2" : py_test_5_2,
        "3" : py_test_5_3,
        "4" : py_test_5_4,
        "5" : py_test_5_5,
        "6" : py_test_5_6,
        "7" : py_test_5_7
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()