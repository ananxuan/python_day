#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
from equl_tihuan import equl_tihuan

float()
def jiafa(k):
    k = k.strip()
    k = equl_tihuan(k)
    w1 = re.findall('^-*\d+\.?\d*|\d+\.?\d*',k)
    w2 = re.findall('[-+]',k)
    if re.match('^-',k):
        w2.pop(0)
    n = 1

    z = float(w1[0])
    for i in w2:
        if i == "+":
            z += float(w1[n])
        elif i == "-":
            z -= float(w1[n])
        n += 1
    return str(z).strip()
if __name__ == '__main__':
    print('此py不能直接运行,请运行计算器.py')