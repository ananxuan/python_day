def a():
    print("aaaa")

def b():
    print("bbbbb")

dic = {"1":a,"2":b}

c = input("input> ")

if dic.get(c) != None:
    print(dic.get(c)())