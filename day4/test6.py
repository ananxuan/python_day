#!/usr/bin/env python

# -*- coding: utf-8 -*-

'''

__title__ = ''

__author__ = 'xuanxuan'

__mtime__ = ''

# code is far away from bugs with the god animal protecting

I love animals. They taste delicious.

'''

import re
def deal_minus(expm):
    s4 = re.findall('\d+[*-|/-|+-|--]\d+',str(expm))
    print(s4)
    # for i in s4:
    #     if '*-' in i:
    #         res = -(i[0] * i[2])
    #     elif '/-' in i:
    #         res = -(i[0] / i[2])
    #     elif '+-' in i:
    #         res = i[0] - i[2]
    #     else:
    #         res = i[0] + i[2]
    # new_exp =str(s4).replace('i', 'res')
    # print('result', new_exp)
    # return new_exp

# deal_minus(expm)



def multi(exp):#expression
    # print(exp)
    listm = re.findall('^-*\d+\.?\d*[*/]-[^+]+|\d+\.?\d*[*/]-[^+]+|^-*[^+-]+|[^+-]+', exp)
    # mullist = []
    # print(listm)
    for item in listm:

        items = item.strip()
        # print(items)
        if "*" in items or "/" in items:
            # print(items)
            # mullist.append(items)
            # for items in mullist:
            numlist = re.split("[*/]", items)
            mullist = re.findall("[*/]",items)
            print(numlist)
            print(mullist)
                # res = None
                # for i in numlist:




def calc(exp):
    expm = re.findall('\([^()]*\)', exp)
    resutmultilist = []
    for item in expm:
        expmk = item.strip("()")
        expms = expmk.strip()
        res1 = [multi(expms)]
        resutmultilist.extend(res1)
    # print(resutmultilist)


if __name__ =="__main__":
    exp = "1-2*((60-30)+(-40/5)*(9-2*5/3 + 7/3*99/4*2998 + 10*568/14)-(-4*3)/(16-3*2))"
    result = calc(exp)
