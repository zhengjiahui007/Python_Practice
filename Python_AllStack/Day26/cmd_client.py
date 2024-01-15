import socket

client_socket_gy = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
servergy_address = ('127.0.0.1',8000)
print("Here is the client_socket_gy ... !")
client_socket_gy.connect(servergy_address)

while True:
    try:
        inp_mess = input(">>>")
        client_socket_gy.send(inp_mess.encode('UTF-8'))
        length_mess = int(str(client_socket_gy.recv(1024),'UTF-8'))
        print("length_mess =  ",length_mess)
        cmd_result = bytes()
        while (len(cmd_result) != length_mess):
            rec_re = client_socket_gy.recv(1024)
            cmd_result += rec_re
        else:
            print('''The result is %s
            ''' %(cmd_result.decode('gbk')))
    except Exception as e:
        print("An exception occured {}!".format(e))

client_socket_gy.close()