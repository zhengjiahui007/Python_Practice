import socket
 
s = socket.socket()
 
ss = s.connect(('127.0.0.1', 8889))
 
while 1:
    message = input('>>>输入待发送消息: ')
    if message == 'exit':
        s.send(b'')
        break
    s.send(message.encode())
    data = s.recv(1024)
    print(f'client收到消息: {data.decode("utf-8")}')
 
 
s.close()