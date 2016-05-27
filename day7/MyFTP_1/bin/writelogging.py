#!/usr/bin/env python3
__author__ = 'DSOWASP'
import logging
import sys
import os
import subprocess

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

# 获取主机名
hn = subprocess.Popen("hostname",shell=True,stdout=subprocess.PIPE)
hostname = hn.stdout.read().decode().strip()


# 写日志类
class Wlog(object):
    # 日志目录
    LOGGING_BASE = "{}/logs".format(BASEDIR)
    def __init__(self,logfile,pname):
        """

        :param logfile: 指定日志文件
        :param pname: 指定进程名
        :return:
        """
        # 日志文件
        logging_file = "{}/{}".format(Wlog.LOGGING_BASE,logfile)
        # 实例化日志句柄
        self.logger = logging.getLogger(pname)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(logging_file)
        # ch = logging.StreamHandler()
        formatter = logging.Formatter(fmt='%(asctime)s %(hostname)s %(name)s %(levelname)s: %(message)s',datefmt='%b %d %H:%M:%S')
        self.extraoption = {"hostname":hostname}
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        self.logger.addHandler(fh)

    # 写日志
    def wlog(self,level,message):
        """

        :param level: 写日志级别
        :param message: 写日志消息
        :return:
        """
        fun = self.logger.__getattribute__(level)
        fun(message,extra=self.extraoption)