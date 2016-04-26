#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'

import re
from chengfa import chengfa
from jiafa import jiafa
from kuohao import kuohao
from tihuan import tihuan
#m = raw_input("input your :")
# m = "2 * 3 + (5 *6/(2+4* 4))/4 + (2+3 / 4+(3+2/5)+3)-3"
m = "1 - (-0.2) *(-60.9-30/4+( -40.6/-5.9)* (9 -2*5/3 +7.1 /3*99/4*2998 +10 * -56.8/14)) - (-4*3)/(16-3*2)"
r = m
#2、将算术转换为列表，每个列表一个字符
# l = re.findall('\S',m)
# print l
#2、取括号,第一个左括号后面是非括号+右括号，记录括号坐标。
# l = re.findall('[^(]+| \(\S+)]',m)
# l = re.findall('[^(]* | \([^()]*',m)
# l = re.findall('[^()]+',m)

# #乘除法
# def math2(k):
#     w = re.findall('\d+|[*/]',k)
#     n = 0
#     z = 1.0
#     for i in w:
#        if i == "*":z = z * float(w[n+1])
#        elif i == "/": z = z / float(w[n+1])
#        else:z = float(i)
#     return z
#加减法
# def math1(s):
#     e = re.findall('[\d\s]+[*/][\d\s]+',s)
#     for i in e:
#         i = math2(i)


def math(g):
    # y = g
    # print "before:",y
    #替换负号
    g = tihuan(g)
    # g = re.sub('')
    # print "tihuan:",g
    if re.findall('[()]+',g):
       # print "math-1:",g
       l = re.findall('[(][^()]+[)]',g)  #取所有最内部括号\
       # print "math-2:",l
       n = 0
       for i in l:
          # print "math-3:",i
          j = re.search('[^()]+',i).group()  #去括号
          # print "math-4:",j
          i = kuohao(j)
          # print "math-5:",i
          g = g.replace(l[n],i,1)
          n = n + 1
       print("del-kuohao:",g)

    elif re.findall('[+*-/]+',g):
        g = kuohao(g)
        # print "math-+*/:",g
        return g
    else:
        print(g)
        return g
    # print "after:",y
    return math(g)
# m = "9 -2*5/3 +7.1 /3*99/4*2998 +10 * -56.8/14"
# r = m
print ("The original input:",m)
m = math(m)
print("The result is:" ,m)

print("eval(r)=",eval(r))

