import socket

client_socket_gy = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
servergy_address = ('127.0.0.1',8091)
print("Here is the client_socket_gy ... !")
client_socket_gy.connect(servergy_address)

while True:
    try:
        inp_mess = input(">>>")
        if ('exit' == inp_mess):break
        client_socket_gy.send(inp_mess.encode('UTF-8'))
        rec_mess = client_socket_gy.recv(1024)
        print("> ",str(rec_mess,'UTF-8'))
    except Exception as e:
        print("An exception occured {}!".format(e))

client_socket_gy.close()