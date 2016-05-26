#!/usr/bin/env python3
__author__ = 'DSOWASP'
import sys
import os
import time
#
# for i in range(10):
#     str = ("\r%s"%("="*i)).ljust(10)+("[%d%%]"%(i*10)).rjust(6)
#     sys.stdout.write(str)
#     # sys.stdout.flush()
#     time.sleep(0.1)

# for i in range(10):
#     print("")
#     time.sleep(0.5)

# a = ["!","@","#","$","%","^","&","*","(",")"]
# i = 1
# s,s1 = 0,0
# while s < 100 or s1 < 100:
#     n = i % 10
#     s = i * 10
#     s1 = i * 5
#     l = s // 10
#     l1 = s1 // 10
#     if s <= 100:
#         str = "{}{}".format(("\r%s"%(a[n]*l)).ljust(11),("[%d%%]"%(s)).rjust(6))
#     if s1 <=  100:
#         str1 = "{}{}".format(("%s"%(a[n]*l1)).ljust(11),("[%d%%]"%(s1)).rjust(6))
#     str2 = str  + str1
#     print(str2,end="")
#     time.sleep(0.1)
#     i += 1
# else:
#     print("")

# for i in range(5):
#     print("=",end="")
#     time.sleep(1)
# print("=",end="")
# time.sleep(1)
# print("=",end="")

# print("==".rjust(10))

# print("==")
# os.system("cls")
# print("==")
# os.system("cls")
# print("==")
#
# import sys,time
# for i in range(100):
#     k = i + 1
#     str = '>'*i+' '*(100-k)
#     sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
#     sys.stdout.flush()
#     time.sleep(0.1)


# import sys,time
# if __name__ == '__main__':
#     for i in range(1,61):
#         sys.stdout.write('#'+'->'+"\b\b")
#         sys.stdout.flush()
#         time.sleep(0.5)

i = 1
n = 100
t = 0.1
while n >= 0:
    if i < 100:
        info = ("[%d%%]"%(i)).rjust(6)
        str1 = "\r{}{}".format(("#"*i).ljust(101),info)
        i += 1
    else:
        t = 0.05
        if n == 100:
            info = "\033[1;31;0m[error]\033[0m"
            t = 1
        else:
            info = ("[%d%%]"%(n)).rjust(6)
        str1 = "\r{}{}".format(("#"*n).ljust(101),info)
        n -= 1

    print(str1,end="")
    time.sleep(t)
