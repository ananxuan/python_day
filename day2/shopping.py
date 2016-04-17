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
LIST_PRODUCT_COPY = []
LIST_CART = []
IS_LOGIN = False
AUTH_FILE = 'user.txt'
AUTH_TYPE = 'file'
PAY_TOTAL_MONEY = 0

def login():

    return True
    pass


def helpme2():
    print("""
        pay     确认订单，进入付款！
        modify  修改购物车
        quit    返回购物商城继续购物
        """
    )


def update_product_file():
    with open('product.txt','w',encoding='utf-8') as f:
        m = 0
        # print("update_product_file:",LIST_PRODUCT)
        n = len(LIST_PRODUCT)
        for i in LIST_PRODUCT:
            str2 = "%s||%s||%s||%s"%(i["id"],i["name"],i["price"],i["count"])
            f.write(str2)
            if m < n-1:
                f.write("\n")
            m += 1


def charge(name,pay_total_money):
    is_auth = False
    is_charge = False
    # print("charge:name=",name)
    with open(AUTH_FILE,'r') as f:
        content = f.readlines()

    with open(AUTH_FILE,'w') as f:
        card_error_num = 0
        CARD_LOGIN_FLAG = False
        cash = 0
        while card_error_num < 3:
            card_passwd = input("请输入银行卡密码> ").strip()
            m = 0
            for i in content:
                i = i.strip().split("||")
                # print(i)
                if name == i[0] and card_passwd == i[3]:
                    cash = round(float(i[4]),2)
                    CARD_LOGIN_FLAG = True
                    break
                m += 1
            if CARD_LOGIN_FLAG == True:
                if cash >= pay_total_money:
                    # print(i)
                    temp_cash = round(float(i[4]),2)
                    # print(temp_cash)
                    temp_cash -= pay_total_money
                    # print(temp_cash)
                    i[4] = str(round(temp_cash,2))
                    # print(i[4])
                    str1 = "||".join(i)
                    content[m] = str1 + "\n"
                    # print(content[m])
                    # print(content)
                    is_charge = True
                    update_product_file()
                    break
                else:
                    is_charge = False
                    print("余额不足！")
                    break
            else:
                is_charge = False
                card_error_num +=1
                print("银行卡密码错误！")

        if is_charge == True:
            n = len(content)
            m = 0
            for i in content:
                # print(i)
                if m == n -1:
                    i = i.strip()
                f.write(i)
                m += 1

    return  is_charge


def helpme3():
    print(
        """
        id      输入要修改的商品id
        ok      确认修改
        """
    )

def modify():
    while True:
        helpme3()
        print_cart()
        modify_input = input("请输入要修改的商品id> ").strip()
        if modify_input.isdigit():
            m_p_id = int(modify_input)
            m = 0
            for i in LIST_CART:
                if i[0] == m_p_id:
                    while True:
                        m_p_c = int(LIST_PRODUCT[m_p_id]["count"]) + LIST_CART[m][2]
                        print("%s库存%d件"%(LIST_PRODUCT[m_p_id]["name"],m_p_c))
                        modify_count_input = input("请输入修改后的件数> ").strip()
                        if modify_count_input.isdigit():
                            m_p_count = int(modify_count_input)
                            if m_p_count <= m_p_c:
                                LIST_CART[m][2] = m_p_count
                                # auto_update_product(m_p_id,m_p_count)
                                LIST_PRODUCT[m_p_id]["count"] = str(m_p_c - m_p_count)
                                break

                            else:
                                print("库存不够啊！")
                        else:
                            print("输入错误！")
                    break

            # return True
        elif "ok" == modify_input:
            return True
        else:
            print("输入错误！")



def pay():
    is_pay = False
    IS_LOGIN = False
    global PAY_TOTAL_MONEY
    while True:
        print("您购买的宝贝如下：")
        print_cart()
        helpme2()
        print("请支付\n")
        pay_input = input("请输入> ").strip()
        name = ""
        if "pay" == pay_input:
            pay_login_num = 0
            if IS_LOGIN == False:
                while pay_login_num < 3:
                    name = input("输入你的账户:> ").strip()
                    passwd = input("输入的密码:> ").strip()
                    auth_url = "%s@%s@%s@%s"%(name,passwd,AUTH_FILE,AUTH_TYPE)
                    if warehouse.auth(auth_url):
                        IS_LOGIN = True
                        break
                    else:
                        IS_LOGIN = False
                        print("not auth")
                    pay_login_num += 1
            if IS_LOGIN == True:
                if charge(name,PAY_TOTAL_MONEY):
                    is_pay = True
                    global  LIST_CART
                    LIST_CART = []
                    print("支持成功！")
                    break
                else:
                    is_pay = False
                    print("扣款失败！")
            else:
                is_pay = False
        elif "modify" == pay_input:
            if modify():
                pass

        elif "quit" == pay_input:
            is_pay = False
            break


    return  is_pay


def product_list():
    global  LIST_PRODUCT
    with open('product.txt','r',encoding='utf-8') as f:
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
    global  LIST_PRODUCT
    LIST_PRODUCT[pid]["count"] = str(int(LIST_PRODUCT[pid]["count"]) - pcount)


def print_cart():
    a = prettytable.PrettyTable(["id","宝贝","购买数量","总金额"])
    c = 0
    global  PAY_TOTAL_MONEY
    PAY_TOTAL_MONEY = 0
    for i in LIST_CART:
        # print(i)
        p = round(i[3]*i[2],2)
        a.add_row([i[0],i[1],i[2],p])
        c += i[2]
        PAY_TOTAL_MONEY += p
    a.add_row(["","总量",c,PAY_TOTAL_MONEY])
    print(a)
    # return TOTAL_MONEY



def buy():
    global  LIST_PRODUCT
    global LIST_CART
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
            # print(LIST_CART)
            if len(LIST_CART) >0:
                if pay():
                    return True
                else:
                    return False
            else:
                print("购物车位空，不用结算啊！")
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

    if product_list():
        pass
    else:
        return False
    while True:
        if buy():
            pass
        else:
            pass


def main():
    if shop():
        pass
    else:
        print("出现不确定错误，程序退出")
        exit()


if __name__ == '__main__':
    main()
