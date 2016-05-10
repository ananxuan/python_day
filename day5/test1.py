
import random

checkcode = '52'

for i in range(14):
    current = random.randrange(0,9)
    checkcode += str(current)

# print(checkcode)

import 密码复杂度检测 as pc

while True:
    str1 = input("请输入密码> ").strip()
    if pc.check_password_complexity(str1,2):
        print("%s复杂度符合要求"%str1)
        break


