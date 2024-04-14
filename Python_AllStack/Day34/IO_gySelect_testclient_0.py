# -*- coding : utf-8 -*-
# __author__ : "Garry Zheng"
#!usr/bin/env/ Python3

import socket,os,time

gy_client_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)

gy_server_address_port = ('127.0.0.1',8898)

gy_client_soc.connect(gy_server_address_port)
print("0 gy_client_soc = ",gy_client_soc)
while True:
    try:
        send_mess = input("Please input >>> ")
        gy_client_soc.send(send_mess.encode('utf-8'))
        if 'Exit' == send_mess:
            break
    except Exception as e:
        print("e is ",e)
        continue
gy_client_soc.close()