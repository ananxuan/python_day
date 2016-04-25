# # a="00014#"
# # print(a.isdigit())
# # print(a.isnumeric())
# # print(a.isalnum())
#
# a = {"name":"a","count":3}
# print(type(a))
# b = a.keys()
# c = a.values()
# print(b)
# print(c)
# for i in b:
#     print(i)
# for i in c:
#     print(i)
# print(type(b))
# print(type(c))
# d = set(b)
# print(type(d))
# print(d)

# import os
# print(__file__)
# b = os.path.dirname(os.path.abspath(__file__))
# print(b)
# c = os.path.join(b,"info.txt")
# print(c)
# with open(c,'r') as f:
#     for i in f.readlines():
#         print(i)
# i = {"name":1,"sex":0}
# l = 0
# while l < 1:
#     a = []
#     a.append(i)
#     i = {"name":2,"sex":1}
#     a.append(i)
#     print(a)
#     l += 1


# from collections import Counter

def create_counter():
    a = "asfasdgagqw3re"
    b = Counter(a)
    print(b)
    print(b.items())
    for i,h in b.items():
        print(i,h)
# create_counter()


#有序字典,打印时值得顺序是不变的。
def crete_collections():
    import  collections
    a = collections.OrderedDict()
    a['a']='a'
    a['b']='b'
    a['c']='c'

    a.update({'a':'aa','d':'dd'})
    print(a)
# crete_collections()


#默认字典就是定义values的值是什么类型
# import  collections
# l = [1,2,3,4,5,6]
# a= collections.defaultdict(list)
# for i in l:
#     a['k1'].append(i)
# print(a)


#可命名元祖
# import collections
# MytupleClass = collections.namedtuple('mytuple',['x','y','z'])
# a = MytupleClass(11,22,33)
# print(a)
##  mytuple(x=11, y=22, z=33)

#队列,像是一个列表
# import  collections
# def c():
#     pass
# a = collections.deque()
# a.append({'b':1,'c':2})
# a.append({'e':1})
# a.append(1)
# a.appendleft(10)
# a.append(c)
# a.extend([111,'sfa',10])
# print(a)
# print(a.index(10))
# a.rotate(2)
# print(a)
# print(a.pop())
# print(a)
#
#
#
# b = []
# b.append({'b':1,'c':2})
# b.append({'e':1})
# b.append(1)
# b.extend([10,1,'sdf'])
# b.append(c)
# print(b)
# print(b.index(10))
# print(b.pop(0))
# print(b)
#
# import  collections
#
# a = dict([('name',1),('sex',0),('age',18)])
# for i in a.items():
#     print(i)
#
# b = collections.OrderedDict([('name',1),('sex',0),('age',18)])
# for i in b.items():
#     print(i)


# import json
# a = '{"name":"ds","other":{"count":1,"age":18}}'
# b = json.loads(a)
# print(b)


# a = ["name"]
# b = str(a[0:])
# print(b)

# a = {}
# a is dict

# import json
# inp_str = "[11,22,33,44]"
# inp_list = json.loads(inp_str)
# print(inp_list)
# for i in range(100):
#     i = str(i)
#     print("\033[%s;31;40mabc\033[0m"%i)



# a = "sdgsdgag"
# print(a.ljust(10))

#域名正则表达式
# import re
# def getUrlFromFile(fobj):
#     # regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.IGNORECASE)
#     regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.IGNORECASE)
#     urls = regex.findall(fobj)
#     # print urls
#     return urls
#
# def main(FilefilePath):
#     fobj = open(FilefilePath, 'r').read()
#     urllist = getUrlFromFile(fobj)
#     print(urllist)
#
# main("info.txt")

# a = {"name":"ds","age":18}
# a.get()
# print(a)
# a.pop("name")
# print(a)

# a = ["asdfsaf"]
# a.clear()
# print(a)

# print("\033[5;31;40mabc\033[0m")

def str_bytes():
    print(bin(ord("a")))
    print(bin(ord("\n")))
    print(bin(ord("刘")))
    for i in "刘":
        print(i,bytes(i,"gbk"))
        # i_byte =
    for i in "刘":
        print(i,bytes(i,"utf-8"))
        i_byte = bytes(i,"utf-8")
        for l in i_byte:
            print(l,bin(l))

# -*- coding:utf-8 -*-

# py 2.7
"""
s = "武沛齐"
for item in s:
    print(item,ord(item), bin(ord(item)))
# 问题？为什么2.7的for不以字符的形式循环
# 如果，字符，想要看字节，需要转换成字节
# 字符串 str ，字节 bytes[无用py3做过度]
# 1、for，默认字节循环
# 2、bytes类型形同虚设
"""
"""
s = "武沛齐"
for item in s:
    # print(item)# 汉字=》三字节》二进制
    print(item, bytes(item, 'utf-8'))
    item_bytes = bytes(item, 'utf-8')
    for j in item_bytes:
        print(j,bin(j))
"""
# py3
# 1、bytes，用来获取字符串的字节表示
# 2、for循环，字符循环

# s = "武沛齐"
# # 将字符串转换成字节
# s_bytes = bytes(s, 'utf-8')
# print(s_bytes)
# # 将字节转换成字符串
# new_str = str(s_bytes, 'utf-8')
# print(new_str)
with open("info.txt","r",encoding="utf-8") as f:
    for i in f.readline():
        print(i,end="")
        print(f.tell())
#
# ret = range(10)




# def foo():
#     print("abc")
#
# def before():
#     print("123")
#     temp()
#
# temp = foo
# foo = before
#
# foo()

# foo = before()