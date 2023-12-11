import sys
#import cal_gy #search the path , then cal_gy = cal_gy.py all codes

#from cal_gy import add_gy,sub_gy #cal_gy is not defined



#print("sys.path is ",sys.path)
#print(f"The result is {cal_gy.add_gy(2,9)}","The result is a {}".format(cal_gy.add_gy(2,9)))
#print("x is ",cal_gy.gy_x)

# def add_gy(x,y):
#     return x + y + 3
# from cal_gy import *


# print(f"The result is {add_gy(2,9)}","The result is a {}".format(sub_gy(2,9)))
# print("x is ",gy_x)

""" 
from web_gyf.web_gy import logger_gy

logger_gy.logger_gy()
 """

from web_gyf.web_gy.logger_gy import logger_gy #run the __init__.py

logger_gy()