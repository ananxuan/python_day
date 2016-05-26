#!/usr/bin/env python3
__author__ = 'DSOWASP'

import  socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    cid = 0

    def handle(self):
        self.cid += 1
        print("new connect:%s:%s"%self.client_address)
        while True:
            try:
                r_data = self.request.recv(1024)
                if not r_data:
                    print("客户端退出连接！")

                print("recv from %s:%s :%s"%(self.client_address,self.cid,r_data.decode()))
                self.request.send(r_data)
            except ConnectionResetError:
                print("client %s:%s is break connect"%self.client_address)
                break



if __name__ == "__main__":
    HOST,PORT = "localhost",9999

    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)

    server.serve_forever()