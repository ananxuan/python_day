#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DGS'

# 实现的功能，只有你eval()能够算来的值，我自己写的代码也就能算出来
import re
from chengfa import chengfa
from jiafa import jiafa
from calculate import calculate
from equl_tihuan import equl_tihuan

# m 为字符串表达式
# m = "-13**3**2//-1.2%+0.1+-13//-3-3.1+ 5.1*12+(-0.2) *(-60.9-30/4+( -(-40.6/ -3.01))*    (-10.1/12*-11.112/+9-1111-(100*---++-+3.12*71.1/9.3 -2)*5*3 +7.1 /3*99/4*2998 -10 * 56.8/-14*-1.123+13)) - (-4*3)/(16-3*2)"
# m = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# m = "2.0 +-13//-3 "
# m = "4.2+2.1"
# original用于eval计算来对比自己写的算法是否正确


# 算术主函数
def math(arith_str):
    #替换空格、--、++、-+、+-、/+、*+为去空格、+、+、-、-、/、*,还有去掉行首的 + 号
    arith_str = equl_tihuan(arith_str)
    # 如果发现括号，则先算括号里面的
    if re.findall('[()]+', arith_str):
       arith_sub = re.findall('[(][^()]+[)]', arith_str)  #取所有最内部括号
       n = 0
       for i in arith_sub:
          # 取括号内的表达式
          j = re.search('[^()]+',i).group()
          # 算括号内的值
          i = calculate(j)
          # 将原来的括号替换为算出来的值
          arith_str = arith_str.replace(arith_sub[n], i, 1)
          n = n + 1
       # print("去最外层括号:", arith_str)
    # 如果没有括号，则再算加减乘除
    elif re.findall('[+*/-]+', arith_str):
        # print(arith_str)
        if re.search('e-',arith_str) == None:
            arith_str = calculate(arith_str)
        return arith_str
    # 如果就一个字符串，不包含括号和加减乘除则，直接返回
    else:
        return arith_str
    # arith_str = equl_tihuan(arith_str)
    return math(arith_str)

if __name__ == '__main__':
    m = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    # m = "5--13**3**2//-1.2%+0.1+-13//-3-3.1+ 5.1*12+(-0.2) *(-60.9-30/4+( -(-40.6/ -3.01))*    (-10.1/12*-11.112/+9-1111-(100*---++-+3.12*71.1/9.3 -2)*5*3 +7.1 /3*99/4*2998 -10 * 56.8/-14*-1.123+13)) - (-4*3)/(16-3*2)"
    # m = "5+-5.1/-3"
    while True:
        if m == "":
            m = input("请输入要求的算术> ")
        if m == 'quit':
            exit()
        elif m.strip() == "":
            continue
        original = m
        print ("The original input:",m)
        if re.search('[^\d+*/.() %-]',m):
            print("有非法字符")
            m = ""
            continue
        m = math(m)
        print("The result is:" ,m)
        if re.search('e',m):
            print("还存在e，需要做进一步处理，这里先用eval来计算最后结果！")
            print("对result用eval进行计算：eval(%s)=%s"%(m,str(eval(m))))
        print("eval(original)=",eval(original))
        m = ""