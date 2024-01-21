import socketserver

class GY_Serve(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        while True:
            try:
                print("Starting GY_Serve ... !")
                con_sock = self.request
                print(con_sock,self.client_address)
            except Exception as e:
                print("Here is an exception : ",e)
                continue
            else:
                while True:
                    try:
                        print("serve waiting ...")
                        rec_mess = con_sock.recv(1024)
                        print("....",str(rec_mess,'UTF-8'))
                        if not rec_mess:break
                        send_mess = input(">>>")
                        con_sock.send(send_mess.encode('UTF-8'))
                    except Exception as e:
                        print("Here is a new exception : ",e)
                        break
                con_sock.close()
        return

if __name__ == "__main__":
    my_serve_gy = socketserver.ThreadingTCPServer(("127.0.0.1",8091),GY_Serve)
    my_serve_gy.serve_forever()
