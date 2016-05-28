#!/usr/bin/env python3
__author__ = 'DSOWASP'

import  socketserver
import re
import  os


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    code_msg  = {
        "220":"{} FTP server ready\r\n",
        "230":"User {} login in\r\n",
        "331":"Password required for {}\r\n",
        "530":"Login incorrect\r\n",
    }
    """
    code_msg  = {
        "220":"{} FTP server ready\r\n",
        "230":"User {} login in\r\n",
        # "330":"{} ",
        "331":"Password required for {}\r\n",
        "530":"Login incorrect\r\n",
    }

    def auth(self):

        r_data = self.request.recv(1024).decode()
        r_data_cmd ,client_user = re.split(r"\s",r_data,1)
        client_user = client_user.strip()
        print("user:%s"%client_user)
        if r_data_cmd == "USER":
            self.request.send(bytes("331 %s"%(self.code_msg["331"]).format(r_data_cmd),"utf-8"))
            r_data = self.request.recv(1024).decode()
            r_data_cmd ,client_pass = re.split(r"\s",r_data,1)
            client_pass = client_pass.strip()
            print("pass:%s"%client_pass)
            if r_data_cmd == "PASS":
                if client_user == "DS" and client_pass == "123":
                    self.request.send(bytes(("230 %s"%self.code_msg["230"]).format(client_user),"utf-8"))
                    self.login_status = True
                else:
                    self.request.send(bytes(("530 %s"%self.code_msg["530"]),"utf-8"))
                    self.login_status = False



    def get(self,filename):

        # try:
        fsize = os.path.getsize(filename)
        f = open(filename,"rb")
        print(bytes("fsize:%s"%fsize,"utf-8"))
        self.request.send(bytes("330 %s"%fsize,"utf-8"))
        send_size = 0
        while send_size< fsize:
            content = f.read(4096)
            self.request.send(content)
            send_size += len(content)
        # except Exception as e:
        #     print(e)





    def handle(self):
        print("new connect:%s:%s"%self.client_address)
        # 告诉客户端连接成功
        self.request.send(bytes(("220 {}".format(self.code_msg["220"])).format("127.0.0.1"),"utf-8"))
        self.auth()
        # 客户端未认证，密码md5传输还未实现
        while True:
            # 这里只进行命令处理
            try:
                r_data = self.request.recv(4096).decode()
                r_data_cmd ,r_data_arg = re.split(r"\s",r_data,1)
                if not r_data:
                    print("客户端退出连接！")

                print("recv from %s :%s"%(self.client_address,r_data))
                print("r_data_cmd:%s"%r_data_cmd)
                if hasattr(self,r_data_cmd):
                    print("服务器开始调用函数")
                    fun = getattr(self,r_data_cmd)
                    fun(r_data_arg)
            except ConnectionResetError:
                print("client %s:%s is break connect"%self.client_address)
                break



# if __name__ == "__main__":
#     HOST,PORT = "localhost",9999
#
#     server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
#
#     server.serve_forever()