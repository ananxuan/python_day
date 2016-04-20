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
import  collections
def c():
    pass
a = collections.deque()
a.append({'b':1,'c':2})
a.append({'e':1})
a.append(1)
a.appendleft(10)
a.append(c)
a.extend([111,'sfa',10])
print(a)
print(a.index(10))
a.rotate(2)
print(a)
print(a.pop())
print(a)



b = []
b.append({'b':1,'c':2})
b.append({'e':1})
b.append(1)
b.extend([10,1,'sdf'])
b.append(c)
print(b)
print(b.index(10))
print(b.pop(0))
print(b)

