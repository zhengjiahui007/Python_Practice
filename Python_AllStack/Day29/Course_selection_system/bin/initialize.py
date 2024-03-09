#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#!/usr/bin/env python

"""
Initialized the administrative account
"""
import os,sys,time,pickle

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src.service import initialize_service

def init_execute():
    initialize_service.main()
    return

if ('__main__' == __name__):
    init_execute()
