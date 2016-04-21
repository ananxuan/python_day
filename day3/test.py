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
# # a.move_to_end()
# a.update({'a':'aa','d':'dd'})
# print(a)
# a.move_to_end('a')
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
# print("sizeof:",a.__sizeof__())
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

#深浅拷贝
#字符串和数字深浅拷贝都是用内存里的同一个地址
import  copy
# a = {
#     'class':'python1',
#     'students':{
#         'a1':0
#     }
# }
#
# b = []
# for i in range(3):
#
#     a['students']['a1']=i
#     b.append(a)
# print(b)

# c = copy.deepcopy(a)
# d = copy()

#发送邮件
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
# def  mail():
#     try:
#         msg = MIMEText('测试邮件','plain','utf-8')
#         msg['Form'] = formataddr(['test1','abc@qq.com'])
#         msg['To'] = formataddr(['test2','493513100@qq.com'])
#         msg['Subject'] = '安安'
#
#         server = smtplib.SMTP('smtp.126.com',25)
#         server.login('liujin2228319@126.com','lj0202game126')
#         server.sendmail('liujin2228319@126.com',['493513100@qq.com',],msg.as_string())
#         server.quit()
#     except(Exception):
#         print("error")
# mail()


#字符串格式化
# fomat(self,*args,**kwargs)
# a = '{0} is {1}'
# res = a.format('alex','sb')
# print(res)
# b = ['ds','ds']
# res = a.format(*b)
# print(res)
# a = '{name} is {what}'
# b = {'name':'lj','what':'ds'}
# res = a.format(**b)
# print(res)

# chr(60)
# ord('A')
# a = [0,1,2,3,4,5,6,7,8,9]
# for i,item in enumerate(a,10):
#     print(i,item)


#map
# a = (1,2,3,4,5)
# def b(c):
#     c *= 2
#     return c
# res1 = map(b,a)
# for i in res1:
#     print(i)
# filter()


# a = range(100)
# b = sum(a)
# print(b)
# #当前环境的所有东西
# print(vars())
# print(vars().keys())
# print(dir())

#fread(1)是读一个字符。而不是一个字节。
# with open('info.txt','r',encoding='utf-8')  as f:
#     for i in f.read():
#         print(f.tell())
#         print(i)
with open('info.txt','r',encoding='utf-8') as f:
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    # print(f.read(1))
    # print(f.tell())