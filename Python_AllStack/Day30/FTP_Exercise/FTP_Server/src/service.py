#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
#！/usr/bin/env python 3

import os,sys,inspect,pickle
import subprocess
import re
import json
import socketserver,socket
from config import settings
from lib import commons

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
    '2006': "上传完毕",
    '2007': "上传成功",
    '2008': "上传失败",
    '3001': 'get info',
    '3002': 'get ack',
    '4001': "用户登录",
    '4002': "授权成功",
    '4003': "授权失败",
    '4004': "创建账户",
    '4005': "创建成功",
    '4006': "创建失败",
    '4007': "账户已存在",
    '4008': "用户退出"

}


class GY_Server(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        server_sock_gy = self.request
        while True:
            print("Starting GY_Serve ... !")
            #print(server_sock_gy,self.client_address)
            welcome_message = "Welcome Online !"
            server_sock_gy.send(welcome_message.encode('utf-8'))
            obj_action = Server_Action(server_sock_gy)
            while True:
                recv_action = server_sock_gy.recv(1024)
                rece_str = recv_action.decode("utf-8")
                cmd_list = rece_str.split(' | ',1)#返回分割后的字符串列表。
                if ('4004' == cmd_list[0]):
                    print(cmd_list[0],cmd_list[1])
                    user_list = json.loads(cmd_list[1])
                    print(user_list)
                    if commons.check_user_exist(settings.USER_DBASE,user_list[0]):
                        server_sock_gy.send(bytes('4007',encoding = 'utf-8'))
                        continue
                    else:
                        obj_action.creat(user_list[0],user_list[1])
                        server_sock_gy.send(bytes('4005',encoding = 'utf-8'))
                        continue
                elif ('4001' == cmd_list[0]):
                    print(cmd_list[0],cmd_list[1])
                    user_list = json.loads(cmd_list[1])
                    print(user_list)
                    obj_action.login(user_list[0],user_list[1])
                elif ('4008' == cmd_list[0]):
                    del obj_action
                    break
                while True:
                    if obj_action.has_login:
                        rece_action = server_sock_gy.recv(1024)
                        if not rece_action:
                            break
                        rece_str = rece_action.decode("utf-8")#str(rece_action,encoding = 'utf-8')
                        cmd_list = rece_str.split(' | ',1)#返回分割后的字符串列表。
                        print(cmd_list[0],cmd_list[1])
                        if ('4008' == cmd_list[0]):
                            del obj_action
                            break
                        action_attr = getattr(obj_action,cmd_list[0])
                        action_attr(cmd_list[1])
                    else:
                        server_sock_gy.send("Please login !".encode('utf-8'))
                        break
        server_sock_gy.close()
        return

class Account_Info():
    def __init__(self,user:str,pwd:str):
        self.username = user
        self.password = pwd
        return

class Server_Action(object):
    def __init__(self, conn:socket):
        self.conn = conn
        self.has_exist = False
        self.has_login = False
        self.username = None
        self.home = None
        self.current_dir = None
        self.db_path = settings.USER_DBASE
        return

    def creat(self,user:str,pwd:str):
        db_file_name = user
        acc_obj = Account_Info(user,pwd)
        db_file_path = os.path.join(self.db_path,db_file_name)
        with open(db_file_path,'wb') as file_p:
            pickle.dump(acc_obj,file_p)
        
        self.username = user
        self.home = os.path.join(settings.USER_HOME,self.username)
        if not os.path.exists(self.home):
            os.mkdir(self.home,0o755)
            self.current_dir = os.path.join(settings.USER_HOME, self.username)
        else:
            print("The {} folder has existed !".format(self.username))
            return False
        return True

    def login(self,user:str,pwd:str) -> bool:
        db_file_path = os.path.join(self.db_path,user)
        with open(db_file_path,'rb') as file_p:
            acc_obj = pickle.load(file_p)
            if (user == acc_obj.username) and (pwd == acc_obj.password):
                result_code = '4002'
                self.has_login = True
                self.username = user
                self.server_initialize()
            else:
                result_code = '4003'
                self.has_login = False
            print(result_code)
            self.conn.send(result_code.encode('utf-8'))
        return

    def server_initialize(self):
        self.home = os.path.join(settings.USER_HOME, self.username)
        self.current_dir = os.path.join(settings.USER_HOME, self.username)
        return

    def post(self,conmand:str):
        print(conmand)
        file_name,target_file_path,file_size,file_md5 = conmand.split(" ")
        print(file_name,target_file_path,file_size,file_md5)
        file_size_int = int(file_size)
        file_server_path = os.path.join(self.home,target_file_path)

        file_has_received_size = 0
        file_exist_size = 0
        if os.path.exists(file_server_path):
            print("File exists !")
            self.conn.send(bytes('2003',encoding = 'utf-8'))
            temp_recvd = self.conn.recv(1024)
            if ('2004' == temp_recvd.decode('utf-8')):
                file_exist_size = os.path.getsize(file_server_path)
                file_exit_info = 'info|%d'%(file_exist_size)
                self.conn.send(bytes(file_exit_info,encoding = 'utf-8'))
                temp_recvd = self.conn.recv(1024)
                print("11 File exists !")
                if ('3001' == temp_recvd.decode('utf-8')):
                    # self.conn.send(bytes('2002',encoding = 'utf-8'))
                    print("File file_exist_size =  ",file_exist_size)
                    file_has_received_size = file_exist_size
                    file_p = open(file_server_path,'ab')
                    #with open(file_server_path,'ab') as file_p:
                        # while (file_has_received_size < file_size_int):
                        #     temp_recvd = self.conn.recv(1024)
                        #     file_p.write(temp_recvd)
                        #     file_has_received_size += len(temp_recvd)
                        #     #print("file_has_received_size = ",file_has_received_size)
                        # else:#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
                        #     file_p.close()
                        #     temp_recvd = self.conn.recv(1024)
                        #     if ('2006' == temp_recvd.decode('utf-8')):
                        #         print("2 file_has_received_size = ",file_has_received_size)
                        #         file_server_md5 = commons.fetch_file_md5(file_server_path)
                        #         if file_md5 == file_server_md5:
                        #             self.conn.send(bytes('2007',encoding = 'utf-8'))
                        #         else:
                        #             self.conn.send(bytes('2008',encoding = 'utf-8'))
            elif ('2005' == temp_recvd.decode('utf-8')):
                print("No need to continue to upload !")
                file_exist_size = -1
                os.remove(file_server_path)
                file_p = open(file_server_path,'wb')
                # self.conn.send(bytes('2002',encoding = 'utf-8'))
                # with open(file_server_path,'wb') as file_p:
                #     while (file_has_received_size < file_size_int):
                #         temp_recvd = self.conn.recv(1024)
                #         file_p.write(temp_recvd)
                #         file_has_received_size += len(temp_recvd)
                #         #print("file_has_received_size = ",file_has_received_size)
                #     else:#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
                #         file_p.close()
                #         temp_recvd = self.conn.recv(1024)
                #         if ('2006' == temp_recvd.decode('utf-8')):
                #             print("2 file_has_received_size = ",file_has_received_size)
                #             file_server_md5 = commons.fetch_file_md5(file_server_path)
                #             if file_md5 == file_server_md5:
                #                 self.conn.send(bytes('2007',encoding = 'utf-8'))
                #             else:
                #                 self.conn.send(bytes('2008',encoding = 'utf-8'))
        else:
            file_p = open(file_server_path,'wb')
        self.conn.send(bytes('2002',encoding = 'utf-8'))
        print("rec = 111 ")
        # with open(file_server_path,'wb') as file_p:
        while (file_has_received_size < file_size_int):
            temp_recvd = self.conn.recv(1024)
            file_p.write(temp_recvd)
            file_has_received_size += len(temp_recvd)
            # if ((0 == file_exist_size) and (1024*1024 < file_has_received_size)):
            #     print("11223")
            #     break
            #print("file_has_received_size = ",file_has_received_size)
        else:#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
            file_p.close()
            temp_recvd = self.conn.recv(1024)
            if ('2006' == temp_recvd.decode('utf-8')):
                print("2 file_has_received_size = ",file_has_received_size)
                file_server_md5 = commons.fetch_file_md5(file_server_path)
                if file_md5 == file_server_md5:
                    print("2000000007")
                    self.conn.send(bytes('2007',encoding = 'utf-8'))
                else:
                    print("2000000008")
                    self.conn.send(bytes('2008',encoding = 'utf-8'))
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
                        print("i = ",i)
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
    # 假设有GBK编码的字符串
    # gbk_string = "你好世界".encode('gbk')
    # print(type(gbk_string))
    
    # # 将GBK编码的字符串解码为Unicode，然后重新编码为UTF-8
    # utf8_string = gbk_string.decode('gbk').encode('utf-8').decode('utf-8')
    # print(utf8_string,type(utf8_string))
    my_serve_gy = socketserver.ThreadingTCPServer((settings.BIND_IP,settings.BIND_PORT),GY_Server)
    my_serve_gy.serve_forever()
