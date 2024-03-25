#!/usr/bin/python3
#!_*_coding:utf-8_*_
#!author:Garry Zheng

import os,sys,socket,inspect,json,re

from config import settings
from lib import commons

'''
json.dump() 和 json.dumps() 都可以将 Python 对象转换为 JSON 字符串，但是它们之间有一些区别：
json.dumps() 将 Python 对象转换为 JSON 字符串，并返回该字符串。而 json.dump() 将 Python 对象转换为 JSON 字符串，并将该字符串写入文件。
json.dumps() 接受一个 Python 对象作为参数，而 json.dump() 接受两个参数：一个 Python 对象和一个写入数据的文件对象。
json.dump() 生成的 JSON 字符串会自动写入文件，而 json.dumps() 只是返回该字符串，需要手动进行处理。

'''

def client_login(conn:socket) -> bool:
    try:
        user_client = input("Please input your user name : ")
        pwd_client = input("Please input your password : ")
        user_info = [user_client,pwd_client]
        user_info_str = json.dumps(user_info)
        conn.send(user_info_str.encode('utf-8'))
        receive_message = conn.recv(1024)
        print(receive_message.decode('utf-8'))
        if ('4002' == receive_message.decode('utf-8')):
            print("Login successfully !")
            return True
        else:
            print("Login failed !")
            return False
    except Exception as e:
        print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
    return False

def client_cmd(con_soc:socket,cmd:str):
    print(cmd)
    con_soc.send(cmd.encode('utf-8'))
    result_info_bytes = con_soc.recv(1024)
    result_info_str = result_info_bytes.decode('utf-8')
    result_list = result_info_str.split('|')
    print(" result_list[1] = ",result_list[1])
    result_len = int(result_list[1])
    con_soc.send(bytes('ack',encoding='utf-8'))
    rece_len = 0
    result_bytes = bytes()
    while (rece_len < result_len):
        temp_bytes = con_soc.recv(1024)
        rece_len += len(temp_bytes)
        result_bytes += temp_bytes
        print("rece_len = ",rece_len)
    print(result_bytes.decode('gbk'))
    return

def client_post(con_soc:socket,cmd:str):
    #post | 12.txt 12.txt
    print(cmd)
    cmd_list = cmd.split(' | ')
    file_path_list = re.split('\s+',cmd_list[1],1)
    print(file_path_list)
    local_file_path = file_path_list[0]
    target_file_path = file_path_list[1]
    file_name = os.path.basename(local_file_path)
    file_md5 = commons.fetch_file_md5(local_file_path)
    print("type is ",type(file_md5))
    file_size = os.path.getsize(local_file_path)
    print(file_md5,file_size)
    file_info_str = "post | %s %s %s %s" %(file_name,target_file_path,file_size,file_md5)
    print(file_info_str)
    file_has_sent_size = 0
    user_choice = '1'
    con_soc.send(file_info_str.encode('utf-8'))
    recv_ack = con_soc.recv(1024)
    print("rec = ",recv_ack.decode('utf-8'))
    if ('2003' == recv_ack.decode('utf-8')):
        user_choice = input("File exists,continue to upload or not (Y/N) : ")
        if ('Y' == user_choice):
            con_soc.send(bytes('2004',encoding = 'utf-8'))
            recv_ack = con_soc.recv(1024)
            recv_ack_str = recv_ack.decode('utf-8')
            cmd_list = recv_ack_str.split('|')
            print(cmd_list)
            con_soc.send(bytes('3001',encoding = 'utf-8'))
            recv_ack = con_soc.recv(1024)
            if ('2002' == recv_ack.decode('utf-8')):
                file_has_sent_size = int(cmd_list[1])
                # with open(local_file_path,'rb') as file_p:
                #     file_p.seek(file_has_sent_size)
                #     while (file_has_sent_size < file_size):
                #         temp_sent = file_p.read(1024)
                #         con_soc.send(temp_sent)
                #         file_has_sent_size += len(temp_sent)
                #         #print("1  file_has_sent_size = ",file_has_sent_size)
                #     else:
                #         print("2  file_has_sent_size = ",file_has_sent_size)
                #         con_soc.send(bytes('2006',encoding = 'utf-8'))
                #         recv_mess = con_soc.recv(1024)
                #         if ('2007' == recv_mess.decode('utf-8')):
                #             print("Upload successfully !!!!")
                #         else:
                #             print("Upload failed !!!!")
        elif ('N' == user_choice):
            con_soc.send(bytes('2005',encoding = 'utf-8'))
            recv_ack = con_soc.recv(1024)

    if ('2002' == recv_ack.decode('utf-8')):
        #file_has_sent_size = 0
        print("11 rec = ",recv_ack.decode('utf-8'))
        with open(local_file_path,'rb') as file_p:
            file_p.seek(file_has_sent_size)
            while (file_has_sent_size < file_size):
                temp_sent = file_p.read(1024)
                con_soc.send(temp_sent)
                file_has_sent_size += len(temp_sent)
                if (('1' == user_choice) and (1024*1024 < file_has_sent_size)):
                    print("223445")
                    break
                #print("1  file_has_sent_size = ",file_has_sent_size)
            else:
                print("2  file_has_sent_size = ",file_has_sent_size)
                con_soc.send(bytes('2006',encoding = 'utf-8'))
                recv_mess = con_soc.recv(1024)
                if ('2007' == recv_mess.decode('utf-8')):
                    print("Upload successfully !!!!")
                else:
                    print("Upload failed !!!!")
    return

def client_get(con_soc:socket,cmd:str):
    print(cmd)
    con_soc.send(cmd.encode('utf-8'))
    return

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

    while True:
        if client_login(con_socket):
            while True:
                client_help_info()
                inp_cmd = input("Please input the command : ")
                if ('help' == inp_cmd):
                    client_help_info()
                    continue
                '''
                Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
                而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
                '''
                cmd_list = inp_cmd.split(' | ')
                choice_client = cmd_list[0]
                if choice_client in choice_dict:
                    choice_dict[choice_client](con_socket,inp_cmd)
        else:
            print("Please input the correct info !")
            continue
    return

def client_main():
    gy_socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
    try:
        server_address = (settings.SERVER_IP,settings.PORT)
        gy_socket_client.connect(server_address)
        print("client_main")
        rec_welcome_message = gy_socket_client.recv(1024)
        print(rec_welcome_message.decode("utf-8"))
        #print(str(rec_welcome_message,encoding='utf-8'))
        client_excute(gy_socket_client)
        gy_socket_client.close()
    except Exception as e:
        print("%s : %s @ line : %s A exception occurred %s" % (os.path.basename(__file__),inspect.currentframe().f_code.co_name,inspect.currentframe().f_lineno,e))
        gy_socket_client.close()
    return
