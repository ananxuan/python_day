#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
import os
import collections
sys.path.append("..")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_CARD_ACCOUNT_FILE = r"%s\DB\card_account"%BASE_DIR
LOGGING_BASE = r"%s\LOG"%BASE_DIR
DB_XIAOFEI_DIR = r"%s\DB\xiaofei"%BASE_DIR

import random
import time
import json
import logging
from BACKEND import wlog

SESSION_LIST = set({})


def create_card_id():
    card_id = '52'
    for i in range(14):
        current = random.randrange(0,9)
        card_id += str(current)
    return card_id

def create_session_id():
    session_start_time = time.time()
    session_id = ''
    for i in range(20):
        current = random.randrange(0,20)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        session_id += str(temp)
    SESSION_LIST.add((session_id,session_start_time))
    return session_id


def login(card_id,card_password):
    session_id = create_session_id()
    login_flag = False
    with open(DB_CARD_ACCOUNT_FILE,'r') as f:
        for i in f:
            i = json.loads(i)
            if card_id == i["card_id"] and card_password == i["card_password"]:
                return session_id,True
                login_flag = True
        if login_flag != True:
            return session_id,False



def create_card(card_id,card_password):
    """
    :param card_id:
    :param card_password:
    :return:
    """
    card_dic = collections.OrderedDict()
    card_dic["card_id"] = card_id
    card_dic["card_password"] = card_password
    # 信用卡额度
    card_dic["credit_limit"] = 20000
    # 账单日
    card_dic["statement_date"] = 10
    # 还款日
    card_dic["repayment_date"] = 23
    # 消费记录
    # card_dic["xiaofei"] = {}
    # card_json = json.loads(card_dic)
    # 将信用卡信息以json格式保存至数据库
    # try:
    # logging_dir = "%s\%s"%(LOGGING_BASE,time.strftime("%Y%m%d"))
    # logging_file = "%s\%s"%(LOGGING_BASE,card_id)
    # print(logging_dir)
    # print(os.listdir(LOGGING_BASE))
    # if time.strftime("%Y%m%d") not in os.listdir(LOGGING_BASE):
    #     os.mkdir(logging_dir)

    # logging.basicConfig(level=logging.INFO,
    #             filename=logging_file,
    #             filemode='a')
    with open(DB_CARD_ACCOUNT_FILE,'a') as f:
        json.dump(card_dic,f)
        f.write("\n")
    # logging.info("create card:%s"%card_id)
    wlog.wlog("create card:%s"%card_id)
    # 为了能够打印账单，这里模拟生成账单数据
    if moni_create_xiaofei(card_id):
        return True
    else:
        return False
    # except:
    #     return False

def mod_credit_limit(card_id,money):
    # logging_dir = "%s\%s"%(LOGGING_BASE,time.strftime("%Y%m%d"))
    logging_file = "%s\%s"%(LOGGING_BASE,card_id)
    flag = False
    TEMP_DB_CARD_ACCOUNT_FILE = "%s_temp"%DB_CARD_ACCOUNT_FILE
    with open(DB_CARD_ACCOUNT_FILE,'r') as f1,open(TEMP_DB_CARD_ACCOUNT_FILE,'w') as f2:
        for i in f1:
            i = json.loads(i)
            if card_id == i["card_id"] and -money <= i["credit_limit"]:
                i["credit_limit"] += money
                flag = True
            json.dump(i,f2)
            f2.write("\n")
    os.remove(DB_CARD_ACCOUNT_FILE)
    os.rename(TEMP_DB_CARD_ACCOUNT_FILE,DB_CARD_ACCOUNT_FILE)
    return flag

def moni_create_xiaofei(card_id):
    """

    :param card_id: 信用卡id
    :return:  None
    """
    DB_XIAOFEI_FILE = r"%s\%s"%(DB_XIAOFEI_DIR,card_id)
    card_dic1 = collections.OrderedDict()
    card_dic1["time"] = time.strftime("%Y%m%d",time.localtime(time.time() - 60 * 24 * 3600))
    card_dic1["shangpin"] = "buy pad on jd"
    card_dic1["money"] = 5000
    # type_id:0为购物，1为套现，2为还款
    card_dic1["type_id"] = 0

    card_dic2 = collections.OrderedDict()
    card_dic2["time"] = time.strftime("%Y%m%d",time.localtime(time.time() - 30 * 24 * 3600))
    card_dic2["shangpin"] = "buy pen on jd"
    card_dic2["money"] = 600
    card_dic2["type_id"] = 0

    # print(DB_XIAOFEI_FILE)
    with open(DB_XIAOFEI_FILE,'a') as f:
        json.dump(card_dic1,f)
        f.write("\n")
        json.dump(card_dic2,f)
        f.write("\n")

    mod_credit_limit(card_id,-(card_dic1["money"]+card_dic2["money"]))
    return True


def taoxian(card_id,money):
    TEMP_DB_CARD_ACCOUNT_FILE = "%s_temp"%DB_CARD_ACCOUNT_FILE
    flag = False
    # 修改账户信用余额
    if mod_credit_limit(card_id,-money) == True:
        flag = True

    # 写购买记录和操作日志
    DB_XIAOFEI_FILE = r"%s\%s"%(DB_XIAOFEI_DIR,card_id)
    if flag == True:
        xiaofei_dic1 = collections.OrderedDict()
        xiaofei_dic1["time"] = time.strftime("%Y%m%d")
        xiaofei_dic1["shangpin"] = "taoxian"
        xiaofei_dic1["money"] = money
        # type_id:0为购物，1为套现，2为还款
        xiaofei_dic1["type_id"] = 1
        with open(DB_XIAOFEI_FILE,'a') as f:
            json.dump(xiaofei_dic1,f)
            f.write("\n")
        wlog.wlog(card_id,"taoxian %d yuan"%money)
    return flag


def query_bill(card_id,month):
    flag = False
    start_date  =  time.strptime("2016%s09"%(str(int(month)-1)),"%Y%m%d")
    end_date = time.strptime("2016%s10"%(month),"%Y%m%d")
    # 消费记录文件
    DB_XIAOFEI_FILE = r"%s\%s"%(DB_XIAOFEI_DIR,card_id)
    record_list = []
    with open(DB_XIAOFEI_FILE,'r') as f:
        for i in f:
            i = json.loads(i)
            if start_date <= time.strptime(i["time"],"%Y%m%d") <= end_date:
                record_list.append(json.dumps(i))

    return record_list




