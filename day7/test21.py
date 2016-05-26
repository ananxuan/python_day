#!/usr/bin/env python3
__author__ = 'DSOWASP'

import time
n = 0
while True:

    if n < 10:
         s = "\r{}".format("="*n)
    s1 = "---"
    s2 =s + s1
    print(s2,end="")

    if n > 20:
        break
    n += 1
    time.sleep(0.1)