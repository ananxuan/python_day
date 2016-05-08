
import random

checkcode = '52'

for i in range(14):
    current = random.randrange(0,9)
    checkcode += str(current)

# print(checkcode)


