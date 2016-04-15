# a=[1]
# b=[1]
# a.append(2)
# try:
#     b.extend(2)
# except(TypeError):
#     print("类型错误")
# print("a=",a)
# print("b=",b)
# a.append([3,4])
# b.extend([3,4])
# print("a=",a)
# print("b=",b)
#
#
# def abc():
#     print("haha")
#     return [2,3]
# print(abc()[1])
# ["gg","kk"][0]
#
#
# class CbaBa(object):
#     if 1 == 2:
#         print("class ok ")
#     else:
#         print("not ")


# with open('abc.txt','r') as f:
#     print(f.readline(),end='')
#     print(f.readline(),end='')
#     f.seek(0)
#     print(f.readline(),end='')
a = ['a','b','c','d',9,'e']
for i in a:
    a.remove(i)
    print(a)

print("last:",a)