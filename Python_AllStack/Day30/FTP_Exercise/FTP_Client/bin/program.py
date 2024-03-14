#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import os,sys,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src import service

if ("__main__" == __name__):
    service.client_main()
    #print("[%s@%s]" % (__file__, sys._getframe().f_lineno))
    #list_gy = ["123","34"]
    #print(type(json.dumps(list_gy)))

# print(BASE_DIR)
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))