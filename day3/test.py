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
# a="asfasdgagqw3re"
# b = Counter(a)
# print(b)
# print(b.items())
# for i,h in b.items():
#     print(i,h)


#有序字典
# import  collections
# a = collections.OrderedDict()
# a['a']='a'
# a['b']='b'
# a['c']='c'
#
# a.update({'a':'aa','d':'dd'})
# print(a)


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

print("\033[5;31;40mabc\033[0m")