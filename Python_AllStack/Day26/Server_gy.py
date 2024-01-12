import socket

server_soc_gy = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0,None)
servergy_address = ('127.0.0.1',8000)
server_soc_gy.bind(servergy_address)
server_soc_gy.listen(3)
print("Here is the server_soc_gy ... !")

while True:
    try:
        print("Waiting server_soc_gy ... !")
        con_sock,con_address = server_soc_gy.accept()
        print(con_sock,con_address)
    except Exception as e:
        print("Here is an exception : ",e)
        continue
    else:
        while True:
            try:
                rec_mess = con_sock.recv(1024)
                print("....",str(rec_mess,'UTF-8'))
            except Exception as e:
                print("Here is a new exception : ",e)
                break
            else:
                if not rec_mess:break
                send_mess = input(">>>")
                con_sock.send(send_mess.encode('UTF-8'))

con_sock.close()

