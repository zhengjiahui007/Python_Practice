# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# __Author__ : "GarryZheng"
# __Date__ : 2024-07-16

import os,sys,time,datetime,calendar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Test_com import py_test_exit

def gy_test_6_8():
    # https://m.php.cn/faq/586236.html
    # https://www.baidu.com/link?url=vlbo0CURmyVJRQRaNe17v7p9jIWDAZl0SN6lNeYYKdC9lN7aAFOXOEdoAWQ28XjCVKfcR7uredk5PL0PXd5FJYeJ9ZnWR8cBsEJHa1vi6rq&wd=&eqid=a1c3c6b500654da200000006669693b0
    # struct_time = time.strptime("30 Nov 00","%d %b %y")
    # print(struct_time)
    today_time = datetime.datetime.now()
    print("today_time = ",today_time,type(today_time))
    gy_localtime = time.localtime(time.time())
    print ("本地时间为 :", gy_localtime)
    gy_year_days = 365
    gy_weekday_dict = {
        0 : "一",
        1 : "二",
        2 : "三",
        3 : "四",
        4 : "五",
        5 : "六",
        6 : "日"
    }
    '''
    能被4整除但不能被100整除,
    或者能被400整除
    '''
    if (((0 == (gy_localtime.tm_year % 4)) and (0 != (gy_localtime.tm_year % 100))) or (0 == (gy_localtime.tm_year % 400))):
        gy_year_days = 366
    else:
        gy_year_days = 365
    print("{year} is {leap} year ".format(year = gy_localtime.tm_year,leap = "leap" if calendar.isleap(gy_localtime.tm_year) else "not leap"))
    out_message_str = "今天是{gy_year}年{gy_month}月{gy_date}日,星期{gy_workday},今年的第{gy_days}天,这一年{gy_per}%的时间已流逝.".format(\
        gy_year = gy_localtime.tm_year,gy_month = gy_localtime.tm_mon,gy_date = gy_localtime.tm_mday,gy_workday = gy_weekday_dict[gy_localtime.tm_wday],\
        gy_days = gy_localtime.tm_yday,gy_per = round((gy_localtime.tm_yday/gy_year_days) * 100,2))
    print(out_message_str)
    return

def gy_test_6_9():
    gy_lst = [123,54,221,1,342,332,12,67,90,45,32]
    for i_val in gy_lst:
        i_val = 0
    print(" gy_lst = ",gy_lst)

    gy_lst1 = [[123,54,221,1],[342,332,12,67],[90,45,32]]
    for i_val in gy_lst1:
        i_val.append(0)
    print(" gy_lst1 = ",gy_lst1)

    gy_dit = {
        "0" : 10,
        "1" : 20,
        "2" : 30
    }
    for i_key,i_val in gy_dit.items():
        i_val = 0
    print("gy_dit = ",gy_dit)

    gy_dit = {
        "0" : [10,11],
        "1" : [20,32],
        "2" : [30,12]
    }
    for i_key,i_val in gy_dit.items():
        i_val.append(0)
    print("gy_dit = ",gy_dit)
    return

def gy_test_6_10():
    # i_gy = 3
    # gy_lst = [i_gy for i_gy in range(i_gy,i_gy + 3,1)]
    # print(gy_lst,i_gy)
    # https://blog.csdn.net/weixin_40134371/article/details/137071930
    gy_date_lst = [
        '2024-01-01','2024-01-15',
        '2024-01-30','2024-02-01',
        '2024-02-08','2024-02-21',
        '2024-03-11','2024-03-31',
        '2024-04-04','2024-04-25',
        '2024-05-01','2024-05-29',
        '2024-06-01','2024-06-28'
    ]
    gy_target_date = '2024-07-02'
    gy_info_dic = {
        '7_days'   : 0,
        '30_days'  : 0,
        "90_days"  : 0,
        "180_days" : 0
    }
    try:
        gy_time_target_tuple = time.strptime(gy_target_date,"%Y-%m-%d")
        gy_time_target_seconds = time.mktime(gy_time_target_tuple)
        gy_time_target_1 = datetime.datetime.strptime(gy_target_date,"%Y-%m-%d")
        print(gy_time_target_tuple,type(gy_time_target_tuple))
        print(gy_time_target_1,type(gy_time_target_1))
        # print(datetime.datetime.strptime(gy_target_date,"%Y-%m-%d"))
        for i_time in gy_date_lst:
            temp_time_tuple = time.strptime(i_time,"%Y-%m-%d")
            temp_time_seconds = time.mktime(temp_time_tuple)
            diff_seconds = abs(gy_time_target_seconds - temp_time_seconds)
            diff_days = int(diff_seconds//(60 * 60 * 24))
            if (diff_days <= 7):
                gy_info_dic["7_days"] += 1
            if (diff_days <= 30):
                gy_info_dic["30_days"] += 1
            if (diff_days <= 90):
                gy_info_dic["90_days"] += 1
            if (diff_days <= 180):
                gy_info_dic["180_days"] += 1

        # gy_time_target_0 = datetime.datetime.strptime(gy_target_date,"%Y-%m-%d")
        # for i_time in gy_date_lst:
        #     temp_time_date = datetime.datetime.strptime(i_time,"%Y-%m-%d")
        #     time_delta_date = gy_time_target_0 - temp_time_date
        #     diff_days = time_delta_date.days
        #     print(f"time_delta_date = {time_delta_date} diff_days = {diff_days} ")
        #     if (diff_days <= 7):
        #         gy_info_dic["7_days"] += 1
        #     if (diff_days <= 30):
        #         gy_info_dic["30_days"] += 1
        #     if (diff_days <= 90):
        #         gy_info_dic["90_days"] += 1
        #     if (diff_days <= 180):
        #         gy_info_dic["180_days"] += 1
    except Exception as e:
        print("An {} occurred !".format(e))
    
    print(gy_info_dic)
    return

def gy_test_6_11():
    dict_gy_str = {
        "python" : "90",
        "c++" : "89",
        "java" : "97"
    }

    for i_key,i_val in dict_gy_str.items():
        dict_gy_str[i_key] = int(i_val)
    print(dict_gy_str)
    return

def gy_test_6_12():
    input_int_odd = int(input("Please input an odd integer : "))
    if (0 == (input_int_odd % 2)):
        print("Input error,it is a even number!")
        return

    for i_count in range(0,input_int_odd,1):
        if (i_count <= (input_int_odd//2)):
            print(" " * ((input_int_odd)//2 - i_count) + "*" * (2 * i_count + 1))
        else:
            print(" " * (i_count - (input_int_odd)//2) + "*" * (input_int_odd - (i_count - (input_int_odd)//2) * 2))
    return

def gy_test_6_13():
    for i in range(1,10,1):
        for j in range(1,i + 1,1):
            print(f"{j} * {i} = %2d"%(j * i),end = "  ")
        print(end = "\n")
    return

def gy_test_6_14():
    gy_str = input("Please input a string : ")
    try:
        character_info_dic = {}
        for i_char in gy_str:
            character_info_dic[i_char] = 0
        for i_char in gy_str:
            if i_char in character_info_dic:
                character_info_dic[i_char] += 1
        print(character_info_dic)
    except Exception as e:
        print(f"An error {e} occurred !")
    return

def gy_test_6_15():
    gy_N = int(input("Please input an integer : "))
    start_N = (10 ** (gy_N - 1))
    end_N = (10 ** (gy_N))
    gy_lst = []
    for i_n in range(start_N,end_N,1):
        sum_n = 0
        temp_n = i_n
        for div_count in range(0,gy_N,1):
            sum_n += (temp_n % 10) ** gy_N
            temp_n //= 10
        if (sum_n == i_n):
            gy_lst.append(i_n)
    print(gy_lst)
    return

def gy_test_6_16():
    gy_N = int(input("Please input an integer : "))
    gy_lst = []
    for i_n in range(1,gy_N + 1,1):
        if (gy_N >= (i_n ** 2)):
            gy_lst.append(i_n ** 2)
        else:
            break
    print(gy_lst)
    return

def gy_test_6_17():
    gy_lst = [3,5,1,2,1,3]
    gy_result_set = set()
    for i_Hundred in gy_lst:
        for i_Ten in gy_lst:
            for i_unit in gy_lst:
                if ((i_unit not in (i_Hundred,i_Ten)) and (i_Hundred != i_Ten)):
                    gy_result_set.add(i_Hundred * 100 + i_Ten * 10 + i_unit)
    print(gy_result_set)
    return

def gy_test_6_18():
    gy_lst = [23,342,12,65,2,3213,65,93,2]
    print("Original lst = ",gy_lst)
    gy_lst_revert = []
    for i in range(0,len(gy_lst)//2,1):
        gy_lst[len(gy_lst) - i - 1], gy_lst[i] = gy_lst[i],gy_lst[len(gy_lst) - i - 1]
    print("Revert lst = ",gy_lst)
    return

def gy_test_6_19():
    gy_N = int(input("Please input the offset number : "))
    gy_lst = [23,342,12,65,2,3213,65,93,2]
    print("Original lst = ",gy_lst)
    # gy_lst_offsetright_2 = gy_lst[-1:-3:-1] + gy_lst[0:len(gy_lst) - 2:1]
    offset_N = gy_N % len(gy_lst)
    for i in range(0,offset_N,1):
        temp_val = gy_lst[-1]
        gy_lst.pop(-1)
        gy_lst.insert(0,temp_val)
    print(f"gy_lst offset {gy_N} {gy_lst} .")
    return

def gy_test_6_20():
    gy_str = (input("Please input 3 number split with space like 1 2 3 : "))
    gy_lst = gy_str.split(" ")
    gy_lst_int = []
    for i_char in gy_lst:
        gy_lst_int.append(int(i_char))
    for i in range(0,len(gy_lst_int),1):
        for j in range(0,len(gy_lst_int) - 1 - i,1):
            if (gy_lst_int[j] < gy_lst_int[j + 1]):
                gy_lst_int[j],gy_lst_int[j + 1] = gy_lst_int[j + 1],gy_lst_int[j]
    for i in gy_lst_int:
        print(i,end = " ")
    return

def gy_test_6_21():
    dict_gy_score = {
        "python" : 590,
        "c++" : 189,
        "java" : 397
    }
    max_score,max_score_key = dict_gy_score["python"],"python"
    for gy_key,gy_val in dict_gy_score.items():
        if (gy_val > max_score):
            max_score,max_score_key = gy_val,gy_key
    print(f"The highest score is {max_score_key} : {max_score} .")
    return

def gy_test_6_22():
    ming_fav_fruit = {"Banana","Apple","Grape"}
    hong_fav_fruit = {"Banana","Strawberry","Peach"}
    print(f"Ming and Hong like both {ming_fav_fruit & hong_fav_fruit}")
    print(f"All of the fav fruits for Ming and Hong are {ming_fav_fruit | hong_fav_fruit}")
    print(f"The fav fruits for Ming but not Hong are {ming_fav_fruit - (ming_fav_fruit & hong_fav_fruit)}")
    print(f"The fav fruits for Hong but not Ming are {hong_fav_fruit - (ming_fav_fruit & hong_fav_fruit)}")
    return

if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit
    1 : gy_test_6_8(Print the info of today)
    2 : gy_test_6_9
    3 : gy_test_6_10(The date diff)
    4 : gy_test_6_11(Dict score int)
    5 : gy_test_6_12(Print rhombus)
    6 : gy_test_6_13(Print 9 * 9 table)
    7 : gy_test_6_14(Count the character)
    8 : gy_test_6_15(Narcissistic number)
    9 : gy_test_6_16(Perfect Square number)
    10 : gy_test_6_17
    11 : gy_test_6_18(Revert list)
    12 : gy_test_6_19(List offset)
    13 : gy_test_6_20(Sort list)
    14 : gy_test_6_21(Get the highest score)
    15 : gy_test_6_22
    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_6_8,
        "2" : gy_test_6_9,
        "3" : gy_test_6_10,
        "4" : gy_test_6_11,
        "5" : gy_test_6_12,
        "6" : gy_test_6_13,
        "7" : gy_test_6_14,
        "8" : gy_test_6_15,
        "9" : gy_test_6_16,
        "10" : gy_test_6_17,
        "11" : gy_test_6_18,
        "12" : gy_test_6_19,
        "13" : gy_test_6_20,
        "14" : gy_test_6_21,
        "15" : gy_test_6_22
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
