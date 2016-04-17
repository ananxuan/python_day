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
if "10.1".isdecimal():
    print("ok")