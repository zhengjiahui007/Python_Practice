#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import os
import sys
# os.path.abspath(__file__)

# print(os.path.abspath(__file__))

# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR1 is {BASE_DIR}")
print("BASE_DIR2 is",BASE_DIR)
print("BASE_DIR3 is {}".format(BASE_DIR))
sys.path.append(BASE_DIR)

from core import main_gy


if (__name__ == "__main__"):
    main_gy.run(1)