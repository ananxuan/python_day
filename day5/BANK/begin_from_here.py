from ATM import atm
from FRONT.front import create_account


def help_begin():
    """

    :return: 返回用户选择
    """
    print("\033[1;32;m1    登录信用卡中心")
    print("2    登录购物商城")
    print("3    退出\033[0m")
    while True:
        choice = input("请输入您的操作> ").strip()
        if choice in ("1","2","3"):
            return choice
        else:
            print("输入错误！")


def exit_this():
    exit()


def begin():
    """

    :return:
    """
    print("欢迎来到模拟ATM和购物商城！")
    print("这里已经创建yi一个模拟账户：")
    print("\033[1;31m账户1：5213464368221768,密码:J12%^sf1234\033[0m")
    fun_dic = {"1":atm.login,"3":exit_this}
    # if create_account() != True:
    #     print("注册账户失败！")
    #     exit()
    while True:
        fun = help_begin()
        fun_dic[fun]()


if __name__ == '__main__':
    #
    begin()
    pass
