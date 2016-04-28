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