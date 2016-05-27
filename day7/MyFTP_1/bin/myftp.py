#!/usr/bin/env python3.5
__author__ = 'DSOWASP'


import subprocess
import sys
import os
import socketserver
import configparser


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
print(BASEDIR)

from bin import simpleftpd
from bin import server_socket
from bin import writelogging




CONGFILE = "{}/conf/simpleftp.conf".format(BASEDIR)
BASENAME = os.path.basename(__file__).split(r".")[0]


class MyFtp(object):

    def __init__(self,ipaddr,port):
        self.iport = (ipaddr,port)

    def start(self):
        try:
            server = socketserver.ThreadingTCPServer(self.iport,server_socket.MyTCPHandler)
            server.serve_forever()
        except KeyboardInterrupt as e:
            print(e)


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
    if len(sys.argv) != 2 :
        print(r"Usage: myftp.py {start|stop|restart|status}")
    else:
        # 读取配置文件
        ipaddr,port = read_conf("ftp","ipaddr","port")
        mf = MyFtp(ipaddr,port)
        if hasattr(mf,sys.argv[1]):
            fun = getattr(mf,sys.argv[1])
            fun()