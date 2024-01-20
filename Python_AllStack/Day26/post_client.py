import socket
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

client_socket_gy = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
servergy_address = ('127.0.0.1',8000)
print("Here is the client_socket_gy ... !")
client_socket_gy.connect(servergy_address)

while True:
    try:
        inp_mess = input(">>>") #post|filename, strip can
        if ("exit" == inp_mess):
            break
        inp_cmd,inp_file_pathname = inp_mess.strip().split('|')
        inp_pathfilename = os.path.join(BASE_DIR,inp_file_pathname)
        inp_filename = os.path.basename(inp_pathfilename)
        inp_filesize = os.path.getsize(inp_pathfilename) # os.stat(inp_pathfilename).st_size

        send_fileinof = "post|{}|{}".format(inp_filename,inp_filesize)

        client_socket_gy.send(send_fileinof.encode('UTF-8'))
        rec_mess = (str(client_socket_gy.recv(1024),'UTF-8'))
        if ("Receive file info OK!" == rec_mess):
            print(rec_mess)
            file_sent_len = 0
            with open(inp_pathfilename,'rb') as f_pic:
                while (file_sent_len < inp_filesize):
                    temp_data = f_pic.read(1024)
                    file_sent_len += len(temp_data)
                    client_socket_gy.send(temp_data)
                else:
                    #print("Send post finish !")
                    client_socket_gy.send(bytes("Post finish!",'utf8'))
                    rec_mess = (str(client_socket_gy.recv(1024),'UTF-8'))
                    if ("Receive finish!" == rec_mess):
                        print(rec_mess)
                    f_pic.close()
        else:
            print("Not receive file file info !")
            continue
    except Exception as e:
        print("An exception occured {}!".format(e))
        continue

client_socket_gy.close()