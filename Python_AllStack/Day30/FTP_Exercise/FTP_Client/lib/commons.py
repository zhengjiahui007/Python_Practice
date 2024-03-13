#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import inspect,sys,os
 
def print_function_name_and_line_number():
    # 获取当前函数的名字
    function_name = inspect.currentframe().f_code.co_name
    # 获取当前行号
    line_number = inspect.currentframe().f_lineno
    # 打印函数名和行号
    print(f"Function name: {function_name}, Line number: {line_number}")
    print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
 
# 调用函数，打印其名字和行号
print_function_name_and_line_number()