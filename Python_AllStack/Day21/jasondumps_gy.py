import json
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print("The is json test  = ",BASE_DIR)


sys.path.append(BASE_DIR)

dic_gy = {"Name":"GarryZheng","Age":38,"Job":"Firmware engineer","Department":"Life Style"}
list_gy = [1,2.3,45,2,223,9]
dic_data_gy = json.dumps(dic_gy)

#print("The is json test  = ",sys.path)
#print("The work path {}".format(os.getcwd()))
file_gy = BASE_DIR + "\gy_file_jn"
f_gy = open(file_gy,"w+")
f_gy.write(dic_data_gy)
dic_data_gy = json.dumps(list_gy)
f_gy.write(dic_data_gy)

f_gy.close()



""" 
file_path = "./" + "gy_file_jn" # 将文件名与当前目录路径连接起来
with open(file_path,"w+") as f:
    content = f.read()
print(content)
 """