#!/usr/bin/env python3
__author__ = 'DSOWASP'

import socket

ip_port = ('192.168.5.124',9999)

sk = socket.socket()
sk.connect(ip_port)

while True:
    cmd = input("cmd> ")
    print("发送:%s"%cmd)
    if cmd == "q":
        break
    try:
        sk.send(bytes(cmd,"utf-8"))
        raw_data = sk.recv(1024)
    except ConnectionResetError:
        print("server break the connect")
        break
    print("recv:%s"%raw_data.decode())