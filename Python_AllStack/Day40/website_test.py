# -*-coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3


import os,time,sys,socket


def gy_main():
    gy_server_local = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
    gy_server_address = ('127.0.0.1',8093)
    gy_server_local.bind(gy_server_address)
    gy_server_local.listen(3)
    gy_client_con = None
    gy_client_add = None

    while True:
        try:
            gy_client_con,gy_client_add = gy_server_local.accept()
            print(gy_client_con,gy_client_add)
        except Exception as e:
            print("An error is : ",e)
            continue
        else:
            while True:
                rec_mess = gy_client_con.recv(1024)
                print(" rec_mess = ",rec_mess.decode("utf8"))
                with open('hello.html','rb') as gy_fp:
                    temp_data = gy_fp.read(1024)
                    print("temp = ",temp_data.decode("utf8"))
                    gy_client_con.sendall(temp_data)
                    print("@@@")
                gy_client_con.close()
                return

if "__main__" == __name__:
    gy_main()

