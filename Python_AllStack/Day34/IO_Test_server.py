# -*-coding : utf-8-*-
# __author__ : "Garry Zheng"
#!usr/bin/env/ python3

'''
https://www.baidu.com/link?url=LrnFdRpU9dMdLgBhGFBRLQh1_xFGKgwjjTxQ7I8u2YYEQviegVcjUPmKc1k1poRkebP7SdClpkngf-UmxAiaml6ZAN4HgCFoe5ObRoWOXUu&wd=&eqid=e3f6166f007494a300000003661155e9
'''
import socket,time

gy_ser_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
gy_serv_add = ('127.0.0.1',8088)
gy_ser_soc.bind(gy_serv_add)
gy_ser_soc.listen(2)
gy_ser_soc.setblocking(False)
print("gy_ser_soc Start ...")
while True:
    try:
        client_con,client_add = gy_ser_soc.accept()
        print(client_con,client_add)
        recv_bytes = client_con.recv(1024)
        print("recv mess : ",recv_bytes.decode('utf-8'))
        if 'Exit' == recv_bytes.decode('utf-8'):
            client_con.close()
            break
    except Exception as e:
        print("e is ",e)
        time.sleep(3)
        continue

gy_ser_soc.close()
