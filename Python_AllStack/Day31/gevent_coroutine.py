# -*- coding : utf-8 -*-
# __author__ : "Garry Zheng"
#!usr/bin/env python3

import gevent,os,sys,time
from urllib.request import urlopen
from greenlet import greenlet
from gevent import monkey

monkey.patch_all()
def gy_getweb(weburl:str):
    print('Get %s ' % weburl)
    re_page = urlopen(weburl)
    data_get = re_page.read()
    print('%d bytes received from %s .' % (len(data_get),weburl))


web_list = ["https://www.qq.com/",
"https://www.163.com/",
"https://www.cnblogs.com/xyao1/p/11002640.html"]

start_t = time.time()
for web_i in web_list:
    gy_getweb(web_i)
print("Normal methods total time : ",time.time() - start_t)

start_t = time.time()
gevent.joinall([gevent.spawn(gy_getweb,web_list[0]),gevent.spawn(gy_getweb,web_list[1]),gevent.spawn(gy_getweb,web_list[2])])

print("Coroutine method tatal time : ",time.time() - start_t)