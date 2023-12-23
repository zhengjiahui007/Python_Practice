#!_*_coding:utf-8_*_
#__author__:"Garry Zheng"

import json
import os
import sys

basic_dir_account = os.path.dirname(os.path.abspath(__file__))
print(basic_dir_account)
print(os.path.dirname(__file__))

acc_dic1234 = {
    'id' : 1234,
    'password' : 'abcd',
    'credit' : 15000,
    'balance' : 15000,
    'enroll_date' : '2016-01-02',
    'expire_date' : '2024-01-01',
    'pay_day' : 30,
    'status' : 0 # 0 = normal,1 = locked,2 = disabled
}

file_path_account = basic_dir_account + r'\accounts_gy\1234.json'

f_account = open(file_path_account,"w+")
f_account.write(json.dumps(acc_dic1234))
f_account.close()