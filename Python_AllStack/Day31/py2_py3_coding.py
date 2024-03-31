# -*- coding : utf-8 -*-
# __author__ : "Garry Zheng"
#!/usr/bin/env python3
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
import os,sys,json,time

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

gy_s = '苑昊'

# print(gy_s.encode('utf-8').decode('gbk'))

# print(gy_s.encode('gbk').decode('utf-8'))

print(json.dumps(gy_s),type(json.dumps(gy_s)))

print(sys.getdefaultencoding())