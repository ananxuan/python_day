#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
sys.path.append("..")
from BACKEND.API.bank_login_api import bank_login_api


class Atm:
    def __init__(self,bank_outlets):
        # 银行网点
        self.bank_outlets = bank_outlets

        pass

    # 欢迎页面
    def __welcome_page(self):
        # 函数字典
        g_fun_dic = {"1": self.__taoxian, "2": self.__huankuan, "3": self.__leave}

        print("1、套现")
        print("2、还款")
        print("3、退出")
        while True:
            select_id = input("请输入您要的操作> ").strip()
            if select_id not in ["1", "2", "3"]:
                print("错误输入！")
                continue
            else:
                return g_fun_dic[select_id]

    # 登录
    def __login(self):
        card_id = input("请输入你的信用卡id> ").strip()
        card_passwd = input("请输入你的密码> ").strip()
        if bank_login_api(card_id,card_passwd):
            print("调用bank_login_api成功")

    # 套现
    def __taoxian(self):
        print("套现")

    # 还款
    def __huankuan(self):
        print("还款")

    # 退出
    def __leave(self):
        print("退出")

    # 主函数
    def atm_begin(self):
        if self.__login() == False:
            exit()
        # 欢迎界面，然后根据输入的id执行相应的函数
        self.__welcome_page()()

# 程序入口
if __name__ == '__main__':
    # 银行网点，这个固定写死，一般是在初始化时手动设置
    bank_outlets = "招商银行火星支行"
    atm = Atm(bank_outlets)
    atm.atm_begin()
else:
    print("此文件不能被调用！")
