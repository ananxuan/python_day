#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
from chengfa import chengfa
from jiafa import jiafa


def calculate(o):

    # 先进行乘除
    if re.findall('[*/]+',o):
        # 存在[0-9]-12.3[*/]-36.12[-+]
        # # l1 = re.findall('^-*\d+\.?\d*/-[^+-]+|^-*\d+\.?\d*\*-[^+-]+|\d+\.?\d*/-[^+-]+|\d+\.?\d*\*-[^+-]+|^-*[^+-]+|[^+-]+',o)
        # ^-*\d+\.?\d*[*/]-[^+-]+   行首为负 小数或整数 乘或除 负 其他任何非[+]字符
        o_temp = o
        o = o.replace("*-","AA")
        o = o.replace("/-","BB")
        # l1 = re.findall('^-*\d+\.?\d*[*/]-[^+]+|\d+\.?\d*[*/]-[^+]+|^-*[^+-]+|[^+-]+',o)
        l1 = re.findall('^-?\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|^-*[^+-]+|[^+-]+',o)
        print(l1)
        n = 0
        o = o_temp
        for i in l1:
            i = i.replace("AA","*-")
            i = i.replace("BB","/-")
            if re.findall('[*/]',i):
                l1[n] = chengfa(i)
                o = o.replace(i,l1[n],1).strip()
            n = n + 1
    if re.findall('[+-]+',o):
            o = jiafa(o)
            return o
    return o