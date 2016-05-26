#!/usr/bin/env python3
__author__ = 'DSOWASP'


import os
import sys

print(__file__)
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)
sys.path.append(BASEDIR)
print(__name__)

from a import mod1
