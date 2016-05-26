#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import subprocess


ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(2)

cid = 0

while True:
    cid += 1
    print('server waiting...')
    conn,addr = sk.accept()
    # client_data = conn.recv(1024)
    # print(str(client_data,'utf8'))
    # conn.sendall(bytes('不要回答,不要回答,不要回答','utf8'))
    while True:
        try:
            client_data = conn.recv(8192)
            str_clinet_data = str(client_data,'utf8').strip()
            if not client_data.decode():
                print("\033[1;31;0m客户端未发送数据!\033[0m")
                break
            print("接收数据,客户端%d:\033[1;31;0m%s\033[0m"%(cid,str_clinet_data))
            cmd_data = subprocess.Popen(str_clinet_data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_data_out , cmd_error =  cmd_data.communicate()   # 返回bytes
            # if cmd_error != bytes("","utf-8"):
            if cmd_error:
                cmd_data_result = cmd_error
            else:
                cmd_data_result = cmd_data_out
            try:
                print(str(cmd_data_result,"gbk"))
            except UnicodeDecodeError:
                print(str(cmd_data_result,"utf-8"))
            # conn.send(client_data)
            cmd_result_size = b"CMD_RESULT_SIZE|%d"%len(cmd_data_result)
            # print(cmd_result_size)
            conn.send(cmd_result_size)

            client_ack = conn.recv(20)
            if client_ack == b"CMD_RESULT_SIZE_OK":
                print("收到客户端的确认，开始发送数据！")
                conn.send(cmd_data_result)
        except ConnectionResetError:
            print("\033[1;31;0m客户端%d关闭连接！\033[0m"%cid)
            break
    conn.close()
