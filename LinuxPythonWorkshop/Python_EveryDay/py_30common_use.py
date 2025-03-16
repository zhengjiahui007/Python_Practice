# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
#!usr/bin/env python3
# __Date__ : "2025-03-16"


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
    return



if (__name__ == "__main__"):
    gy_common_30_use()
