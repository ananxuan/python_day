#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re

def equl_tihuan(g):
    g = g.strip()
    #  替换空格、--、++、-+、+-、/+、*+为去空格、+、+、-、-、/、*,还有去掉行首的 + 号
    while True:
        g = g.replace(" ","")
        if g.startswith("+"):
            g = g[1:]
        if re.findall('\+-\d',g):
            # print("kka")
            b = re.findall('\+-\d',g)
            n = 0
            # print(b)
            for i in b:
                # print(i)
                i = i.replace("+-","+0-")
                # print(i)
                # print(b[0])
                g = g.replace(b[n],i,)

        if re.findall('\+-|--|\+\+|-\+|\*\+|/\+|\*\*\+|//\+|%\+',g):
            g = re.sub('\+-','-',g)
            g = re.sub('--','+',g)
            g = re.sub('\+\+','+',g)
            g = re.sub('-\+','-',g)
            g = re.sub('\*\+','*',g)
            g = re.sub('/\+',"/",g)
            g = re.sub('\*\*\+',"**",g)
            g = re.sub('//\+',"//",g)
            g = re.sub('%\+',"%",g)
        else:
            break
    return g