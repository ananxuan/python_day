#!/usr/bin/env python3
__author__ = 'DSOWASP'
class Hello(object):
    A = 1
    def __init__(self,name,sex):
        self.nam = name
        self.sex = sex
    def buy(self):
        print("asdad")


a = Hello("ds","m")
b = Hello("ds","m")
c = Hello("ds","m")

a.A = 2
# b.A = 2
Hello.A = 3
# b.A = 3

print(a.__dir__())

print(b.__dir__())


print(id(a.A))
print(id(b.A))
print(id(c.A))

def kat(o):
    # print(o.A)
    o.buy()
    print("kkkkkkk")
a.buy()
Hello.buy = kat

a.buy()