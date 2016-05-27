#!/usr/bin/env python3
__author__ = 'DSOWASP'

import  socketserver
import re


class MyTCPHandler(socketserver.BaseRequestHandler):

    code_msg  = {
        "220":b"{} FTP server ready\r\n",
        "230":b"User {} login in\r\n",
        "331":b"Password required for {}\r\n",
        "530":b"Login incorrect\r\n",
    }

    def auth(self):

        r_data = self.request.recv(1024).decode()
        r_data_cmd ,client_user = re.split(r"\s",r_data,1)
        if r_data_cmd == "USER":
            self.request.send(bytes((b"331 %s"%(self.code_msg["331"])).format(r_data_cmd)))
            r_data = self.request.recv(1024).decode()
            r_data_cmd ,client_pass = re.split(r"\s",r_data,1)
            if r_data_cmd == "PASS":
                if client_user == "DS" and client_pass == "123":
                    self.request.send((b"230 %s"%self.code_msg["230"]).format(client_user))
                else:
                    self.request.send(b"530 %s"%self.code_msg["530"])


    def handle(self):
        print("new connect:%s:%s"%self.client_address)
        # 告诉客户端连接成功
        self.request.send(b"220 %s %s"%(self.server,self.code_msg["220"]))
        self.auth()
        while True:
            # 这里只进行命令处理
            try:
                r_data = self.request.recv(1024).decode()
                r_data_cmd ,r_data_arg = re.split(r"\s",r_data,1)
                if not r_data:
                    print("客户端退出连接！")

                print("recv from %s:%s :%s"%(self.client_address,r_data))
                self.request.sen(r_data)
            except ConnectionResetError:
                print("client %s:%s is break connect"%self.client_address)
                break



# if __name__ == "__main__":
#     HOST,PORT = "localhost",9999
#
#     server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
#
#     server.serve_forever()