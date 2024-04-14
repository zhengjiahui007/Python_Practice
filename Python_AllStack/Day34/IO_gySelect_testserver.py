# -*- coding : utf-8 -*-
# __author__ : "Garry Zheng"
#!usr/bin/env/ Python3

import socket,os,time,select

gy_server_soc_0 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
gy_serv_add_port_0 = ('127.0.0.1',8898)
gy_server_soc_0.bind(gy_serv_add_port_0)
gy_server_soc_0.listen(3)

gy_server_soc_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
gy_serv_add_port_1 = ('127.0.0.1',8899)
gy_server_soc_1.bind(gy_serv_add_port_1)
gy_server_soc_1.listen(3)

gy_input_list = [gy_server_soc_0,gy_server_soc_1]
gy_output_list = []
rece_message = {}
r_list = []
w_list = []
e_list = []
print("gy_ser_soc Start ...")
while True:
    r_list,w_list,e_list = select.select(gy_input_list,gy_output_list,[])
    print("r_list = ",r_list)
    for i_soc in r_list:
        conn,addre = i_soc.accept()
        print(conn,addre)
        recv_bytes = conn.recv(1024)
        print("recv mess : ",recv_bytes.decode('utf-8'))
        if 'Exit' == recv_bytes.decode('utf-8'):
            client_con.close()
            break
    time.sleep(3)








