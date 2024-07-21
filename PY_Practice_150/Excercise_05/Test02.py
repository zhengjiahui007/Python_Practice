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


if (__name__ == "__main__"):
    dis_playmessage = '''
    0 : Exit
    1 : gy_test_6_8(Print the info of today)
    2 : gy_test_6_9

    '''
    dic_input = {
        "0" : py_test_exit,
        "1" : gy_test_6_8,
        "2" : gy_test_6_9
    }
    while True:
        print(dis_playmessage)
        input_val = input("Please input your choice : ")
        dic_input[input_val]()
