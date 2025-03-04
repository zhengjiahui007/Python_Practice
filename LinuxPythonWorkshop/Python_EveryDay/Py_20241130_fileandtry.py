# _*_ coding : utf-8 _*_
# __author__ : "Garry Zheng"
# !usr/bin/env python3
# __Date__ : "2025-03-04"

import time

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

if ('__main__' == __name__):
    gy_file_main_0("./data_file/AUI_Struct.txt","r")

