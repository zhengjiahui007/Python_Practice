import inspect,sys,os

import sys
import hashlib


def fetch_file_md5(file_path):
    obj_h = hashlib.md5()
    try:
        with open(file_path,'rb') as file_p:
            for temp_bytes in file_p:
                #print(type(temp_bytes),temp_bytes)
                obj_h.update(temp_bytes)
            # while True:
            #     temp_bytes = file_p.read(16)
            #     print(type(temp_bytes),temp_bytes,not temp_bytes)
            #     if not temp_bytes:
            #         break
            #     obj_h.update(temp_bytes)
            print(obj_h.hexdigest())
    except Exception as e:
        print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
    return obj_h.hexdigest()
        # temp_str = str()
        # print(not temp_str)
        # temp_str = ""
        # print(not temp_str)
        # temp_str = "2"
        # print(not temp_str)