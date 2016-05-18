#!/usr/bin/env python3
__author__ = 'DSOWASP'
import sys
import os
print("b%s"%sys.path)
print(os.path.abspath(__file__))
print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.getcwd())
print(os.listdir("."))
import a