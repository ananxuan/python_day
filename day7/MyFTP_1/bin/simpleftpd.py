#!/usr/bin/env python3
__author__ = 'DSOWASP'

import configparser
import socket
import sys
import os
import subprocess
import socketserver


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from bin import writelogging

CONGFILE = "{}/conf/simpleftp.conf".format(BASEDIR)
BASENAME = os.path.basename(__file__).split(r".")[0]




class MyTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self,port,ipaddr):
        self.port = port
        self.ipaddr = ipaddr
        self.cid = 0
        self.__run()
        



    def __run(self):
        self.sk = socket.socket()
        self.sk.bind((self.ipaddr,self.port))

        # listen这里就是启动监听
        self.sk.listen(5)

        # 启动监听写日志
        loginfo1 = "The simpleftpd is listen on {}:{}".format(self.ipaddr,self.port)
        loginfo2 = "The simpleftpd is started"
        self.__wlog("info",loginfo1,loginfo2)

        # 开始接收数据
        while True:
            self.cid += 1
            conn,addr = self.sk.accept()


            # 客户点连接，写入日志
            self.__wlog("info","client %s:%s connected"%(addr[0],addr[1]))
            # 开始处理数据

            # 客户端认证
            if self.__auth(conn,addr):
                self.__deal_data(conn,addr)

    def __auth(self,conn,addr):
        # 发送消息告诉需要客户端认证
        conn.send(b"User:")


    def __deal_data(self,conn,addr):
        while True:
            try:
                b_r_client = conn.recv(1024)
                r_client = b_r_client.decode().strip()
                if not r_client:
                    print("客户端未发送数据！")
                    break
                print("客户端发过来的是:%s"%r_client)
                cmd_data = subprocess.Popen(r_client,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                cmd_data_out , cmd_error =  cmd_data.communicate()   # 返回bytes
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
                print("\033[1;31;0m客户端%d关闭连接！\033[0m"%self.cid)
                break

    def __wlog(self,level="info",*args):
        for loginfo in args:
            wl.wlog(level,loginfo)

def read_conf(section="ftp", *args):
    """

    :param section: 需要读取的section，默认为ftp
    :param args: 需要读取的option
    :return: 返回读取的option的值列表
    """
    cp = configparser.ConfigParser()
    cp.read(CONGFILE)
    values = []
    for option in args:
        try:
            if option.lower() == 'port':
                values.append(cp.getint(section,option))
            else:
                values.append(cp.get(section,option))
        except (configparser.NoOptionError,configparser.NoSectionError):
            values.append("None")
    return values


if __name__ == "__main__":
    # 实例化写日志
    wl = writelogging.Wlog("simpleftp.log",BASENAME)
    # 读取配置文件
    port,ipaddr = read_conf("ftp","port","ipaddr")
    # print(port,ipaddr)
    # 启动MyFtp实例
    mf = MyFtp(port,ipaddr)