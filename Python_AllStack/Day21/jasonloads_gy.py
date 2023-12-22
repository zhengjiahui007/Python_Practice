import json
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print("The is json test  = ",BASE_DIR)
sys.path.append(BASE_DIR)

file_gy = BASE_DIR + "\gy_file_jn"
gy_f = open(file_gy,"r")
gy_data = gy_f.read()
gy_dic = json.loads(gy_data)

gy_f.close()

print(gy_dic)