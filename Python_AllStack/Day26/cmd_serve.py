import socket,subprocess

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
                obj_cmd = subprocess.Popen(rec_message.decode('utf8'),shell = True,stdout = subprocess.PIPE)
                print("1 obj_cmd = " ,type(obj_cmd))
                obj_cmd_result = obj_cmd.stdout.read()
                cmd_result_len_byte = str(len(obj_cmd_result)).encode('utf8')
                send_len = gy_client_soc.send(cmd_result_len_byte)
                print("1 send_len = " ,send_len)
                send_len = gy_client_soc.send(obj_cmd_result)
                print("2 send_len = " ,send_len)
            except Exception as e:
                print("Here gy_client_soc  an exception ",e)
                break
            else:
                print("cmd {} run finish !".format(str(rec_message,'utf8')))

gy_client_soc.close()
