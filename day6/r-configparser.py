#!/usr/bin/env python3
__author__ = 'DSOWASP'
import configparser
cp = configparser.ConfigParser()
with open("cp.cnf","r") as f:
    # print(cp.sections())
    cp.read_file(f)
    # print(cp.get("mysqld","user"))
    # cp.update()
    for key in cp.keys():
        print("[%s]"%key)
        for keys,values in cp[key].items():
            print("%s = %s"%(keys,values))
print(cp.sections())
print(cp.defaults())
print(cp.options("mysqld"))
# print(cp.keys())
cp.remove_option("mysqld","user")
cp.remove_section("client")
print(cp.get("mysqld","user"))
# print(cp.getint("mysqld","user"))  # 把值从字符串转换为int
print(cp.has_option("mysqld","user"))
print(cp.has_section("abd"))
print("************************")
for key in cp.keys():
    print("[%s]"%key)
    for keys,values in cp[key].items():
        print("%s = %s"%(keys,values))