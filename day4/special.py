#!/usr/bin/env python3
__author__ = 'DSOWASP'
import re
from equl_tihuan import equl_tihuan
import copy
def special(str1):
    str1 = equl_tihuan(str1)
    w1 = re.findall('^-*\d+\.?\d*|\d+\.?\d*|-\d+\.?\d*',str1)
    w2 = re.findall('[CDEFG%]',str1)
    w2_temp = copy.copy(w2)
    # print(w1)
    # print(w2)
    # 找C（**）优先级最高
    n = len(w2)
    m = n
    w2.reverse()
    # w2_temp = copy.copy(w2)
    # print(w2_temp)
    z = float(w1[n])
    for i in w2:
        # print("i,n:",i,n)
        if i == 'C':
            # print(w1[n-1],w1[n])
            z = float(w1[n-1]) ** float(w1[n])
            w1.pop(n)
            # print("w2:",w2)
            # print(w2_temp)
            w2_temp.pop(n-1)
            # print("w2:",w2)
            w1[n-1] = z
            # print(w1)
        n -= 1

    # print(w1)
    w2 = w2_temp
    # print(w2)
    n = 0
    z = float(w1[0])
    for i in w2:
        try:
            if i == "D":
                z = z // float(w1[n+1])
            elif i == "%":
                z = z % float(w1[n+1])
            elif i == "E":
                z = z ** float("-"+w1[n+1])
            elif i == "F":
                z = z // float("-"+w1[n+1])
            elif i == "G":
                z = z % float("-"+w1[n+1])
        except(ZeroDivisionError):
            print("%s %s %s is error,0不能做除数！"%(str(z),i,str(float(w1[n+1]))))
            exit()
        n += 1
    # print(z)
    return str(z)


a = "-13C3C2D-5%-8.1%2"
special(a)

