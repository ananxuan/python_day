#!/usr/bin/env python3
__author__ = 'DSOWASP'

# 设置默认的level为DEBUG
# 设置log的格式
#
# import logging
#
# logging.basicConfig(
#      level=logging.DEBUG,
#      format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
#  )
#
# print("abc")
# logging.info("def")

# print("\033[32;2m哈哈\033")
# a={"name":"abc","pass":"def",}
# print(a.get("file"))

# a={"name":1,"count":2}
# print(list(a.keys()))
# a={}
# with open("a.txt","r") as f:
#     for i in f.readlines():
#         i = i.strip().split("|")
#         a[i[0]]={"pwd":i[1],"登录次数":i[2]}
# print(a)

# a = float("1.9")
# # b = a*3
# print(3*a)
# b ="ok"
# c = "haha"
# a = "%s@%s"%(b,c)
# print(a)
# with open("user.txt",'r+') as f:
#     g =f.readlines()
#     f.seek(0)
#     m = 0
#     for i in g:
#         i = i.strip().split("||")
#         if i[0] == "owasp":
#             temp = float(i[4])
#             temp -= 100.99
#             i[4] = str(temp)
#             str1 = "||".join(i)
#             g[m] = str1 + "\n"
#             break
#         m += 1
#     for i in g:
#         f.write(i)
# content = ['||##username##password##card-id##card-passwd##card-money\n', 'owasp||123456||10133678287||654321||9994.3\n', 'ds||123456||10133678288||654321||10000.00']
# with open("user.txt","w") as f:
#     for i in content:
#         f.write(i)
# a=[1,"book",30]
# c=[2,"pc",30]
# b=[3,"ll",31]
# import prettytable
# p = prettytable.PrettyTable(["id","name","count"])
# p.add_row(a)
# p.add_row(b)
# p.add_row(c)
# print(p)
# if "10.1".isdecimal():
#     print("ok")


# with open('a.txt','a',encoding='utf-8') as f:
#     f.write("新增的")
# with open('a.txt','r') as g:
#     L = g.readlines()
#     L[2]="change\n"
#
#
# print(L)
# L = ["sfafa\n","sfafg\n","sfsafag\n"]
# f = open("a.txt",'w',encoding='utf-8')
# f.writelines(L)
# f.close()
# import collections
# collections.namedtuple()

# L = ['faf','fhhh','tttt']
# i = ['ffff']
# M = []
# for i in L:
#     M.append(i)
#
# print(M)

'''
用户信息
locked.txt
tenglan
judy
king

login.txt
jack 123456
bob 123
dawang 789
'''

# login_count = 0   #定义登陆次数（初始值为0）
# user = input("请输入用户名：")
# if len(user) == 0: #用户名不能为空
#     print("用户名不能为空，请重新输入")
# while login_count <3:    #限定登陆次数小于3
#     is_login = False
#     with open("locked.txt","r") as locked_file:   #使用with可避免忘记打f.close()
#         for line in locked_file.readlines():  # 循环遍历每一行
#             if user == line.strip():      #去除换行符
#                 print("用户%s已被锁定"%user)
#                 continue         #跳过后续代码, 继续进行循环
#     pwd=input("请输入密码：")
#     with open("login.txt", 'r') as login_file:
#       for line in login_file.readlines():     #循环遍历每一行
#         username, passward = line.strip().split()   #去除换行符以空格分割
#         if username == user and passward == pwd:
#             # print("success!")
#             # print("欢迎%s用户成功登录系统" % username)
#             is_login = True
#             break
#             #跳过后续代码, 退出当前循环
#     if is_login == True:
#         print("欢迎登陆")
#         break
#     else:
#         print("您的用户名和密码有误，请重新输入！")
#         login_count += 1                #计数（每登陆一次+1）
#         # break
#         #跳过后续代码, 退出当前循环
# if login_count >=3:
#         print("您的用户已被锁定")
#         with open("locked.txt", 'a') as locked:
#             locked.write("\n"+user)       #密码错误三次写进黑名单
#
def bb(x):
    return x+1
a = map(bb,[1,2,3,4])
print(a)
print(a.__doc__)
for i in a:
    print(i)