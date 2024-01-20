import socket
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
File_Store_Flolder = "Lessons_pic"
gy_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
servergy_address = ('127.0.0.1',8000)
gy_server.bind(servergy_address)
gy_server.listen(3)

print("Here is the gy_server ... !")
while True:
    try:
        gy_client_soc,gy_client_add = gy_server.accept()
    except Exception as e:
        print("Here is an exception ",e)
        continue
    else:
        while True:
            try:
                rec_message = gy_client_soc.recv(1024)
                print("... ... ",rec_message.decode('utf8'),type(rec_message))
                rec_cmd,rec_filename,rec_filesize = rec_message.decode('utf8').split('|')
                print(rec_cmd,rec_filename,rec_filesize)
                gy_client_soc.send(bytes("Receive file info OK!",'UTF-8'))
                file_rece_len = 0
                rec_filesize = int(rec_filesize)
                rec_file_path = os.path.join(BASE_DIR,File_Store_Flolder,rec_filename)
                with open(rec_file_path,'wb') as f_pic:
                    while (file_rece_len < rec_filesize):
                        rec_data = gy_client_soc.recv(1024)
                        write_len_temp = f_pic.write(rec_data)
                        file_rece_len += write_len_temp
                    else:
                        #print("wait for client mess!")
                        rec_data = gy_client_soc.recv(1024)
                        if ("Post finish!" == rec_data.decode('utf8')):
                            gy_client_soc.send(bytes("Receive finish!",'utf8'))
                        #print("Receive finish!")
                        f_pic.close()
            except Exception as e:
                print("Here gy_client_soc  an exception ",e)
                gy_client_soc.close()
                break
            else:
                print("Receive {} finish !".format(rec_file_path))

gy_client_soc.close()