#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'

import re
def chengfa(k):
    k = k.strip()
    w1 = re.findall('-*\d+\.?\d*',k)
    w2 = re.findall('[*/]+',k)
    n = 1
    z = float(w1[0])
    # print "w1=",w1
    # print "w2=",w2
    for i in w2:
#        print "Setp %d,i=%s" %(n,i)
        if i == "*":
            # print float(w1[n-1])
            # print float(w1[n])
            z = float(w1[n-1]) * float(w1[n])
            #z = ("%.10f" %z)
            # print "***",z
            n = n + 1
            w1[n-1] = z
            # print "z=",z
        elif i == "/":
            # print float(w1[n-1])
            # print float(w1[n])
            z = float(w1[n-1]) / float(w1[n])
            #z = ("%.10f" %z)
            n = n + 1
            w1[n-1] = z
            # print z
#        print "z=",z
    return str(z).strip()

#print "math2=",math2("55 * 3 /2 * 34/3")
# print chengfa("5 *6/18.0")
# print chengfa("-6 / 5 *7")
# print chengfa("-40.1/-5")
# print chengfa("6.8813559322*175572.945238")