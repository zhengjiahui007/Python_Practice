#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import os,sys,inspect
import subprocess
import re
import json
import socketserver,socket
from config import settings

ACTION_CODE = {
    '1000': 'cmd',
    '2000': 'post',
    '3000': 'get',
}

REQUEST_CODE = {
    '1001': 'cmd info',
    '1002': 'cmd ack',
    '2001': 'post info',
    '2002': 'ACK(可以开始上传)',
    '2003': '文件已经存在',
    '2004': '续传',
    '2005': '不续传',
    '3001': 'get info',
    '3002': 'get ack',
    '4001': "未授权",
    '4002': "授权成功",
    '4003': "授权失败"
}


class GY_Server(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        try:
            server_sock_gy = self.request
            print("Starting GY_Serve ... !")
            #print(server_sock_gy,self.client_address)
            welcome_message = "Welcome Login !"
            server_sock_gy.send(welcome_message.encode('utf-8'))
            obj_action = Server_Action(server_sock_gy)
            while True:
                if obj_action.has_login:
                    rece_action = server_sock_gy.recv(1024)
                    if not rece_action:
                        break
                    rece_str = rece_action.decode("utf-8")#str(rece_action,encoding = 'utf-8')
                    cmd_list = rece_str.split(' | ',1)#返回分割后的字符串列表。
                    print(cmd_list[0],cmd_list[1])
                    action_attr = getattr(obj_action,cmd_list[0])
                    action_attr(cmd_list[1])
                else:
                    obj_action.login()
        except Exception as e:
            print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
        server_sock_gy.close()
        return

class Server_Action(object):
    def __init__(self, conn:socket):
        self.conn = conn
        self.has_login = False
        self.username = None
        self.home = None
        self.current_dir = None

    def login(self):
        while True:
            login_mess = self.conn.recv(1024)
            login_mess_str = login_mess.decode('utf-8')
            user_list = json.loads(login_mess_str)
            print(user_list)
            if ('Garry' == user_list[0]) and ('12345' == user_list[1]):
                result_code = '4002'
                self.has_login = True
                self.username = user_list[0]
            else:
                result_code = '4003'
                self.has_login = False
            print(result_code)
            self.conn.send(result_code.encode('utf-8'))
            if '4002' == result_code:
                break
        return

    def server_initialize(self):
        self.home = os.path.join(settings.USER_HOME, self.username)
        self.current_dir = os.path.join(settings.USER_HOME, self.username)
        return

    def post(self,conmand:str):
        print(conmand)
        return

    def get(self,conmand:str):
        print(conmand)
        return

    def cmd(self,conmand:str):
        print(conmand)
        return

def server_main():
    print("ser main")
    my_serve_gy = socketserver.ThreadingTCPServer((settings.BIND_IP,settings.BIND_PORT),GY_Server)
    my_serve_gy.serve_forever()
