#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
from chengfa import chengfa
from jiafa import jiafa
from special import special
from equl_tihuan import equl_tihuan


def calculate(o):

    # 进行等价替换
    o = equl_tihuan(o)

    # 先算特殊算术
    o_temp = o
    # print(o)
    o = o.replace("**","C")
    o = o.replace("//","D")
    # o = o.replace("%","E")
    print(o)
    if re.findall('C|D|%',o):
        print("ok")
        l1 = re.findall('(\d+\.?\d*)(C|D|%)(-|\+)?([^+*/-]+)',o)
        m = 0
        # 拼接元祖
        for i in l1:
            i = "".join(i)
            l1[m] = i
            m += 1
        o = o_temp
        n = 0
        print(l1)
        for i in l1:
            # i = i.replace("C",)
            l1[n] = special(i)
            i = i.replace("C","**")
            i = i.replace("D","//")
            print("i:",i)
            print(l1[n])
            print("o:",o)
            o = o.replace(i,l1[n],1).strip()
            print(o)
            n += 1

    # 进行乘除
    if re.findall('[*/]',o):
        # 保留最原始的 o 值
        o_temp = o
        o = o.replace("*-","AA")
        o = o.replace("/-","BB")
        # l1 = re.findall('^-*\d+\.?\d*[*/]-[^+]+|\d+\.?\d*[*/]-[^+]+|^-*[^+-]+|[^+-]+',o)
        # l1 = re.findall('^-?\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|^-*[^+-]+|[^+-]+',o)
        # 取乘除表达式，包含*  /   *-   /-   的式子
        l1 = re.findall(r'(^-)?(\d+\.?\d*)(AA|BB|\*|/)([^ +-]+)',o)
        m = 0
        # 拼接元祖
        for i in l1:
            i = "".join(i)
            l1[m] = i
            m += 1
        n = 0
        o = o_temp

        # 计算每一个表达式
        for i in l1:
            i = i.replace("AA","*-")
            i = i.replace("BB","/-")
            if re.findall('[*/]',i):
                l1[n] = chengfa(i)
                o = o.replace(i,l1[n],1).strip()
            n = n + 1
    # 计算加减法
    if re.findall('[+-]',o):
        if re.search('e-',o) == None:
            o = jiafa(o)
            return o
    return o