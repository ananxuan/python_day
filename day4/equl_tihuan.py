#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'
import re

def equl_tihuan(g):
    # 可能由于输入错误，算子中会存在空格，这里是去掉算子中的空格
    g = g.replace(" ","")
    # 替换+-和--为+或-，用递归
    if re.findall('\+-|--',g):
        g = re.sub('\+-','-',g)
        g = re.sub('--','+',g)
        g = equl_tihuan(g)
        g = str(g).strip()
    # print("等价变换:",g)
    return g