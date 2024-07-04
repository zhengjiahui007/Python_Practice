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
        for j in range(0,len(lst) - 1 - i,1):
            if (lst[j] > lst[j + 1]):
                lst[j],lst[j + 1] = lst[j + 1],lst[j]
    return lst

#pop_sort
def py_test_2_1():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221]
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
        print("2 lst = ",lst)
        while ((i_start < j_end) and (lst[i_start] <= pivot)):
            i_start += 1
        #print("i_start = ",i_start)
        lst[j_end] = lst[i_start]
        print("1 lst = ",lst)

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
def gy_quick_sort_1(lst:list,start_index:int,end_index:int):
    if (start_index >= end_index):
        return

    i_start = start_index
    j_end = end_index
    pivot = lst[start_index]
    print("pivot = ",pivot)
    while (i_start < j_end):
        while ((i_start < j_end) and (lst[j_end] >= pivot)):
            j_end -= 1
        lst[j_end],lst[i_start] = lst[i_start],lst[j_end]
        #print("2 lst = ",lst)
        while ((i_start < j_end) and (lst[i_start] <= pivot)):
            i_start += 1
        lst[j_end],lst[i_start] = lst[i_start],lst[j_end]
        #print("1 lst = ",lst)

    print("i_start = ",i_start," j_end = ",j_end)
    print("lst = ",lst)
    #lst[j_end] = pivot
    gy_quick_sort_1(lst,start_index,i_start - 1)
    gy_quick_sort_1(lst,i_start + 1,end_index)
    return

#quick_sort
def py_test_2_2():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221]
    gy_quick_sort(gy_lst,0,len(gy_lst) - 1)
    print(gy_lst)
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    gy_quick_sort_1(gy_lst,0,len(gy_lst) - 1)
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
        #print(temp_index,lst)
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

def gy_Shell_sort(lst:list):
    gy_lst_len = len(lst)
    gy_step = gy_lst_len//2
    temp_lst = []
    while (gy_step > 0):
        # print("gy_step = ",gy_step)
        for i in range(0,gy_step,1):
            # print("i = ",i)
            temp_lst = []
            for j in range(i,gy_lst_len,gy_step):
                # print("j = ",j)
                temp_lst.append(lst[j])
            # print("temp_lst = ",temp_lst)
            gy_insert_sort(temp_lst)
            for j in range(i,gy_lst_len,gy_step):
                lst[j] = temp_lst[j // gy_step]
            #sorted_lst += (temp_lst)
            # print("1 lst = ",temp_lst)
        gy_step //= 2
        # print(" lst = ",lst)

    return lst

#Shell's sort
def py_test_2_4():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221,6356]
    gy_Shell_sort(gy_lst)
    print(gy_lst)
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    gy_Shell_sort(gy_lst)
    print(gy_lst)
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532]
    gy_Shell_sort(gy_lst)
    print(gy_lst)
    return

'''
归并操作的工作原理如下：
第一步：申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
第二步：设定两个指针，最初位置分别为两个已经排序序列的起始位置
第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
重复步骤3直到某一指针超出序列尾
将另一序列剩下的所有元素直接复制到合并序列尾
'''
def gy_merge_sort_loop(lst:list):
    lst_len = len(lst)
    temp_lst = []
    for i in lst:
        temp_lst.append([i])
    # print(temp_lst)
    gap_n = 1
    while (gap_n <= (lst_len)):
        # print("gap_n = {} , lst_len = {}.".format(gap_n,lst_len))
        merged_sort_lst = []
        for i_index in range(0,len(temp_lst),2):
            k,j = 0,0
            temp_sort_lst = []
            # print("i_index = {} len(temp_lst) = {} .".format(i_index,len(temp_lst)))
            if ((i_index + 1) >= len(temp_lst)):
                merged_sort_lst.append(copy.deepcopy(temp_lst[i_index]))
            else:
                # print("{} {} {}".format(i_index,k,j))
                while ((k < len(temp_lst[i_index])) and (j < len(temp_lst[i_index + 1]))):
                    if (temp_lst[i_index][k] < temp_lst[i_index + 1][j]):
                        temp_sort_lst.append(temp_lst[i_index][k])
                        k += 1
                    else:
                        temp_sort_lst.append(temp_lst[i_index + 1][j])
                        j += 1
                if (k == len(temp_lst[i_index])):
                    temp_sort_lst.extend(temp_lst[i_index + 1][j:])
                elif (j == len(temp_lst[i_index + 1])):
                    temp_sort_lst.extend(temp_lst[i_index][k:])
                merged_sort_lst.append(copy.deepcopy(temp_sort_lst))
                del temp_sort_lst[::]
            # print("merged_sort_lst = ",merged_sort_lst)
        gap_n *= 2
        del temp_lst[::]
        temp_lst = copy.deepcopy(merged_sort_lst)
        # print("0 temp_lst = ",temp_lst)
        del merged_sort_lst[::]
    # print("1 temp_lst = ",temp_lst)
    return temp_lst[0]

def gy_merge_list(l_lst:list,r_lst:list):
    l_index,r_index = 0,0
    temp_sort_lst = []
    while ((l_index < len(l_lst)) and (r_index < len(r_lst))):
        if (l_lst[l_index] < r_lst[r_index]):
            temp_sort_lst.append(l_lst[l_index])
            l_index += 1
        else:
            temp_sort_lst.append(r_lst[r_index])
            r_index += 1
    if (l_index == len(l_lst)):
        temp_sort_lst.extend(r_lst[r_index::])
    elif (r_index == len(r_lst)):
        temp_sort_lst.extend(l_lst[l_index::])

    #print("temp_sort_lst = ",temp_sort_lst)
    return temp_sort_lst

def gy_merge_sort_recursive(lst:list):
    if (1 >= len(lst)):
        #print("111 lst = ",lst)
        return lst

    gy_mid = len(lst)//2
    #print("gy_mid = ",gy_mid)
    l_lst = gy_merge_sort_recursive(lst[:gy_mid:])
    #print("l_lst = ",l_lst)
    r_lst = gy_merge_sort_recursive(lst[gy_mid::])
    #print("r_lst = ",r_lst)
    #print("l_lst = ",l_lst," r_lst = ",r_lst)
    return gy_merge_list(l_lst,r_lst)

#merge sort
def py_test_2_5():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221,6356,685,231,87,90]
    print(gy_merge_sort_loop(gy_lst))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_merge_sort_loop(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,9]
    print(gy_merge_sort_recursive(gy_lst))
    return

def gy_select_sort(lst:list):
    for i in range(0,len(lst),1):
        for j in range(i,len(lst),1):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]

    return lst

#select sort
def py_test_2_6():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221,6356,685,231,87,90]
    print(gy_select_sort(gy_lst))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_select_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,9]
    print(gy_select_sort(gy_lst))
    return

'''
堆排序的原理与步骤
堆排序基于一个叫做“堆”的数据结构，通常是一个最大堆或最小堆。
在最大堆中，父节点的值总是大于或等于其子节点的值；
在最小堆中，父节点的值总是小于或等于其子节点的值。以下是堆排序的基础步骤：

堆排序步骤

构建初始堆：将待排序的数组元素构建成一个最大堆（或最小堆）。

从最后一个非叶子节点开始，向上调整每个子树，使其成为一个最大堆。
时间复杂度：O(n)
堆调整与排序

移除堆顶元素：将堆顶元素（最大或最小）与堆的最后一个元素交换。
堆大小减一：现在，堆的大小减少了1，最后一个元素是之前的最大（或最小）元素。
堆调整：将交换后的新堆顶元素向下调整，使其重新成为一个最大堆。
重复：持续进行以上步骤，直到堆的大小减少到1。
时间复杂度：每次调整的复杂度是 O(log n)，共需要 n 次调整，所以总时间复杂度是 O(n log n)。

https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%A0%91?fromModule=lemma_search-box

①节点：包含一个数据元素及若干指向子树分支的信息 [5]。
②节点的度：一个节点拥有子树的数目称为节点的度 [5]。
③叶子节点：也称为终端节点，没有子树的节点或者度为零的节点 [5]。
④分支节点：也称为非终端节点，度不为零的节点称为非终端节点 [5]。
⑤树的度：树中所有节点的度的最大值 [5]。
⑥节点的层次：从根节点开始，假设根节点为第1层，根节点的子节点为第2层，依此类推，如果某一个节点位于第L层，则其子节点位于第L+1层 [5]。
⑦树的深度：也称为树的高度，树中所有节点的层次最大值称为树的深度 [5]。
⑧有序树：如果树中各棵子树的次序是有先后次序，则称该树为有序树 [5]。
⑨无序树：如果树中各棵子树的次序没有先后次序，则称该树为无序树 [5]。
⑩森林：由m（m≥0）棵互不相交的树构成一片森林。如果把一棵非空的树的根节点删除，则该树就变成了一片森林，森林中的树由原来根节点的各棵子树构成 [5]。

⑤ 对于具有n个结点的完全二叉树，如果按照从上至下从左至右的数组顺序对所有节点从0开始编号，则对于序号为i的结点有：
 ·若i>0，i位置节点的双亲序号：(i-1)/2；i=0，i为根节点编号，无双亲节点
 · 若2i+1<n，左孩子序号：2i+1，2i+1>=n则无左孩子
 · 若2i+2<n，右孩子序号：2i+2，2i+2>=n则无右孩子
 最后一个非叶子节点的index = len/2 - 1
在完全二叉树中， 第一个非叶子结点 其实就是 最后一个叶子结点的父节点。
假定父节点为i；则 其左叶子为2i+1 ， 右叶子为2i+2；
则当叶子节点为n-1时，就有了上面这位兄弟的n/2 -1 的结论

n - 1 = 2i + 2
i = (n - 3)/2
n - 1 = 2i+1
i = (n - 2)/2 = n/2 -1 
https://baijiahao.baidu.com/s?id=1792470750878885698&wfr=spider&for=pc

'''

def gy_adjust_heap(lst:list,parent_index:int,lst_size:int):
    # the left and right child index
    left_child = 2 * parent_index + 1
    right_child = 2 * parent_index + 2
    # print("parent_index = {0} left_child = {1} right_child = {2} lst_size = {3} ".format(parent_index,left_child,right_child,lst_size))
    ''' method 1
    if ((lst_size > left_child) and (lst[left_child] > lst[parent_index])):
        lst[left_child],lst[parent_index] = lst[parent_index],lst[left_child]
        gy_adjust_heap(lst,left_child,lst_size)

    if ((lst_size > right_child) and (lst[right_child] > lst[parent_index])):
        lst[right_child],lst[parent_index] = lst[parent_index],lst[right_child]
        gy_adjust_heap(lst,right_child,lst_size)
    '''
    #method 2
    max_index = parent_index
    if (parent_index < (lst_size//2)):
        if ((lst_size > left_child) and (lst[left_child] > lst[max_index])):
            max_index = left_child
        if ((lst_size > right_child) and (lst[right_child] > lst[max_index])):
            max_index = right_child
        if (max_index != parent_index):
            lst[max_index],lst[parent_index] = lst[parent_index],lst[max_index]
            # adjust the below sub tree
            gy_adjust_heap(lst,max_index,lst_size)

    return

def gy_build_heap(lst:list):
    for i in range(len(lst)//2 - 1,-1,-1):
        gy_adjust_heap(lst,i,len(lst))
        # print("lst = ",lst)
    return

def gy_heap_sort(lst:list):
    # build a Max heap or Min heap
    '''
      9212, 
      1122, 6356, 
      908, 123, 1123, 685, 
      87, 321, 3, 54, 2, 221, 7, 231, 
      1, 12, 90

      9212, 
      1122, 6356, 
      908, 123, 1123, 685,
      90, 321, 3, 54, 221, 2, 7, 231, 
      87, 12, 1


      1122,
      908,1123,
      1,3,2,7,
      12,321,123,54,221,6356,685,231,
      87,90,9212

    '''
    gy_build_heap(lst)
    for i in range(len(lst) - 1,-1,-1):
        lst[0],lst[i] = lst[i],lst[0]
        gy_adjust_heap(lst,0,i) #i is the len
    return lst

#heap sort
def py_test_2_7():
    gy_lst = [1122,908,1123,1,3,2,7,12,321,123,54,221,6356,685,231,87,90,9212]
    print(gy_heap_sort(gy_lst))
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    print(gy_heap_sort(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,9]
    print(gy_heap_sort(gy_lst))
    return

if ("__main__" == __name__):
    dis_playmessage = """
    0.Exit.
    1.py_test_2_1.(pop sort)
    2.py_test_2_2.(quick sort)
    3.py_test_2_3.(insert sort)
    4.py_test_2_4.(Shell's sort)
    5.py_test_2_5.(merge sort)
    6.py_test_2_6.(select sort)
    7.py_test_2_7.(heap sort)
    """
    test_dict = {
        "0" : py_test_exit,
        "1" : py_test_2_1,
        "2" : py_test_2_2,
        "3" : py_test_2_3,
        "4" : py_test_2_4,
        "5" : py_test_2_5,
        "6" : py_test_2_6,
        "7" : py_test_2_7
    }
    print(dis_playmessage)
    while True:
        gy_choice = input("Please input the test choice : ")
        test_dict[gy_choice]()