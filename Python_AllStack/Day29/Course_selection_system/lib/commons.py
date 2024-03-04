#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import uuid,hashlib

def creat_uuid():
    return str(uuid.uuid1())

def creat_md5():
    m = hashlib.md5()
    mx.update(bytes(str(time.time()),encoding = 'utf-8'))
    return m.hexdigest

if ('__main__' == __name__):
    print(type(str(uuid.uuid1())))


    