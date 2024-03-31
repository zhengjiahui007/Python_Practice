# -*- coding : utf-8 -*-
#!__author__ : "Garry Zheng"
#! /usr/bin/env python 3

# -*- coding : utf-8 -*-
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
import os,sys,time
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(BASE_PATH)
sys.path.append(BASE_PATH)

# file_p = open('test_txt.txt','r',encoding='utf-8')
# print(file_p.read())
# file_p.close()

# gy_s = 'I am 郑嘉惠'
# print(repr(gy_s))
# print(type(gy_s))


# gy_s = u'I am 郑嘉惠'
# print(repr(gy_s))
# print(type(gy_s))
print(b'hello' + 'gy')