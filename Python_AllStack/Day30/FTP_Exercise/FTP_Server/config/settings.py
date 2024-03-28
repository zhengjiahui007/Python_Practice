#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


BIND_IP = '127.0.0.1'
BIND_PORT = 9992


USER_HOME = os.path.join(BASE_DIR,'home')
USER_DBASE = os.path.join(BASE_DIR,'db')