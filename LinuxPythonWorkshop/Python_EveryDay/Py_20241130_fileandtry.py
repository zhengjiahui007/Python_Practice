# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
# !usr/bin/env python3
# __Date__ : "2025-03-04"
# coding=utf-8

import time,os

def gy_file_main_0(file_path:str,mode:str):
    gy_file = None
    try:
        gy_file = open(file_path,mode,encoding = 'utf-8')
        for gy_line in gy_file:
            print(gy_line,end = "")
            time.sleep(2)
    except FileNotFoundError:
        print('FileNotFoundError !')
    except LookupError:
        print("LookupError !")
    except UnicodeDecodeError:
        print("UnicodeDecodeError!")
    finally:
        print("finally !")
        if gy_file:
            gy_file.close()
    return

def gy_file_main_1(file_path:str,mode:str):
    gy_file_p = None
    try:
        with open(file_path,mode,encoding = 'utf-8') as gy_file_p:
            for gy_line in gy_file_p:
                print(gy_line,end = " ")
                time.sleep(1)

        with open(file_path,mode,encoding = 'utf-8') as gy_file_p:
            gy_file_list = gy_file_p.readlines()
            print(gy_file_list)     
    except Exception as e:
        print('An exception occurred : ',e)
    finally:
        print("end of the gy_file_main_1 !")
    return

from math import sqrt

def gy_is_prime(gy_n:int)->bool:
    prime_flag = False
    try:
        if (gy_n <= 1):
            prime_flag = False
        elif (gy_n == 2):
            prime_flag = True
        elif (gy_n >= 3):
            if ((gy_n % 2) == 0):
                prime_flag = False
            else:
                prime_flag = True
                for i in range(3,int(sqrt(gy_n)) + 1,1):
                    if ((gy_n % i) == 0):
                        prime_flag = False 
    except Exception as e:
        print('Something went wrong e = {}'.format(e))
        prime_flag = False
    finally:
        # print('The try except is finished !')
        return prime_flag

def gy_file_main_2(gy_N:int,gy_file_0:str,mode_0:str,gy_file_1:str,mode_1:str,gy_file_2:str,mode_2:str):
    gy_prime_list = []
    for i in range(1,gy_N + 1,1):
        if gy_is_prime(i):
            gy_prime_list.append(i)
    # print(gy_prime_list)
    print(len(gy_prime_list))
    if os.path.exists(gy_file_0):
        os.remove(gy_file_0)

    if os.path.exists(gy_file_1):
        os.remove(gy_file_1)

    if os.path.exists(gy_file_2):
        os.remove(gy_file_2)
    try:
        count_100 = 0
        count_1000 = 0
        count_10000 = 0
        for i in gy_prime_list:
            if (i <= 100):
                count_100 += 1
                with open(gy_file_0,mode_0,encoding = "utf-8") as gy_file_100:
                    gy_file_100.write(str(i) + " ")
                    if((0 != count_100) and (0 == (count_100 % 10))):
                        gy_file_100.write("\n")
            elif (i <= 1000):
                count_1000 += 1
                with open(gy_file_1,mode_1,encoding = "utf-8") as gy_file_1000:
                    gy_file_1000.write(str(i) + " ")
                    if((0 != count_1000) and (0 == (count_1000 % 10))):
                        gy_file_1000.write("\n")
            else:
                count_10000 += 1
                with open(gy_file_2,mode_2,encoding = "utf-8") as gy_file_10000:
                    gy_file_10000.write(str(i) + " ")
                    if((0 != count_10000) and (0 == (count_10000 % 10))):
                        gy_file_10000.write("\n")
    except:
        print('Something went wrong')
    finally:
        print('The try except is finished')
    return

import json,requests

def gy_json_main(gy_jsonfile:str,mode:str):
    gy_dict = {
        "job" : "Software engineer",
        "name": "GarryZheng",
        "age" : 39,
        "info": { "job" : "Software engineer","name": "GarryZheng","age" : 39}
    }
    gy_file_handle = None
    try:
        gy_error = False
        if os.path.exists(gy_jsonfile):
            os.remove(gy_jsonfile)

        with open(gy_jsonfile,mode,encoding = 'utf-8') as gy_file_handle:
            json.dump(gy_dict,gy_file_handle)

    except Exception as e:
        print('An exception occurred is : ',e)
        gy_error = True
    finally:
        if(False == gy_error):
            print("save the json file OK!")
    return

def gy_request_json_main():
    try:
        gy_error = False
        gy_request = requests.get("https://www.baidu.com/")
        # request_str = str(gy_request.text, encoding='utf-8')
        # gy_data_py = json.loads(request_str)
        # print(gy_request.text)
        if (200 == gy_request.status_code):
            # print(gy_request.status_code)  # 获取响应状态码
            # print(gy_request.headers)  # 获取响应头
            # print(gy_request.content)  # 获取响应内容
            # print(gy_request.text)
            print(gy_request.json())
    except json.JSONDecodeError:
        print("JSON decoding error !")
    except Exception as e:
        print('An exception occurred is : ',e)
        gy_error = True
    finally:
        if(False == gy_error):
            print("load the json file OK!")
    return

if ('__main__' == __name__):
    # gy_file_main_0("./data_file/AUI_Struct.txt","r")
    # gy_file_main_1("./data_file/AUI_Strut.txt","r")
    # gy_file_main_2(20000,"./data_file/100.txt","a+","./data_file/1000.txt","a+","./data_file/10000.txt","a+")
    # gy_json_main("./data_file/my_dict.json","w")
    gy_request_json_main()


