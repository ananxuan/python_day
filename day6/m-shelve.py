#!/usr/bin/env python3
__author__ = 'DSOWASP'
import json
import shelve


#
# a= {"a":"abc"}
# b = 2
#
# class c(object):
#     def __init__(self):
#         self.a = 1
#
# d =shelve.open("shelve.shv")
# d["ok"] = a
# d["no"] = b
# d["yes"] = c

class c:
    def __init__(self):
        self.a = 2

# print(c.__class__.)
a = shelve.open("shelve.shv")
for key,value in a.items():
    if value.__class__.__name__  == 'type':
        c1 = c()
        print(c1.a)


