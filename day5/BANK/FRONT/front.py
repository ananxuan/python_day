#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
sys.path.append("..")
from BACKEND import card


import re,hashlib
def check_password_complexity(card_passwd):
    if re.search('\d',card_passwd) and re.search('[a-zA-Z_]',card_passwd) and re.search('[\W]',card_passwd) and 10 <= len(card_passwd) <= 20:
        return True


def create_account():
    """

    :return:
    """
    # 生成信用卡id
    card_id = card.create_card_id()
    print("给您生成的信用卡id是:\033[1;31;0m%s\033[0m"%(card_id))
    # 设置密码
    while True:
        print("你可以设置这个密码：J12%^sf1234")
        card_password = str(input("请为您的信用卡设置密码：>")).strip()
        if check_password_complexity(card_password):
            break
        else:
            print("\033[1;31;40m密码不符合复杂度要求，密码必须包含数字、字母、和特殊字符，长度在10个到20个字符之间！\033[0m")
    # 获取密码的md5值
    m1 = hashlib.md5()
    m1.update(card_password.encode(encoding='utf-8'))
    card_password_md5 = m1.hexdigest()
    # print(type(card_password_md5))
    # print(card_password_md5)
    # 生成信用卡
    return card.create_card(card_id,card_password_md5)

if __name__ == "__main__":
    print("请执行begin_from_here.py")

