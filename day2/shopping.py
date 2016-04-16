#!/usr/bin/env python3
__author__ = 'DSOWASP'

# 商品属性
# (id,name,price,count):(商品id,商品名字，商品价格，商品数量)

# 用户属性
# (username,passwd,card-id,acrd-passwd,money):(用户名，密码，银行卡id，银行卡密码，银行卡余额)

# 购物登录认证
# 通过用户名和密码认证
import warehouse
import prettytable



LIST_PRODUCT_MOD = ['id','name','price','count']
LIST_PRODUCT = []
LIST_CART = []
IS_LOGIN = False
TOTAL_MONEY = 0
AUTH_FILE = 'user.txt'
AUTH_TYPE = 'file'

def login():

    return True
    pass


def helpme2():
    print("""
        pay     确认订单，进入付款！
        modify  修改购物车
        quit    退出购物商城
        """
    )


def pay():
    print("您购买的宝贝如下：")
    helpme2()
    print_cart()
    print("请支付\n")
    if IS_LOGIN == False:
        while True:
            name = input("输入你的账户:> ").strip()
            passwd = input("输入的密码:> ").strip()
            auth_url = "%s@%s@%s@%s"%(name,passwd,AUTH_FILE,AUTH_TYPE)
            if warehouse.auth(auth_url):
                print("ok")
            else:
                print("not auth")
        pass

    return  True


def product_list():
    with open('product.txt','r+',encoding='utf-8') as f:
        for i in f.readlines():
            i = dict(zip(LIST_PRODUCT_MOD,i.strip().split("||")))
            LIST_PRODUCT.append(i)
        m = 0
        a = prettytable.PrettyTable(['id','name','price','count'])
        a.align["name"] = "l"
        for i in LIST_PRODUCT:
            a.add_row([m,i["name"],i["price"],i["count"]])
            m += 1
        print(a)
    return  True


def auto_update_product(pid,pcount):
        LIST_PRODUCT[pid]["count"] = str(int(LIST_PRODUCT[pid]["count"]) - pcount)


def print_cart():
    a = prettytable.PrettyTable(["宝贝","购买数量","总金额"])
    c = 0
    TOTAL_MONEY = 0
    for i in LIST_CART:
        # print(i)
        p = round(i[3]*i[2],2)
        a.add_row([i[1],i[2],p])
        c += i[2]
        TOTAL_MONEY += p
    a.add_row(["总量",c,TOTAL_MONEY])
    print(a)



def buy():
    while True:
        helpme1()
        pid = input("请输入> ").strip()
        if pid.isdigit():
            pid = int(pid)
            if len(LIST_PRODUCT) > pid:
                p = LIST_PRODUCT[pid]
                p_name = p["name"]
                p_price = float(p["price"])
                p_count = int(p["count"])
                print("您选购的%s,单价%s,仓库剩余%s"%(p["name"],p["price"],p["count"]))
                while True:
                    pcount = input("请输入要购买的数量> ").strip()
                    if pcount.isdigit():
                        pcount = int(pcount)
                        if pcount <= p_count:
                            print("您已选购%s,%d件，总额%f"%(p_name,pcount,pcount*p_price))
                            while True:
                                is_ok = input("你确定加入购物车吗？[yes/no]> ").strip()
                                if "YES" == is_ok.upper():
                                    m = 0
                                    flag1 = 0
                                    for i in LIST_CART:
                                        if i[0] == pid:
                                            LIST_CART[m][2] += pcount
                                            flag1 = 1
                                            break
                                        m += 1
                                    if flag1 == 0:
                                        LIST_CART.append([pid,p_name,pcount,p_price])
                                    auto_update_product(pid,pcount)
                                    break
                                elif "NO" == is_ok.upper():
                                    break
                                else:
                                    print("请输入[yes/no]> ")
                            break
                        else:
                            print("对不起，仓库木有这么多库存！")
                    else:
                        print("购买数量输入有误,请输入数字")
            else:
                print("输入的id超过范围！")
        elif "check" == pid:
            if pay():
                return True
            else:
                pass
            pass
        elif "l" == pid:
            print_cart()
        elif "quit" == pid:
            print("欢迎再次光临！")
            exit()
        else:
            print("输入有误！，请重新输入")



def helpme1():
    print("""
    id          按商品id选购商品
    check       结算
    l           查看购物车
    quit        退出购物
    """)



def shop():
    print("欢迎来到DS购物商城！".center(40,'#'))
    # while True:
    if product_list():
        pass
    else:
        return False
    if buy():
        pass
    else:
        pass
    # print(LIST_PRODUCT)


if __name__ == '__main__':
    if shop():
        pass
    else:
        print("出现不确定错误，程序退出")
        exit()
