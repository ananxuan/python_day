#!/usr/bin/env python3
__author__ = 'DSOWASP'

# 商品属性
# (id,name,price,count):(商品id,商品名字，商品价格，商品数量)

# 用户属性
# (username,passwd,card-id,acrd-passwd,money):(用户名，密码，银行卡id，银行卡密码，银行卡余额)

# 购物登录认证
# 通过用户名和密码认证
import logging
import prettytable

# 设置默认的level为DEBUG
 # 设置log的格式
logging.basicConfig(
     level=logging.DEBUG,
     format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
 )

LIST_PRODUCT_MOD = ['id','name','price','count']
LIST_PRODUCT = []

def login():

    return True
    pass


def pay():
    pass


def product():
    with open('product.txt','r+',encoding='utf-8') as f:
        for i in f.readlines():
            i = dict(zip(LIST_PRODUCT_MOD,i.strip().split("||")))
            LIST_PRODUCT.append(i)

        m = 0
        a = prettytable.PrettyTable(['id','name','price','count'])
        a.align["name"] = "l"
        for i in LIST_PRODUCT:
            a.add_row([m,i["name"],i["price"],i["count"]])
            # print("%d    商品:%s,   价格:%s,  数量:%s"%(m,i["name"],i["price"],i["count"]))
            m += 1
        print(a)
        # print(LIST_PRODUCT)
    pass


def helpme():
    print("okok")
    print("1、use vcs - update，2、use vcs -commit-commit&push")
    return True
    pass


def shop():
    print("欢迎来到DS购物商城！".center(30,'#'))
    # while True:
    if helpme():
        pass
    if product():
        pass
    pass


if __name__ == '__main__':
    shop()