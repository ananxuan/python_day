# for i in f:是以迭代的方式访问f文件，
# 而f.read(),f.readlines()是一次性将文件以字符或行的形式读到列表
# f.readline()读取一行到列表
def for_line_in_f():
    with open("test.txt","r",encoding="utf-8") as f:
        for line in f:
            #print("f.tell():",f.tell())    # OSError: telling position disabled by next() call
            print(line,end="")
    print("\n#####")
    with open("test.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            # print(f.tell())
            print(line,end="")


# 创建迭代器
def create_iter():
    a = ["anc","def"]
    b = iter(a)
    print(type(b))      # <class 'list_iterator'>
    print(b)            # <list_iterator object at 0x0000020E36AC50B8>
    # print(b[0])         # TypeError: 'list_iterator' object is not subscriptable
    print(b.__iter__())
    for i in b:
        print(i)

# create_iter()

# 生成器，一个函数包含yield时，那么这个函数的yield会返回一个生成器比如atm1，atm1里的值
# 是每次yield的值，只有调用atm1.__next__()时,函数yield后面的语句才会执行
def create_generator():
    def example1(money1):
        if money1 <= 500:
            money1 -= 100
            yield 100
            print("atm1你来取钱了")
    atm1 = example1(500)
    print(type(atm1))
    for i in atm1:
        print(i)

    print("#######################")
    def example2(money2):
        n = 0
        # print("example2")
        while money2 >= 100:
            money2 -= 100
            n += 1
            print("%d,atm2你来取钱了"%n)
            yield money2
            print("%d,去玩了"%n)
    atm2 = example2(500)        # atm2就是一个生成器类型,如果不执行atm2.__next__(),后面的print("你来取钱")不会执行
    print(type(example2))       # <class 'function'>
    print(type(atm2))           # <class 'generator'>
    # atm2.
    # for i in atm2:              # i的值为每次yield返回的值
    #     print(i)
    print(atm2.__next__())
    # print(atm2.__next__())
# create_generator()


# 生产者消费者
def cusumer():

    pass

def product():
    pass


# 装饰器
def login(fun):
    def inner(*args,**kwargs):
        print("通过认证")
        # print(args,kwargs)
        print("id-fun:",id(fun))
        return  fun(*args,**kwargs)
    return inner

def tv():
    print("这里是tv-%s")
    return 5

# print("id-tv:",id(tv))
# tv = login(tv)
# n = tv()
# print(n)
# tv(*('page',),**{})

# 高级装饰器
def fun1():
    print("fun1")

def fun2():
    print("fun2")

def Filter(f1,f2):
    def outer(main_fun):    # 3、outer(login)     main_fun = login  返回inner
        def inner(f1,f2):
            f1()
            main_fun()
            f2()
        return inner
    return outer

# 1 、先执行Filter(fun1,fun2),返回outer,变成@outer
@Filter(fun1,fun2)      # @outer
def login():            # def login():   # 2、login = outer(login)  # 4、 login = inner
    print("login")

# login()     # 5、执行inner


# 正则
import re
a1 = re.match("abc","abcsdabcff")       # re.match()从首字母匹配，匹配一次
a2 = re.match("abc","babcdabcff")
b1 = re.findall("abc","abcsdfabcf")     # re.findall()查找所有匹配字符
c1 = re.search("abc","ddddabcsdfabcf")      # re.search()查找第一次匹配的字符
d1 = re.sub("abc","@@@@@","abcdfabcdfabc",count=2) # 从行首开始查找。替换2次
print(a1.group())
# print(a2.group())       # AttributeError: 'NoneType' object has no attribute 'group'
print(b1)
print(c1.group(),c1.start())
print(d1)