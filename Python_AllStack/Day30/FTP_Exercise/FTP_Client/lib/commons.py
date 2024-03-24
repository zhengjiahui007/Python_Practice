#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import inspect,sys,os

import sys
import hashlib


def fetch_file_md5(file_path):
    obj_h = hashlib.md5()
    with open(file_path,'rb') as file_p:
        for temp_bytes in file_p:
            #print(type(temp_bytes),temp_bytes)
            obj_h.update(temp_bytes)
        # while True:
        #     temp_bytes = file_p.read(16)
        #     print(type(temp_bytes),temp_bytes,not temp_bytes)
        #     if not temp_bytes:
        #         break
        #     obj_h.update(temp_bytes)
        print(obj_h.hexdigest())
    return obj_h.hexdigest()
        # temp_str = str()
        # print(not temp_str)
        # temp_str = ""
        # print(not temp_str)
        # temp_str = "2"
        # print(not temp_str)


def print_function_name_and_line_number():
    # 获取当前函数的名字
    function_name = inspect.currentframe().f_code.co_name
    # 获取当前行号
    line_number = inspect.currentframe().f_lineno
    # 打印函数名和行号
    print(f"Function name: {function_name}, Line number: {line_number}")
    print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
 
# 调用函数，打印其名字和行号
#print_function_name_and_line_number()

# fetch_file_md5("12.txt")