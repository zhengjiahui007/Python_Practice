#!/usr/bin/python3
#!_*_coding:utf-8_*_
#!author:Garry Zheng

import os,sys,socket,inspect

from config import settings

def client_cmd(con_soc:socket,cmd:list):
    print(cmd)

def client_post(con_soc:socket,cmd:list):
    print(cmd)

def client_get(con_soc:socket,cmd:list):
    print(cmd)

def client_exit():
    exit()
    return

def client_help_info():
    print("""
        help | help info
        cmd | command,for example : cmd | ls
        post | upload file path
        get | download file path
        exit | exit
    """)

def client_excute(con_socket:socket):
    choice_dict = {
        "cmd" : client_cmd,
        "post" : client_post,
        "get" : client_get,
        "exit" : client_exit
    }
    client_help_info()
    while True:
        inp_cmd = input("Please input the command : ")
        if ('help' == inp_cmd):
            client_help_info()
            continue
        '''
        Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
        而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
        '''
        cmd_list = inp_cmd.split('|')
        choice_client = cmd_list[0]
        if choice_client in choice_dict:
            choice_dict[choice_client](con_socket,cmd_list[1:])

def client_main():
    try:
        gy_socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
        server_address = (settings.SERVER_IP,settings.PORT)
        gy_socket_client.connect(server_address)
        print("client_main")
        rec_welcome_message = gy_socket_client.recv(1024)
        print(rec_welcome_message.decode("utf8"))
        print(str(rec_welcome_message,encoding='utf-8'))
        client_excute(gy_socket_client)
    except Exception as e:
        print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))

    return
