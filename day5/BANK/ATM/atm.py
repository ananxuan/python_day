#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
import hashlib
import json
import time
sys.path.append("..")
from BACKEND.API.bank_login_api import bank_login_api
from BACKEND import card



def welcome_page():
    # 函数字典
    g_fun_dic = {"1": taoxian, "2": huankuan, "3":query_bill, "4": leave}

    print("\033[1;32;m1、提现")
    print("2、还款")
    print("3、查询账单")
    print("4、退出\033[0m")
    while True:
        select_id = input("请输入您要的操作> ").strip()
        if select_id not in ["1", "2", "3", "4"]:
            print("错误输入！")
            continue
        else:
            return g_fun_dic[select_id]

# 登录
def login():
    error_times = 0
    while error_times < 3:
        card_id = input("请输入你的信用卡id> ").strip()
        card_passwd = input("请输入你的密码> ").strip()
        m1 = hashlib.md5()
        m1.update(card_passwd.encode(encoding='utf-8'))
        card_passwd_md5 = m1.hexdigest()
        session_id,login_flag =  bank_login_api(card_id,card_passwd_md5)
        if login_flag == True:
            print("调用bank_login_api成功")
            # print("您的会话id是:%s"%session_id)
            break
        else:
            error_times += 1
            print("登录失败！")
    else:
        return None

    while True:
        fun = welcome_page()
        some_flag = fun(card_id)
        if some_flag == "level":
            return None

# 套现
def taoxian(card_id):
    print("提现")
    money  = int(input("您要提现多少？> ").strip())
    if card.taoxian(card_id,money):
        print("套现成功！")
    else:
        print("余额不足")

# 还款
def huankuan():
    print("还款")

# 查询账单
def query_bill(card_id):
    print("查询账单")
    start_date  =  time.strptime("2016%s09"%(str(int(month)-1)),"%Y%m%d")
    month = input("您要查询几月份账单:> ").strip()
    need_pay = 0
    if int(month) in range(1,13):
        bill_content =  card.query_bill(card_id,month)
        for i in bill_content:
            i = json.loads(i)
            print("\033[1;31;0m%s\033[0m"%(i["shangpin"]))
            print(i["time"],end="")
            print(8*" ",end="")
            print("￥ ",i["money"])
            # if time.strptime(i["time"],"%Y%m%d") < start_date:
            #     zhinajin =
            # if i["type_id"] == 1:
            #
            #     # lixi = float(i["money"]) * (time.mktime(time.strptime(time.strftime("%Y%m%d",time.localtime()),"%Y%m%d")) - time.mktime(time.strptime(i["time"],"%Y%m%d")))/86400
            #     shouxufei =  i["money"] / 100.0
            #     if shouxufei < 10:
            #         shouxufei = 10.0
            #     print("￥ ",i["money"])
            #     print("套现手续费:%s"%shouxufei)
            need_pay += float(i["money"])
        print("\033[1;31;0m本期应还%.2f\033[0m"%need_pay,end="")
        print(8*" ",end="")
        print(r"最后还款日:%s/24"%(month))
        print(r"最低还款:%.2f"%(need_pay/10))



# 退出
def leave(*argv):
    print("退出")
    return "level"

