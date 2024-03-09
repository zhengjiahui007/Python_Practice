#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#!/usr/bin/env python

import os,sys,time,pickle


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src.service import admin_service


if "__main__" == __name__:
    admin_service.admin_main()