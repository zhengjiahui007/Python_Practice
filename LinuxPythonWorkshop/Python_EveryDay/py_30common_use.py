# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3
# __Date__ : "2025-03-16"

import time,os,sys
from datetime import datetime
import random

'''
https://mp.weixin.qq.com/s/_J4t7IIYtmszaEQNAgNCxg
'''

def gy_common_30_use():
    '''
    1. 列表推导式 List Comprehension
    [表达式 for 变量 in 列表] 
    [out_exp_res for out_exp in input_list]
    或者 
    [表达式 for 变量 in 列表 if 条件]
    [out_exp_res for out_exp in input_list if condition]
    # 获取1到10的平方数
    '''
    gy_list_1_10_square = [x ** 2 for x in range(1,11,1)]
    print("The square lis from 1 to 10 : ",gy_list_1_10_square)

    '''
    交换两个变量的值
    '''
    gy_a,gy_b = 1,2
    print("gy_a = {1} gy_b = {0}".format(gy_a,gy_b))
    gy_a,gy_b = gy_b,gy_a
    print("gy_a = {1} gy_b = {0}".format(gy_a,gy_b))

    '''
    读取文件内容
    '''
    try:
        with open("./data_file/100.txt","r") as gy_f:
            print("Content is = {}".format(gy_f.read()))

    except Exception as e:
        print('An exception occurred = ',e)
    finally:
        print("close ok!")

    '''
    获取当前时间
    '''
    print("The time is {} ".format(datetime.now()))

    '''
    字符串反转
    '''
    gy_str = "I am Garry!"
    print("gy_str = ",gy_str," gy_str reverse = ",gy_str[-1::-1])

    '''
    合并多个字典
    '''
    gy_d0 = {"a":1,"b":3}
    gy_d1 = {"c":1,"d":2}
    gy_d2 = {"e":23,"f":5}
    gy_D = {**gy_d0,**gy_d1,**gy_d2}
    print("gy_D = ",gy_D)

    ''''
    查找列表中的最大值和最小值
    '''
    gy_lst = [1,4,23,33,21,67,339]
    print("The max value is ",max(gy_lst))
    print("The min value is ",min(gy_lst))

    '''
    计算列表中元素的平均值
    '''
    gy_list_aver = sum(gy_lst) / len(gy_lst)
    print("gy_list_aver = ",gy_list_aver)

    '''
    使用sorted()和.sort()对列表进行排序
    '''
    print("sort the list = ",sorted(gy_lst),gy_lst.sort(),gy_lst)

    '''
    11. 生成指定范围的随机整数
    '''
    print("The random value in 1 to 1000 : ",random.randint(1,1000))

    '''
    12. 检查文件或文件夹是否存在
    '''
    print("The file ./data_file/100.txt {gy_exist} existing !".format(gy_exist = "is" if os.path.exists("./data_file/100.txt") else "is not"))
    
    '''
    字符串替换
    '''
    gy_text = "Garryzheng"
    print("",gy_text.replace("rry","ttu"))

    '''
    14. 提取文件扩展名
    '''
    gy_filename = "test.py"
    extension_name = os.path.splitext(gy_filename)[1]
    print(" {} ".format(extension_name))
    
    '''
    15. 检查一个字符串是否为数字
    '''
    gy_digitext0 = "1234"
    gy_digitext1 = "1t234"

    print(" {1} {0} ".format(gy_digitext0.isdigit(),gy_digitext1.isdigit()))
    
    
    
    return



if (__name__ == "__main__"):
    gy_common_30_use()

