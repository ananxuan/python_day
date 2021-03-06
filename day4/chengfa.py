#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
from equl_tihuan import equl_tihuan

import re
def chengfa(k):
    k = k.strip()
    k = equl_tihuan(k)
    w1 = re.findall('-*\d+\.?\d*',k)
    w2 = re.findall('[*/]+',k)
    n = 1
    z = float(w1[0])
    for i in w2:
        if i == "*":
            z = float(w1[n-1]) * float(w1[n])
            n = n + 1
            w1[n-1] = z
        elif i == "/":
            try:
                z = float(w1[n-1]) / float(w1[n])
                n = n + 1
                w1[n-1] = z
            except(ZeroDivisionError):
                print("除数不能为0")
                exit()
    return str(z).strip()

if __name__ == '__main__':
    print('此py不能直接运行,请运行计算器.py')