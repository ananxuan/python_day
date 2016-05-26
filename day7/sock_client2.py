#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

# sk.sendall(bytes('请求占领地球','utf8'))
# server_reply = sk.recv(1024)
# print(str(server_reply,'utf8'))

while True:
    user_input = input("cmd>>:").strip()
    if user_input == "":
        continue
    if user_input == 'q':break

    sk.send(bytes(user_input,'utf8'))
    # print("发送数据: \033[1;32;0m%s\033[0m"%user_input)

    server_reply_size_data = sk.recv(50)
    # print(server_reply_size_data)
    server_reply_size_flag, server_reply_size = server_reply_size_data.decode("utf-8").split("|")
    server_reply_size = int(server_reply_size)
    if server_reply_size_flag == "CMD_RESULT_SIZE":
        print("服务端将发送字节数:%d"%server_reply_size)
        print("给服务端发送确认！")
        sk.send(b"CMD_RESULT_SIZE_OK")
    server_result = b""
    recv_size = 0
    # n = 1
    while recv_size < server_reply_size:
        server_reply = sk.recv(500)
        server_result += server_reply
        recv_size += len(server_reply)
        print("共接收%d字节"%recv_size)
        # code,server_result = str(server_reply[:9].split(b'0')[0],"utf-8"),server_reply[9:]
    else:
        print("------load-done-----")
        print("\033[1;32;0m%s\033[0m"%str(server_result,"gbk"),end="")
    # try:
    #     print("接收数据: \033[1;32;0m%s\033[0m"%str(server_reply,'utf-8'))
    # except UnicodeDecodeError:
    #     print("接收数据: \033[1;32;0m%s\033[0m"%str(server_reply,'gbk'))
sk.close()
