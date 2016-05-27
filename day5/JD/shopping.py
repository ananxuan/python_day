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



LIST_PRODUCT_MOD = ['id','name','price','count']            # 打印购物车prettytable头部信息
LIST_PRODUCT = []           # 库存
# LIST_PRODUCT_COPY = []
LIST_CART = []              # 购物车
IS_LOGIN = False           # 是否登录
AUTH_FILE = 'user.txt'      # 认证文件，存放商城用户名，密码，银行卡账户密码，余额
AUTH_TYPE = 'file'          # 认证类型
PAY_TOTAL_MONEY = 0             # 需要支付的金额


def helpme2():              # 帮助信息
    print("""
        pay     确认订单，进入付款！
        modify  修改购物车
        quit    返回购物商城继续购物
        """
    )


def update_product_file():          # 缺付款后更新仓库
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


def charge(name,pay_total_money):           # 付款
    # is_auth = False
    is_charge = False

    with open(AUTH_FILE,'r') as f:      # 获取用户信息（用户名、密码、银行卡信息）
        content = f.readlines()


    card_error_num = 0                  # 银行卡密码输错次数
    CARD_LOGIN_FLAG = False
    cash = 0
    while card_error_num < 3:           # 银行卡密码错误三次后重新登录
        card_passwd = input("请输入银行卡密码> ").strip()
        m = 0
        for i in content:
            i = i.strip().split("||")
            # print(i)
            if name == i[0] and card_passwd == i[3]:      # 用户名和密码匹配
                cash = round(float(i[4]),2)
                CARD_LOGIN_FLAG = True              # 标识银行卡密码正确
                break
            m += 1
        if CARD_LOGIN_FLAG == True:                 # 如果银行卡密码正确
            if cash >= pay_total_money:                 # 银行卡余可付款
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
                update_product_file()           # 确认付款后更新仓库文件
                break
            else:
                is_charge = False
                print("余额不足！")
                break
        else:
            is_charge = False
            card_error_num +=1
            print("银行卡密码错误！")

        if is_charge == True:           # 付款成功后更新银行卡余额
            n = len(content)
            m = 0
            with open(AUTH_FILE,'w') as f:          # 将更新后的信息写回文件
                for i in content:
                    # print(i)
                    if m == n -1:
                        i = i.strip()
                    f.write(i)
                    m += 1

    return  is_charge


def helpme3():      # 帮助信息
    print(
        """
        id      输入要修改的商品id
        ok      确认修改
        """
    )

def modify():           # 修改购物车
    while True:
        helpme3()
        print_cart()            # 打印购物车
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
                                LIST_PRODUCT[m_p_id]["count"] = str(m_p_c - m_p_count)      # 更新购物车列表
                                break

                            else:
                                print("库存不够啊！")
                        else:
                            print("输入错误！")
                    break

            # return True
        elif "ok" == modify_input:       # 确认购物车修改成功
            return True
        else:
            print("输入错误！")



def pay():                            # 付款
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
                if charge(name,PAY_TOTAL_MONEY):        # 进入银行卡进行扣款流程
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
        elif "modify" == pay_input:          # 修改购物车
            if modify():
                pass

        elif "quit" == pay_input:           # 退出支付，重新购物
            is_pay = False
            break


    return  is_pay


def product_list():             #初始化仓库库存到列表
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


def auto_update_product(pid,pcount):            # 更新库存列表
    global  LIST_PRODUCT
    LIST_PRODUCT[pid]["count"] = str(int(LIST_PRODUCT[pid]["count"]) - pcount)


def print_cart():                       # 打印购物车
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



def buy():                      # 购买商品
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
                                        LIST_CART.append([pid,p_name,pcount,p_price])    # 将宝贝加入购物车
                                    auto_update_product(pid,pcount)             # 更新库存列表
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
        elif "check" == pid:            # 结算
            # print(LIST_CART)
            if len(LIST_CART) >0:
                if pay():               # 进入结算流程
                    return True
                else:
                    return False
            else:
                print("购物车位空，不用结算啊！")
        elif "l" == pid:                # 打印购物车
            print_cart()
        elif "quit" == pid:
            print("欢迎再次光临！")
            exit()
        else:
            print("输入有误！，请重新输入")


def helpme1():           # 帮助信息
    print("""
    id          按商品id选购商品
    check       结算
    l           查看购物车
    quit        退出购物
    """)


def shop():             # 主函数
    print("欢迎来到DS购物商城！".center(40,'#'))

    if product_list():   # 打印商品列表，库存
        pass
    else:
        return False
    while True:             # 进入购物流程
        if buy():
            pass
        else:
            pass


def main():         # 主函数
    if shop():      # 进入商城
        pass
    else:
        print("出现不确定错误，程序退出")
        exit()


if __name__ == '__main__':
    main()
