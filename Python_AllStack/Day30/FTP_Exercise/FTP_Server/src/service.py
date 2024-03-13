#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import os,sys,inspect

import socketserver
from config import settings

class GY_Server(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        while True:
            try:
                print("Starting GY_Serve ... !")
                server_sock_gy = self.request
                print(server_sock_gy,self.client_address)
                welcome_message = "Welcome Login !"
                server_sock_gy.send(welcome_message.encode('utf8'))
            except Exception as e:
                print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
                continue
            else:
                while True:
                    try:
                        print("serve waiting ...")
                        rec_mess = server_sock_gy.recv(1024)
                        print("....",str(rec_mess,'UTF-8'))
                        if not rec_mess:break
                        send_mess = input(">>>")
                        server_sock_gy.send(send_mess.encode('UTF-8'))
                    except Exception as e:
                        print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
                        break
                server_sock_gy.close()
        return

def server_main():
    print("ser main")
    my_serve_gy = socketserver.ThreadingTCPServer((settings.BIND_IP,settings.BIND_PORT),GY_Server)
    my_serve_gy.serve_forever()
