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
                self.server_initialize()
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
        cmd_list = re.split('\s+',conmand,1)
        print(cmd_list)
        if 'ls' == cmd_list[0]:
            if len(cmd_list) == 1:
                if self.current_dir:
                    cmd_list.append(self.current_dir)
                else:
                    cmd_list.append(self.home)
            else:
                if self.current_dir:
                    folder_p = os.path.join(self.current_dir,cmd_list[1])
                else:
                    folder_p = os.path.join(self.home,cmd_list[1])
                cmd_list[1] = folder_p

        if 'cd' == cmd_list[0]:
            if len(cmd_list) == 1:
                    cmd_list.append(self.home)
            else:
                if self.current_dir:
                    folder_p = os.path.join(self.current_dir,cmd_list[1])
                else:
                    folder_p = os.path.join(self.home,cmd_list[1])
                cmd_list[1] = folder_p
        cmd_str = ' '.join(cmd_list)
        print("cmd_str = ",cmd_str)
        try:
            result_bytes = subprocess.check_output(cmd_str,shell = True)
            print(type(result_bytes))
            info_result_str = 'info|{}'.format(len(result_bytes))
            print(info_result_str)
            info_result_bytes = info_result_str.encode('utf-8')
            self.conn.send(info_result_bytes)
            ack_bytes = self.conn.recv(1024)
            if 'ack' == ack_bytes.decode('utf-8'):
                result_total_len = len(result_bytes)
                if 1024 < result_total_len:
                    for i in range(0,result_total_len,1024):
                        temp_data = result_bytes[i : (i + 1024) : 1]
                        self.conn.send(temp_data)
                else:
                    self.conn.send(result_bytes)
        except Exception as e:
            print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
        return

def server_main():
    print("ser main")
    # try:
    #     data_by = b'334dfksjfkf34fkqfksdjfjadkf0ere'
    #     print(len(data_by))
    #     for i in range(0,len(data_by),3):
    #         print(i,data_by[i:i+3:1])
    # except Exception as e:
    #     print(e)
    # data_b = bytes()
    # data_s = str()
    # print(type(data_b),type(data_s))
    my_serve_gy = socketserver.ThreadingTCPServer((settings.BIND_IP,settings.BIND_PORT),GY_Server)
    my_serve_gy.serve_forever()
