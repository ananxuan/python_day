#!/usr/bin/env python3
__author__ = 'DSOWASP'


class cat:
    def __init__(self,jiao,name):
        self.jiao = jiao
        self.name = "error"

class dog(cat):
    def __init__(self,jiao,name):
        super(dog,self).__init__(jiao,name)
        self.name = "not error"


dog1 = dog("wwj","dog1")
print(dog1.jiao,dog1.name)