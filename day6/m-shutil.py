#!/usr/bin/env python3
__author__ = 'DSOWASP'
import shutil
import os
# print(__file__)

# 文件拷贝
# f1 = open("srcfile",'rb')
# f2 = open("dstfile",'wb')
# shutil.copyfileobj(f1,f2)

# a = shutil.copyfile("srcfile","dstfile")
# print(a)
# print(os.path.normcase(os.path.abspath("srcfile")))


# shutil.copytree("srcdir","dstdir")
print(os.path.dirname(__file__))
print(os.path.basename(__file__))

import shelve
shelve.