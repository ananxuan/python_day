#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
from chengfa import chengfa
from jiafa import jiafa
def kuohao(o):
    if re.findall('[*/]+',o):
        # l1 = re.findall('[\d\s*/\.]+[^+-]',o)   #分离乘除和加减
        # l1 = re.findall('^-*[^+-]+|[^+-]+',o)   #分离乘除和加减
        # l1 = re.findall('.*/-[^-+]+|.*\*-[^-+]+|^-*[^+-]+|[^+-]+',o)   #分离乘除和加减
        # l1 = re.findall('\d+/-[^-+]+|\d+\*-[^-+]+|.*/-[^-+]+|.*\*-[^-+]+|^-*[^+-]+|[^+-]+',o)   #分离乘除和加减
        l1 = re.findall('^-*\d+\.?\d*/-[^+-]+|^-*\d+\.?\d*\*-[^+-]+|\d+\.?\d*/-[^+-]+|\d+\.?\d*\*-[^+-]+|^-*[^+-]+|[^+-]+',o)
        # l2 = re.findall('[+-]',o)    #记录加号和减号
        # print l1
        # print l2
        n = 0
        # m = 0
        # j = ['']
        for i in l1:
            if re.findall('[*/]',i):
                # print i
                l1[n] = chengfa(i)
                # m = m  + 1
                o = o.replace(i,l1[n],1).strip()
                # print type(o)
                # print "*/:",o

            n = n + 1
        # return o

        # print l1
        # print l2
        # print n," ",m
#         print o
#         print type(o)
#         print o
    if re.findall('[+-]+',o):
        # if re.findall('^-',o):
        #     print o
        #     return o
        # else:
        #     print 0
        #     print "kuohao:+-:",o
            o = jiafa(o)
            # print "+-:",o
            return o
    # else:
    #     print o
    return o
    # kuohao(o)
#
# print kuohao("5.0 + 5 * 22 / 9 - 8 + 9 + 2+ 1+9*7")
# print type(kuohao("5 *6/18.0"))
# print kuohao("-40/-5+9")
# print kuohao("1-2*-1388337.04762+12.0/10.0")
# print kuohao("40.1/-5+5*-4")
