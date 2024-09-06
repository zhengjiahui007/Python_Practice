# -*- coding : utf-8 -*-
# !usr/bin/env python3
# __Author__ : "GarryZheng"
# __Date__ : "2024-07-26"

import os,sys,time,datetime,calendar,re,pprint
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

def gy_revert_int(gy_num:int)->int:
    if (not isinstance(gy_num,int)) or (0 >= gy_num):
        return None
    gy_num_new = gy_num
    mode_num = 0
    gy_lst_single_num = []
    while (0 < gy_num_new):
        mode_num = gy_num_new % 10
        gy_lst_single_num.insert(0,mode_num)
        gy_num_new //= 10
    # print(gy_lst_single_num)
    ten_multi = 0
    gy_num_reverse = 0
    for i in gy_lst_single_num:
        gy_num_reverse += i * (10**(ten_multi))
        ten_multi += 1
    return gy_num_reverse

def gy_test_7_11():
    a = 1234578
    print(f"The {a} reversed is {gy_revert_int(a)} !")
    a = 32434545
    print(f"The {a} reversed is {gy_revert_int(a)} !")
    a = 10000
    print(f"The {a} reversed is {gy_revert_int(a)} !")
    return

def gy_test_7_12():
    gy_time = "15小时43分29秒"
    gy_time_new = gy_time.replace("小"," ")
    gy_time_lst = re.split("[时分秒]",gy_time_new)
    print("gy_time_lst = ",gy_time_lst)
    gy_seconds_total = int(gy_time_lst[0]) * 3600 + int(gy_time_lst[1]) * 60 + int(gy_time_lst[2])
    print("gy_seconds_total = ",gy_seconds_total)
    return

def gy_transfer_score(gy_data):
    # dict
    if isinstance(gy_data,dict):
        for key,val in gy_data.items():
            gy_data[key] = gy_transfer_score(val)
        return gy_data
    # list
    gy_score_lst = []
    if isinstance(gy_data,list):
        for i_val in gy_data:
            gy_score_lst.append(gy_transfer_score(i_val))
        return gy_score_lst
    # string
    if isinstance(gy_data,str):
        return int(gy_data)

    return None

def gy_test_7_13():
    gy_score_data = {
        'python' : {'上学期' : '95','下学期' : '97'},
        'c++' : ['94','91','99'],
        'java' : [{'月考' : '91','期中考' : '99','期末考' : '92'}]
    }
    gy_transfer_score(gy_score_data)
    print("gy_score_data = ",gy_score_data)
    pprint.pprint(gy_score_data)
    return

def gy_programline_count_in_file(folder_path:str)->int:
    print(" folder_path = ",folder_path)
    program_line_count = 0
    for name_lst in os.listdir(folder_path):
        print(" name_lst = ",name_lst, os.path.isfile(os.path.join(folder_path,name_lst)))
        if ((os.path.isfile(os.path.join(folder_path,name_lst))) and name_lst.endswith('.py')):
            with open(os.path.join(folder_path,name_lst),'r',encoding = 'utf-8') as f_p:
                # total_line_gen = (1 for i in f_p)
                # line_count = sum(total_line_gen)
                # print('line_count = ',line_count)
                gy_find_triple_quoted = 0
                for i_line in f_p:
                    if i_line.isspace():
                        continue
                    if i_line.lstrip().startswith('#'):
                        continue
                    if (i_line.lstrip().startswith("'''") or i_line.lstrip().startswith('"""')) and (0 == gy_find_triple_quoted):
                        gy_find_triple_quoted = 1
                        continue
                    if (i_line.lstrip().startswith("'''") or i_line.lstrip().startswith('"""')) and (1 == gy_find_triple_quoted):
                        gy_find_triple_quoted = 0
                        continue
                    if (1 == gy_find_triple_quoted):
                        continue
                    program_line_count += 1

    return program_line_count

def gy_test_7_14():
    folder_path = os.path.join(BASE_DIR,"Excercise_05")
    print('BASE_DIR = ',BASE_DIR)
    print(gy_programline_count_in_file(folder_path))
    return


def gy_test_7_15():
    gy_str = "@@ ### This is a book ,my name is GZ ##!88 73289 ok I am fine !"
    gy_words_lst = []
    gy_words_start = -1
    for i in range(0,len(gy_str),1):
        if ((('a' <= gy_str[i]) and ('z' >= gy_str[i])) or (('A' <= gy_str[i]) and ('Z' >= gy_str[i]))):
            if (-1 == gy_words_start):
                gy_words_start = i
        else:
            if (-1 != gy_words_start):
                gy_words_lst.append(gy_str[gy_words_start : i : 1])
            gy_words_start = -1
    print(" gy_words_lst = ",gy_words_lst)
    return

def gy_test_7_16():
    file_path = os.path.join(BASE_DIR,"Excercise_06","stu_score.txt")
    print('file_path = ',file_path)
    gy_score_dict = {}
    with open(file_path,'r',encoding = 'utf-8') as f_p:
        for i_line in f_p:
            gy_single_lst = []
            gy_single_lst = i_line.split("，")
            gy_score_dict[gy_single_lst[0]] = int(gy_single_lst[1])
    print("gy_score_dict = ",gy_score_dict)
    max_score = 0
    for gy_key,gy_val in gy_score_dict.items():
        if (gy_val > max_score):
            max_score = gy_val
    print("max_score = ",max_score)
    min_score = 100
    for gy_key,gy_val in gy_score_dict.items():
        if (gy_val < min_score):
            min_score = gy_val
    print("min_score = ",min_score)

    gy_max_num = 0
    gy_min_num = 0
    for gy_key,gy_val in gy_score_dict.items():
        if (gy_val == max_score):
            gy_max_num += 1
        if (gy_val == min_score):
            gy_min_num += 1
    print(f"gy_max_num = {gy_max_num} gy_min_num = {gy_min_num} !")

    sum_score = 0
    for gy_key,gy_val in gy_score_dict.items():
        sum_score += gy_val
    print("average_score = ",sum_score/len(gy_score_dict))
    return

def gy_test_7_17():
    file_path = os.path.join(BASE_DIR,"Excercise_06","stu_score_1.txt")
    print('file_path = ',file_path)
    gy_yuwenscore_dict = {}
    gy_shuxuescore_dict = {}
    gy_score_dict = {}
    with open(file_path,'r',encoding = 'utf-8') as f_p:
        for i_line in f_p:
            gy_single_lst = []
            gy_single_lst = i_line.split("，")
            gy_shuxuescore_dict[gy_single_lst[0]] = int(gy_single_lst[1])
            gy_yuwenscore_dict[gy_single_lst[0]] = int(gy_single_lst[2])
            gy_score_dict[gy_single_lst[0]] = {'数学' : int(gy_single_lst[1]),'语文' : int(gy_single_lst[2])}
    print("gy_yuwenscore_dict = ",gy_yuwenscore_dict)
    print("gy_shuxuescore_dict = ",gy_shuxuescore_dict)
    gy_yuwen_samescore_dict = {}
    for gy_val in gy_yuwenscore_dict.values():
        gy_yuwen_samescore_dict[gy_val] = []
    for gy_key,gy_val in gy_yuwenscore_dict.items():
        gy_yuwen_samescore_dict[gy_val].append(gy_key)

    print("gy_yuwen_samescore_dict = ",gy_yuwen_samescore_dict)
    for gy_yuwen_key in gy_yuwen_samescore_dict.keys():
        if (len(gy_yuwen_samescore_dict[gy_yuwen_key]) > 1):
            print(f" {gy_yuwen_samescore_dict[gy_yuwen_key]} are the same score {gy_yuwen_key} !")

    gy_shuxue_samescore_dict = {}
    for gy_val in gy_shuxuescore_dict.values():
        gy_shuxue_samescore_dict[gy_val] = []
    for gy_key,gy_val in gy_shuxuescore_dict.items():
        gy_shuxue_samescore_dict[gy_val].append(gy_key)

    print("gy_shuxue_samescore_dict = ",gy_shuxue_samescore_dict)
    for gy_shuxue_key in gy_shuxue_samescore_dict.keys():
        if (len(gy_shuxue_samescore_dict[gy_shuxue_key]) > 1):
            print(f" {gy_shuxue_samescore_dict[gy_shuxue_key]} are the same score {gy_shuxue_key} !")

    for gy_name,gy_score in gy_score_dict.items():
        if (gy_score_dict[gy_name]['数学'] == gy_score_dict[gy_name]['语文']):
            print(f" {gy_name}'s Yuwen and Math score are the same !")

    gy_totalscore_dict = {}
    gy_highest_score = 0
    for gy_name,gy_score in gy_score_dict.items():
        gy_totalscore_dict[gy_name] = int(gy_score['数学']) + int(gy_score['语文'])
        if (gy_totalscore_dict[gy_name] > gy_highest_score):
            gy_highest_score = gy_totalscore_dict[gy_name]
    print("gy_totalscore_dict = ",gy_totalscore_dict," gy_highest_score = ",gy_highest_score)
    total_score = 0
    for gy_name,gy_score in gy_totalscore_dict.items():
        total_score += gy_score
        if (gy_highest_score == gy_score):
            print(f" {gy_name} got the highest score , gy_highest_score = {gy_highest_score} ")
    print("The average score of total score is  = ",round((total_score/len(gy_totalscore_dict)),2))
    return

def gy_test_7_18():
    file_path = os.path.join(BASE_DIR,"Excercise_06","Toupiao.txt")
    print('file_path = ',file_path)
    gy_vote_set = set()
    with open(file_path,'r',encoding = 'utf-8') as f_p:
        for i_line in f_p:
            gy_vote_set.add(i_line.rstrip())
    print(f'There are {len(gy_vote_set)} students take part in the vote, they are {gy_vote_set} ! ')

    gy_vote_dic = {}
    for gy_name in gy_vote_set:
        gy_vote_dic[gy_name] = 0
    print('gy_vote_dic = ',gy_vote_dic)

    with open(file_path,'r',encoding = 'utf-8') as f_p:
        for i_line in f_p:
            gy_name = i_line.rstrip()
            gy_vote_dic[gy_name] += 1
    print('gy_vote_dic = ',gy_vote_dic)

    gy_max_vote = 0
    for name_key,vote_val in gy_vote_dic.items():
        if (vote_val > gy_max_vote):
            gy_max_vote = vote_val
    print('gy_max_vote = ',gy_max_vote)
    for name_key,vote_val in gy_vote_dic.items():
        if (vote_val == gy_max_vote):
            print('The highest voted name_key = ',name_key)
    return

def gy_test_7_19():
    file_path = os.path.join(BASE_DIR,"Excercise_06","fruits_Saturday.txt")
    print('file_path = ',file_path)
    sat_fruit_spent_dict = dict()
    sat_fruit_set = set()
    with open(file_path,'r',encoding = 'utf-8') as file_p:
        for i_line in file_p:
            gy_single_line = []
            gy_single_line = i_line.strip().split(" ")
            sat_fruit_spent_dict[gy_single_line[0]] = float(gy_single_line[1])
            sat_fruit_set.add(gy_single_line[0])
    print('sat_fruit_spent_dict = ',sat_fruit_spent_dict)
    sat_max_spent = 0
    sat_max_spent_fruit = ""
    sat_total_spent = 0
    for i_fruit,i_money in sat_fruit_spent_dict.items():
        sat_total_spent += i_money
        if (i_money > sat_max_spent):
            sat_max_spent = i_money
            sat_max_spent_fruit = i_fruit
    print('The sat_max_spent_fruit is  = ',sat_max_spent_fruit," sat_total_spent = ",sat_total_spent)

    file_path = os.path.join(BASE_DIR,"Excercise_06","fruits_Sunday.txt")
    print('file_path = ',file_path)
    sun_fruit_spent_dict = dict()
    sun_fruit_set = set()
    with open(file_path,'r',encoding = 'utf-8') as file_p:
        for i_line in file_p:
            gy_single_line = []
            gy_single_line = i_line.strip().split(" ")
            sun_fruit_spent_dict[gy_single_line[0]] = float(gy_single_line[1])
            sun_fruit_set.add(gy_single_line[0])
    print('sun_fruit_spent_dict = ',sun_fruit_spent_dict)
    sun_max_spent = 0
    sun_max_spent_fruit = ""
    sun_total_spent = 0
    for i_fruit,i_money in sun_fruit_spent_dict.items():
        sun_total_spent += i_money
        if (i_money > sun_max_spent):
            sun_max_spent = i_money
            sun_max_spent_fruit = i_fruit
    print('The sun_max_spent_fruit is  = ',sun_max_spent_fruit," sun_total_spent = ",sun_total_spent)
    print('The total spent in Sat and Sun is  = ',round((sat_total_spent + sun_total_spent),2))
    print('sat_fruit_set = ',sat_fruit_set)
    print('sun_fruit_set = ',sun_fruit_set)
    print("The fruits both on Sat and Sun are = ",sat_fruit_set.intersection(sun_fruit_set))
    print("The fruits on Sun but not on Sun are = ",sun_fruit_set.difference(sat_fruit_set))
    if (sun_max_spent > sat_max_spent):
        print('sun_max_spent_fruit = ',sun_max_spent_fruit)
    else:
        print('sat_max_spent_fruit = ',sat_max_spent_fruit)
    return

def gy_test_7_20():
    file_path = os.path.join(BASE_DIR,"Excercise_06","IP.txt")
    print('file_path = ',file_path)
    ip_times_dict = dict()
    with open(file_path,'r',encoding = 'utf-8') as fp_file:
        for i_line in fp_file:
            ip_val = i_line.strip()
            ip_times_dict.setdefault(ip_val,0)
            ip_times_dict[ip_val] += 1
    print('0 ip_times_dict = ',ip_times_dict)
    ip_times_lst = []
    for ip,times in ip_times_dict.items():
        ip_times_lst.append((ip,times))
    print(' ip_times_lst = ',ip_times_lst)
    fun = lambda x : x[1]
    # 参数key指定了只含一个参数的方法，这个方法用来从列表的每个元素中提取比较键
    # key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    ip_times_lst.sort(key = fun,reverse = False)
    for i in ip_times_lst:
        print(i)
    return

def gy_test_7_21():
    file_path = os.path.join(BASE_DIR,"Excercise_06","TeleNO.txt")
    print('file_path = ',file_path)
    gy_pattern = re.compile("\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}")
    tele_lst = []
    with open(file_path,'r',encoding = 'utf-8') as fp_file:
        for i_line in fp_file:
            ip_val = i_line.strip()
            gy_match_obj = gy_pattern.match(ip_val)
            if (None != gy_match_obj):
                tele_lst.append(ip_val)
    print("tele_lst = ",tele_lst)
    return

def gy_test_7_22():
    gy_lst = [1,2,3,4,5,6,7,8,9]
    gy_mv = 5
    for k in range(0,gy_mv,1):
        gy_tmp = gy_lst[-1]
        for i in range(len(gy_lst) - 1,0,-1):
            gy_lst[i] = gy_lst[i - 1]
        gy_lst[0] = gy_tmp
    print(gy_lst)
    return

def gy_test_7_23():
    gy_lst = ["fruits_Saturday.txt","IP.txt","TeleNO.txt","Toupiao.txt"]
    gy_file_all = "file_all.txt"
    gy_file_all_path = os.path.join(BASE_DIR,"Excercise_06",gy_file_all)
    with open(gy_file_all_path,'w',encoding = 'utf-8') as all_fp:
        for file_name in gy_lst:
            file_path = os.path.join(BASE_DIR,"Excercise_06",file_name)
            print('file_path = ',file_path)
            with open(file_path,'r',encoding = 'utf-8') as fp_single:
                for i_line in fp_single:
                    all_fp.write(i_line)
    return

def gy_test_7_24():
    gy_file_all = "all_file.txt"
    gy_file_all_path = os.path.join(BASE_DIR,"Excercise_06",gy_file_all)
    gy_pattern = re.compile("[013]{1}")
    with open(gy_file_all_path,'r',encoding = 'utf-8') as fp_all:
        for i_line in fp_all:
            val_line = i_line.strip()
            gy_match_obj = gy_pattern.match(val_line)
            if (None != gy_match_obj):
                # print(gy_match_obj.group())
                gy_single_file = gy_match_obj.group() + ".txt"
                gy_single_file_path = os.path.join(BASE_DIR,"Excercise_06",gy_single_file)
                with open(gy_single_file_path,'a+',encoding = 'utf-8') as fp_single:
                    fp_single.write(i_line)
    return


if (__name__ == "__main__"):
    dis_choice = '''
    0 : Exit
    1 : gy 1 - 10
    2 : gy 11 - 20
    '''

    dis_playmessage = '''
    0  : Exit
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
    dis_playmessage2 = '''
    0  : Exit
    11 : gy_test_7_11
    12 : gy_test_7_12
    13 : gy_test_7_13
    14 : gy_test_7_14
    15 : gy_test_7_15
    16 : gy_test_7_16
    17 : gy_test_7_17
    18 : gy_test_7_18
    19 : gy_test_7_19
    20 : gy_test_7_20
    21 : gy_test_7_21
    22 : gy_test_7_22
    23 : gy_test_7_23
    24 : gy_test_7_24
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
        "10" : gy_test_7_10,
        "11" : gy_test_7_11,
        "12" : gy_test_7_12,
        "13" : gy_test_7_13,
        "14" : gy_test_7_14,
        "15" : gy_test_7_15,
        "16" : gy_test_7_16,
        "17" : gy_test_7_17,
        "18" : gy_test_7_18,
        "19" : gy_test_7_19,
        "20" : gy_test_7_20,
        "21" : gy_test_7_21,
        "22" : gy_test_7_22,
        "23" : gy_test_7_23,
        "24" : gy_test_7_24
    }
    while True:
        print(dis_choice)
        input_val = input("Please input your choice : ")
        if ('0' == input_val):
            py_test_exit()
        elif ('1' == input_val):
            print(dis_playmessage)
        elif ('2' == input_val):
            print(dis_playmessage2)

        input_val = input("Please input your choice again : ")
        dic_input[input_val]()
