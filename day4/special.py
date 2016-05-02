#!/usr/bin/env python3
__author__ = 'DSOWASP'
import re
from equl_tihuan import equl_tihuan
import copy

# 特殊运算函数，包括乘方、模、
def special(str1):
    str1 = equl_tihuan(str1)
    # 找出所有数字，这里也可以用 w1 = re.split('CDEFG%')
    # w1 = re.findall('^-*\d+\.?\d*|\d+\.?\d*|-\d+\.?\d*',str1)
    w1 = re.split('[CDEFG%]',str1)
    # print(w1)
    w2 = re.findall('[CDEFG%]',str1)
    w2_temp = copy.copy(w2)
    # 找C（**、乘方）优先级最高
    n = len(w2)
    # 反转运算符顺序，因为乘方得从右往左取值
    w2.reverse()
    # 算乘方
    for i in w2:
        if i == 'C':
            z = float(w1[n-1]) ** float(w1[n])
            # 算出来后就把运算符从列表中去除，并去掉以运算的数字
            w1.pop(n)
            w2_temp.pop(n-1)
            w1[n-1] = z
        n -= 1
    w2 = w2_temp


    # 再算其他运算
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
    return str(z)