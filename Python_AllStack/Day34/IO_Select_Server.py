import socket
from select import *
 
server = socket.socket()
 
# 设置非阻塞
server.setblocking(False)
server.bind(('0.0.0.0', 8889))
server.listen(5)
 
# 输入队列
inputs = [server]
# 输出队列
outputs = []
# 存放消息
input_message = {}
 
while 1:
    # 等待事件响应
    r_list, w_list, e_lisy = select(inputs, outputs, [])
 
    # 先遍历可读的fd
    for r_client in r_list:
        # 如果接受的对象是server，表示server有消息到来
        if r_client is server:
            client, client_addr = server.accept()
            # 设置非阻塞
            client.setblocking(False)
            # 讲client放入接受监听对象
            inputs.append(client)
            input_message[client] = []
        else:   # 不是server，则代表是client发来的消息
            data = r_client.recv(1024)
            if data:
                input_message[r_client].append(data)
                # 讲当前连接放入可写队列，表示可写
                if r_client not in outputs:
                    outputs.append(r_client)
            else:
                # 数据为空，表示client断开
                if r_client in outputs:
                    outputs.remove(r_client)
                inputs.remove(r_client)
                input_message.pop(r_client)
 
    # 遍历可写的fd
    for w_client in outputs:
        # 取出之前client发送的数据
        messages = input_message.get(w_client)
        # 没有可发送的数据
        if not messages:
            # 删除该client
            outputs.remove(w_client)
            continue
        this_message = messages.pop(0)
        w_client.send(this_message.upper())
 