#!/usr/bin/env python3
__author__ = 'DSOWASP'


class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __getattr__(self, item):
        return self.dis
    def show(self):
        print("A_show")
    def dis(self):
        print("A_dis")

a = A(1,2)
getattr(a,"show")()
