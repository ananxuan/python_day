#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re
def tihuan(g):
    g = g.split()
    h = ''
    for i in g:
        h = h + i.strip()
    g = h
    # print "qukongge:", g
    if re.findall('\+-|--',g):
        g = re.sub('\+-','-',g,count=0)
        g = re.sub('--','+',g,count=0)
        g = tihuan(g)
        g = str(g).strip()
        # print "equal change:",g
    return g

# print tihuan("f +-sdfa d --+-g")