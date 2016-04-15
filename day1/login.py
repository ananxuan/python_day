#!/usr/bin/env python3
__author__ = 'DSOWASP'

"""
userlist.txt
python 123
ds 123456
lj 123
yy 123
abc 321
ok ok
"""
"""
locklist.txt
python
ds
"""

error_count = 0             # 认证错误次数，包括用户名错误和用户名正确但是密码错误
error_users = []            # 用于存放用户名存在，但是密码错误的列表，存放数据格式如：
# [{'name':'ds','count':1},{'name':owasp','count':2}],当某个用户的count为3时，就把这个
# 用户加到locklist.txt文件中， 由于error_users保存在内存中，因此只有在当前会话有效

flag1 = 0    # 0表示用户名不存在，1表示用户名密码正确，2表示用户名正确，但是密码错误
flag2 = 0    # 0表示当前用户不存在与error_users中,1当前用户存在于error_users中或error为非空
while True:
    import time
    username = input("用户名:").strip()
    password = input("密码:").strip()
    if username == "EXIT":                 # 为了能正确退出程序而设置的
        break
    flag1 = 0
    with open('locklist.txt','r') as f_lock:   # 验证此用户是否被锁定
        u1 = f_lock.read().split("\n")
        if u1.count(username) != 0:
            print("此账户已被锁定！请选择其他账户登录")
            time.sleep(1)
            continue
    with open('userlist.txt','r') as f_user:         # 验证用户名和密码
        for line in f_user:
            user = line.split()[0]
            passwd = line.split()[1]
            if username == user:
                if password == passwd:                  # 用户和密码都正确，设置flag=1
                    print("Welcome to My Python Page!!!")
                    flag1 = 1
                    break
                elif flag2 == 1:                       # 密码不对，且当前error_users为非空
                    flag1 = 2                           # 用户名正确，但是密码不对
                    for i in error_users:              # 判断这个用户是否已存在于error_users中
                        # print("循环字典1",error_users)
                        if username == i.get("name"):  # 在error_users中找到了这个账户
                            # print("找到字典元素:",username,error_users)
                            flag2 = 1                  # 当前用户存在于error_users中
                            i["count"] = i.get("count") + 1          # 置当前用户的密码错误次数加1
                            if i.get("count") >= 3:                   # 如果错误次数等于3
                                        with open('locklist.txt','a') as f_lock:         # 就锁定这个账户
                                            f_lock.write("\n%s" % username)
                                            print("输入错误次数过多，%s账户已被锁定！请联系管理员！" %(username))
                            else:                     # 如果错误次数小于3，则打印提示信息
                                print("用户%s已输入错误密码%d次，此账户还剩%d次尝试机会" % (i.get("name") , i.get("count"),3 - i.get("count")))
                            break                     # 如果再error_users中找到了当前的用户，则退出error_users的循环
                        else:                         # 如果在error_users中没找到这个用户，则打印提示信息，并设置flag2=0
                            flag2 = 0
                if flag2 == 0:                        # 添加当前用户到error_users中。
                    flag1 = 2                         # 用户名和密码都不正确
                    # print("添加前字典情况",error_users)
                    error_users.append({'name':username,'count':1})
                    print("用户%s已输入错误密码1次，此账户还剩2次尝试机会" % (username))
                    # print("添加%s用户到字典"%username)
                    # print(error_users)
                    flag2 = 1                        # 设置flag2=1表示error_users为非空

    if flag1 == 1:                                   # flag1=1表示用户名密码正确，则退出
        break
    elif flag1 == 0:                                 # flag=0表示用户名不存在斌，error_count加1
        error_count += 1
        print("用户名不存在，请重新输入，还剩%d次尝试机会" %(3 - error_count))
    elif flag1 == 2:                                 # flag1=2表示用户名正确但是密码错误.error_count 加1
        error_count += 1
    if error_count >= 3:                             # 如果输错的此时大于等于3则打印提示信息，并sleep5秒，重置error_count
        print("输入错误次数超过3次，请5秒后重新输入")
        error_count = 0
        time.sleep(5)