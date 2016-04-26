#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
from tihuan import tihuan
float()
def jiafa(k):
    k = k.strip()
    k = tihuan(k)
    w1 = re.findall('^-*\d+\.?\d*|\d+\.?\d*',k)
    w2 = re.findall('[-+]+',k)
    if re.match('^-',k):
        w2.pop(0)
    n = 1
    z = float(w1[0])
    # print "w1=",w1
    # print "w2=",w2
    for i in w2:
        # print "Setp %d,i=%s" %(n,i)
        if i == "+":
            # z = float(int(w1[n-1])) + float(int(w1[n]))
            z = float(w1[n-1]) + float(w1[n])
            #z = ("%.10f" %z)
            n = n + 1
            w1[n-1] = z
            # print "z=",z
        elif i == "-":
            z = float(w1[n-1]) - float(w1[n])
            #z = ("%.10f" %z)

            n = n + 1
            w1[n-1] = z
            # print z
        # print "z=",z
    return str(z).strip()

# print "jiafa=",jiafa("55 + 3  - 2 + 34 -3")
# print "jiafa=",jiafa("5 +12.2222222222- 8 + 9 + 2+ 1+63.0")

# print jiafa("-8")