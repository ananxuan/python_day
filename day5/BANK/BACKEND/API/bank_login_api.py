#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
sys.path.append("..")
from BACKEND import card

def bank_login_api(card_id,card_passwd):
    print("正在调用bank_login_api")
    session_id, login_flag = card.login(card_id,card_passwd)

    return True