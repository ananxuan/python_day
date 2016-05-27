#!/usr/bin/env python3.5
__author__ = 'DSOWASP'



import socket
import sys
import  re
import getpass

class Ftp(object):
    def __init__(self,ipaddr,port):
        self.iport = (ipaddr,port)
        self.sk = socket.socket()
        self.sk.connect(self.iport)
        self.run()

    def run(self):
        # 确认服务器发送220消息
        server_status_msg = self.sk.recv(128).decode()
        # print("ser1:%s"%server_status_msg)
        if server_status_msg.split()[0] == "220":
            print(server_status_msg)
            if self.auth():
                pass

        while True:
            cmd_input = input("ftp> ").strip()



    def auth(self):
        # 发送用户名,用户名默认是ftp
        # username = "ftp"
        username = input("用户 (%s:(ftp)): "%self.iport[0]).strip()
        if username == "":
            username = "ftp"
        self.sk.send(bytes("USER %s\r\n"%username,"utf-8"))
        r_data = self.sk.recv(1024).decode()
        print(r_data.strip())
        r_data_code, r_data_msg = re.split(r"\s",r_data,1)
        if r_data_code == "331":
            password = getpass.getpass("pass: ").strip()
            self.sk.send(bytes("PASS %s\r\n"%password,"utf-8"))
            r_data = self.sk.recv(1024).decode()
            print(r_data.strip())
            r_data_code, r_data_msg = re.split(r"\s",r_data,1)
            if r_data_code == "230":
                return



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(r"Usage: ftp.py ip port")
    else:
        ftp = Ftp(sys.argv[1],int(sys.argv[2]))