#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
sys.path.append("..")
from BACKEND import card

DB_CARD_ACOUNT_FILE = '../../DB/card_account'


import re,hashlib
def check_password_complexity(card_passwd):
    if re.search('\d',card_passwd) and re.search('[a-zA-Z_]',card_passwd) and re.search('[\W]',card_passwd) and 10 <= len(card_passwd) <= 20:
        return True


def create_account():
    print("现在开始注册账户!")
    card_id = card.create_card_id()
    print("给您生成的信用卡id是:%s"%(card_id))
    while True:
        card_password = str(input("请为您的信用卡设置密码：>")).strip()
        if check_password_complexity(card_password):
            break
        else:
            print("\033[1;31;40m密码不符合复杂度要求，密码必须包含数字、字母、和特殊字符，长度在10个到20个字符之间！\033[0m")
    m1 = hashlib.md5()
    m1.update(card_password.encode(encoding='utf-8'))
    card_password_md5 = m1.hexdigest()
    print(card_password_md5)
    with open(DB_CARD_ACOUNT_FILE,'a') as f:
        pass

create_account()

