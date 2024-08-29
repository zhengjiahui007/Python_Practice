# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-07-26"

import os,sys,time,datetime,calendar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit

#Palindrome 回文
def gy_isPalindrome(lst:str):
    gy_str_letter_number = []
    for i_str in lst:
        if i_str.isalnum() or i_str.isalpha():
             gy_str_letter_number.append(i_str)
    # print(f"gy_str_letter_number = {gy_str_letter_number}")
    # for i in range(0,len(gy_str_letter_number)//2,1):
    # print(gy_str_letter_number[0:len(gy_str_letter_number)//2:1])
    # gy_str_letter_number[0:len(gy_str_letter_number)//2 + 1:1]
    # print(gy_str_letter_number[-1:(-len(gy_str_letter_number)//2):-1])
    if gy_str_letter_number[0::1] == gy_str_letter_number[-1::-1]:
        return True
    return False


def gy_test_7_1():
    print(gy_isPalindrome("1234554321"))
    print(gy_isPalindrome("123abcdcba321"))
    print(gy_isPalindrome("123adcba321"))
    print(gy_isPalindrome("人过大佛寺，寺佛大过人"))

    ty_str = "1357908642"
    print(ty_str[-1:0:-1])
    print(ty_str[-1::-1])
    print(ty_str[::-1])
    print(ty_str[::1])
    print(ty_str[::])
    return

def gy_test_7_2():
    gy_str_input = input("Please input an sentance : ")
    start_i = -1
    start_len = 0
    gy_str_lst = []
    for i in range(0,len(gy_str_input),1):
        if gy_str_input[i].isalpha():
            if (0 == start_len):
                start_i = i
            start_len += 1
        else:
            if ((i != start_i) and (-1 != start_i)):
                gy_str_lst.append(gy_str_input[start_i:i:1])
                start_i = -1
            gy_str_lst.append(gy_str_input[i])
            start_len = 0
    print("gy_str_lst = ",gy_str_lst)
    gy_str_lst.reverse()
    gy_str_rever = "".join(gy_str_lst)
    # for i in range(len(gy_str_lst) - 1,-1,-1):
    #     # print("gy_str_lst[i] = ",gy_str_lst[i])
    #     gy_str_rever = gy_str_rever + gy_str_lst[i]
    #     print("id = ",id(gy_str_rever))
    print("gy_str_rever = ",gy_str_rever)
    return

'''
find the peak number in list
'''
def gy_find_peak(lst:list):
    if (2 >= len(lst)):
        return None

    gy_lst_peak = []
    for i in range(0,len(lst),1):
        gy_peak_flag = False
        if ((0 == i) and (lst[i] > lst[i + 1])):
            gy_peak_flag = True
        elif (((len(lst) - 1) == i) and (lst[i] > lst[i - 1])):
            gy_peak_flag = True
        elif ((lst[i] > lst[i - 1]) and (lst[i] > lst[i + 1])):
            gy_peak_flag = True
        if gy_peak_flag:
            gy_lst_peak.append((i,lst[i]))

    return gy_lst_peak

def gy_test_7_3():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,43,3248,674,21,90,3,12]
    print(gy_find_peak(gy_lst))
    gy_lst = [1236556,12354,221,1342,332,12,6790,4532,90,32]
    print(gy_find_peak(gy_lst))
    return

'''
string to int
'''
GY_MAX_INT = (2 ** 31 - 1)
GY_MIN_INT = ((-2) ** 31)
def gy_str_to_int(in_str:str):
    gy_int = 0
    try:
        start_number_index = -1
        plus_minus = 0
        for i in range(0,len(in_str),1):
            if (not in_str[i].isspace() or ('+' == in_str[i]) or ('-' == in_str[i])):
                start_number_index = i
                plus_minus = 1
                if ('-' == in_str[i]):
                    plus_minus = -1
                break
        # print(f"start_number_index = {start_number_index} , plus_minus = {plus_minus} .")
        if (-1 == start_number_index):
            return gy_int

        gy_str = in_str[start_number_index::1]
        # print(f"gy_str = {gy_str} .")
        if ((1 == len(gy_str)) and (('+' == gy_str[0]) or ('-' == gy_str[0]))):
            return gy_int

        if (('+' == gy_str[0]) or ('-' == gy_str[0])):
            if not gy_str[1].isdigit():
                return gy_int
        elif not gy_str[0].isdigit():
            return gy_int

        gy_str_lst = []
        for j in range(0,len(gy_str),1):
            if (gy_str[j].isdigit() or ('+' == gy_str[j]) or ('-' == gy_str[j])):
                gy_str_lst.append(gy_str[j])
        print(f"gy_str_lst = {gy_str_lst} .")
        gy_int = int("".join(gy_str_lst))
        print(f"The {gy_int} is {type(gy_int)}")
        if (gy_int > GY_MAX_INT):
            return GY_MAX_INT
        elif (gy_int < GY_MIN_INT):
            return GY_MIN_INT
        else:
            return gy_int
    except Exception as e:
        print(f"An error occured {e}")
    return gy_int

def gy_test_7_4():
    print(gy_str_to_int("!  123"))
    print(gy_str_to_int(" -45! abc 123"))
    print(gy_str_to_int(" # +45! abc 123"))
    print(gy_str_to_int("  +45! abc 123"))
    print(gy_str_to_int("  3147483 647"))
    print(gy_str_to_int("  -3147483 647"))
    return


def gy_mountain_array(lst:list):
    if (3 > len(lst)):
        return False

    peak_index = -1
    for i in range(1,len(lst),1):
        if (lst[i - 1] < lst[i]):
            continue
        else:
            peak_index = (i - 1)
            print(f"The peak index is {peak_index} .")
            for j in range(peak_index + 1,len(lst),1):
                if (lst[j - 1] > lst[j]):
                    continue
                else:
                    j = j - 1
                    break
            break
    print(f"The j is {j} .")
    if (j == (len(lst) - 1)):
        print(f"The peak index is {peak_index} .")
        return True
    return False

def gy_test_7_5():
    gy_lst = [1122,908,1123,61,3,62,47,12,321,123,54,221,34,43,3248,674,21,90,3,12]
    print("The gy_lst {mountain_flag} mountain array !".format(mountain_flag = 'is' if gy_mountain_array(gy_lst) else "is not"))
    gy_lst = [123,54,221,34,43,3248,674,21,90,3,12]
    print("The gy_lst {mountain_flag} mountain array !".format(mountain_flag = 'is' if gy_mountain_array(gy_lst) else "is not"))
    gy_lst = [123,221,334,443,3248,674,321,190,33,32]
    print("The gy_lst {mountain_flag} mountain array !".format(mountain_flag = 'is' if gy_mountain_array(gy_lst) else "is not"))
    return

def gy_count_one_bit(number_input:int):
    if not isinstance(number_input,int):
        return -1

    one_bit_count = 0
    while (0 != number_input):
        print("The (number_input&1) is  ",(number_input&1))
        if (1 == (number_input&1)):
            one_bit_count += 1
        number_input >>= 1

    return one_bit_count

def gy_test_7_6():
    one_bit_count = gy_count_one_bit(37498)
    print("The one_bit_count is  ",one_bit_count)
    return

# find the missing number in [1,N]
def gy_test_7_7():
    gy_lst = [2,5,4,1,12,8,9,3,6,7,11]
    gy_N = len(gy_lst) + 1
    sum_N = 0
    for i in range(1,gy_N + 1,1):
        sum_N += i
    sum_gy_lst = 0
    for j in gy_lst:
        sum_gy_lst += j
    gy_miss_number = sum_N - sum_gy_lst
    print("The miss number is ",gy_miss_number)

    # gy_lst_flag = [0 for i in range(0,len(gy_lst) + 1,1)]
    # print("The gy_lst_flag is ",gy_lst_flag)
    for j in range(1,len(gy_lst) + 1,1):
        if j not in gy_lst:
            break
    print("The miss number is ",j)
    return

def gy_add_bin_str(bin_str_0:str,bin_str_1:str):
    for i in bin_str_0:
        if (('0' != i) and ('1' != i)):
            return None
    for i in bin_str_1:
        if (('0' != i) and ('1' != i)):
            return None
    # method 2
    gy_bin_len_0 = len(bin_str_0)
    gy_bin_len_1 = len(bin_str_1)
    new_bin_str_0 = ""
    new_bin_str_1 = ""
    diff_0 = 0
    if (gy_bin_len_0 >= gy_bin_len_1):
        diff_0 = gy_bin_len_0 - gy_bin_len_1
        new_bin_str_1 = '0' * diff_0 + bin_str_1
        new_bin_str_0 = bin_str_0
    else:
        diff_0 = gy_bin_len_1 - gy_bin_len_0
        new_bin_str_0 = '0' * diff_0 + bin_str_0
        new_bin_str_1 = bin_str_1
    print(f"new_bin_str_0 = {new_bin_str_0} , new_bin_str_1 = {new_bin_str_1} !")
    gy_carry_num = 0
    gy_sum_bit = 0
    gy_sum_lst = []
    for index in range((len(new_bin_str_0) - 1),-1,-1):
        gy_sum_bit = 0
        gy_sum_bit = int(new_bin_str_0[index]) + int(new_bin_str_1[index]) + gy_carry_num
        gy_carry_num = 0
        if (2 == gy_sum_bit):
            gy_carry_num = 1
            gy_sum_bit = 0
        elif (3 == gy_sum_bit):
            gy_carry_num = 1
            gy_sum_bit = 1
        else:
            gy_carry_num = 0
        gy_sum_lst.append(str(gy_sum_bit))
    print("gy_sum_lst = ",gy_sum_lst)
    gy_sum_str = "".join(gy_sum_lst)

    print("gy_sum_str = ",gy_sum_str[::-1])

    # method 1
    gy_int_0 = int(bin_str_0,2)
    gy_int_1 = int(bin_str_1,2)
    print(f"gy_int_0 = {gy_int_0} , gy_int_1 = {gy_int_1} !")
    return bin(gy_int_0 + gy_int_1)

def gy_test_7_8():
    gy_bin_str_0 = '1100110101'
    gy_bin_str_1 =    '1011001'
    print(gy_add_bin_str(gy_bin_str_0,gy_bin_str_1))
    gy_bin_str_0 = '1111111111'
    gy_bin_str_1 = '1111111111'
    print(gy_add_bin_str(gy_bin_str_0,gy_bin_str_1))
    return

def gy_find_firstword(str_input:str):
    try:
        for i_val in str_input:
            if (('a' > i_val) or ('z' < i_val)):
                print(f"The string is not correct {str_input}!")
                return (-1,"")

        for i in range(0,len(str_input),1):
            i_val = str_input[i]
            new_str = str_input.replace(i_val," ",1)
            if i_val not in new_str:
                return (i,i_val)

    except Exception as e:
        print(f"An error occured {e}")
    return (-1,"")

def gy_test_7_9():
    print("The first lettet which appearing only once is ",gy_find_firstword("ureoiwufjdasdlklfksj"))
    print("The first lettet which appearing only once is ",gy_find_firstword("abcacd"))
    print("The first lettet which appearing only once is ",gy_find_firstword("eettgfaq"))
    return

def gy_plus_two_strings(str_0:str,str_1:str)->str:
    if ((not str_0.isdigit()) or (not str_1.isdigit())):
        return None

    gy_len_0 = len(str_0)
    gy_len_1 = len(str_1)
    new_str_0 = ""
    new_str_1 = ""
    diff_0 = 0
    if (gy_len_0 >= gy_len_1):
        diff_0 = gy_len_0 - gy_len_1
        new_str_1 = '0' * diff_0 + str_1
        new_str_0 = str_0
    else:
        diff_0 = gy_len_1 - gy_len_0
        new_str_0 = '0' * diff_0 + str_0
        new_str_1 = str_1
    # print(f"new_str_0 = {new_str_0} , new_str_1 = {new_str_1} !")
    gy_carry_num = 0
    gy_sum_bit = 0
    gy_sum_lst = []
    for index in range((len(new_str_0) - 1),-1,-1):
        gy_sum_bit = 0
        gy_sum_bit = int(new_str_0[index]) + int(new_str_1[index]) + gy_carry_num
        gy_carry_num = gy_sum_bit//10
        gy_sum_bit = gy_sum_bit%10
        gy_sum_lst.insert(0,str(gy_sum_bit))
        if (0 == index):
            if (gy_carry_num != 0):
               gy_sum_lst.insert(0,str(gy_carry_num)) 
    # print("gy_sum_lst = ",gy_sum_lst)
    gy_sum_str = "".join(gy_sum_lst)
    return gy_sum_str

def gy_multi_strs(str_0:str,str_1:str)->str:
    if ((not str_0.isdigit()) or (not str_1.isdigit())):
        return None
    '''
    str_0 * str_1[i]:
        str_0[j] * str_1[i],store the result as string,need * 10(n - 1) , then sum the list as one result str_0 * str_1[i]
    sum the list of all the str_0 * str_1[i],get the total result
    '''
    str_0_reversed = str_0[::-1]
    str_1_reversed = str_1[::-1]
    # store str_0[j] * str_1[i] result list
    multi_single_result = []
    single_multi_single_result = 0
    ten_multi_str0 = 1
    ten_multi_str1 = 1
    # print(str_0," * ",str_1)
     # store str_0 * str_1[i] result list
    multi_single_sum_result = []
    for i_val in str_1_reversed:
        multi_single_result = []
        ten_multi_str0 = 1
        for j_val in str_0_reversed:
            single_multi_single_result = int(j_val) * int(i_val)
            multi_single_result.append(str(single_multi_single_result) + (ten_multi_str0 - 1) * '0')
            single_multi_single_result = 0
            ten_multi_str0 += 1
        # print("multi_single_result = ",multi_single_result)
        plus_res = multi_single_result[0]
        for i in range(1,len(multi_single_result),1):
            plus_res = gy_plus_two_strings(plus_res,multi_single_result[i])
        # print("plus_res = ",plus_res)
        multi_single_sum_result.append(plus_res + (ten_multi_str1 - 1) * '0')
        ten_multi_str1 += 1
        # print("multi_single_sum_result = ",multi_single_sum_result)
    total_result = multi_single_sum_result[0]
    for j in range(1,len(multi_single_sum_result),1):
        total_result = gy_plus_two_strings(total_result,multi_single_sum_result[j])
    return total_result

def gy_test_7_10():
    a = "678"
    b = "89"
    print(f"The {a} * {b} = {gy_multi_strs(a,b)} ")
    # print("The result is ",gy_multi_strs("6078","19089"))
    a = "6078"
    b = "19089"
    print(f"The {a} * {b} = {gy_multi_strs(a,b)} ")
    a = "123424234132423416078"
    b = "4314376574569345657819089"
    print("The {0} * {1} = {2} ".format(a,b,gy_multi_strs(a,b)))
    a = "123424234132423416078"
    b = "90"
    print("The {0} * {1} = {2} ".format(a,b,gy_multi_strs(a,b)))
    return

if (__name__ == "__main__"):
    dis_playmessage = '''
    00 : Exit
    01 : gy_test_7_1
    02 : gy_test_7_2
    03 : gy_test_7_3
    04 : gy_test_7_4
    05 : gy_test_7_5
    06 : gy_test_7_6
    07 : gy_test_7_7
    08 : gy_test_7_8
    09 : gy_test_7_9
    10 : gy_test_7_10
    '''
    dic_input = {
        "0"  : py_test_exit,
        "01" : gy_test_7_1,
        "02" : gy_test_7_2,
        "03" : gy_test_7_3,
        "04" : gy_test_7_4,
        "05" : gy_test_7_5,
        "06" : gy_test_7_6,
        "07" : gy_test_7_7,
        "08" : gy_test_7_8,
        "09" : gy_test_7_9,
        "10" : gy_test_7_10
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()