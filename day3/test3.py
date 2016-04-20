x = 10
y = 20
def a():
    y = 2
    # x = x + 1  错误
    print("a-x",x)
    print("a-y",y)
    def b():
        x = 1
        # y = y + 1  错误

        print("b-x",x)
        print("b-y",y)
    b()
a()


# x = 10
# def  a():
#     print(x)
#     x = x + 1
#     print(x)
#
# a()