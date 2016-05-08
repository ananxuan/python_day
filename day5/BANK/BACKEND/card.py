#!/usr/bin/env python3
__author__ = 'DSOWASP'

import sys
sys.path.append("..")



import random
import time
import json

SESSION_LIST = set({})
DB_CARD_ACOUNT_FILE = '../../DB/card_account'


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
    with open(DB_CARD_ACOUNT_FILE,'r') as f:
        pass


class card:
    def __init__(self):
        pass