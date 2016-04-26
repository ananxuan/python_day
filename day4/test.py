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
def create_re():
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

def create_raise():
    try:
        a = {"name":18}
        b = a["a"]
        print(b)
    except(Exception):
        pass

# create_raise()

# 子程序和协程

def A():
    import time
    print("A")
    time.sleep(100)
def B():
    print("B")
    A()

def C():
    print("C")
    B()

def D():
    n = 1
    while n < 5:
        m = yield n
        print("m:",m)
        print("n:",n)
        n += 4
        yield 10
        yield

d = D()
# __next__() 是寻找下一个yield，并将yield后面的值返回,右面没值，则返回None,如果没找到yield 就报错,__next__()不给yield传值
# j = d.__next__()
# print(j)
# j = d.__next__()
# print(j)

# send(x)是返回上一个中断的yield，并将值传给yield,然后寻找下一个yield,并将yield后面的值返回,如果没找到下一个yield，就报错
# 如果在这之前没有开启generator，则只能传递None值给yield (使用 send(None))，并立即返回yield后面的值
# j = d.send(3)  # TypeError: can't send non-None value to a just-started generator

def exam1():
    j = d.send(None)   # j = 1 ， 返回的是第一次遇到yield后 n的值
    print(j)    # j = 1
    #
    # 1
    j = d.send(3)
    print(j)
    # 1
    # m: 3
    # n: 1
    # 10
    j = d.__next__()
    print(j)
    # 1
    # m: 3
    # n: 1
    # 10
    # 4
    j = d.send(20)

# exam1()

# 编码问题  ,b表示字节(最前面的0去掉)，\x表示16进制
# UTF-8是这样做的：

# 1. 单字节的字符，字节的第一位设为0，对于英语文本，UTF-8码只占用一个字节，和ASCII码完全相同；
#
# 2. n个字节的字符(n>1)，第一个字节的前n位设为1，第n+1位设为0，后面字节的前两位都设为10，这n个字节的其余空位填充该字符unicode码，高位用0补足。
# 这里有一个很大的问题,bin只是将数字转为二进制，并非转为了unicode编码，unicode是2字节，python3和内存中都是unicode保存，
# ord是返回字符在unicode的位置，比如空格" "的位置是32，bin(32)就是0b100000,这样就省略了10个0，
# 网络传输是以bytes传输
def test_code():
    a = " "
    print(bin(ord(a.encode())))       # 0b100000     # 最前面的10个0去掉
    print(bin(ord(a)))                # 0b100000
    print(ord(a))                     # 32
    a = "~"
    print(bin(ord(a.encode())))       # 0b1111110    # 最前面的9个0去掉
    print(bin(ord(a)))
    print(ord(a))                     # 126

    a = "ab"
    print(a.encode())       # b'ab'   # bytes
    a = str("ab")
    print(a.encode())       # b'ab'   # bytes     其二进制表示可以查ascii表
    a = "我"
    print(a.encode())       # b'\xe6\x88\x91'
    print(ord(a))           # 25105         # """ Return the Unicode code point for a one-character string. """
    print(bin(ord(a)))      # 0b 1100010 00010001
    print(bin(25105))       # 0b 1100010 00010001     # 返回的应该是unicode编码  ，最前面的一个0去掉了0b 01100010 00010001
    for i in a.encode():
        print(i)            # 230            136            145
        print(bin(i))       # 0b11100110     0b10001000     0b10010001    则unicode编码为 0110 001000 010001

    a = "我"
    print(a.encode(encoding='gbk'))     # b'\xce\xd2'

    a = "你"
    print(a.encode())       # b'\xe4\xbd\xa0'
    # 报
    # 01100010 10100101                 # unicode
    # 11100110 10001010 10100101        # utf-8

    print("我".encode("gbk"))        # b'\xce\xd2'
    for i in "我".encode(encoding='gbk'):
        print(i)                    # 206               210
        print(bin(i))               # 0b11001110        0b11010010

    print("######")
    print("我".encode("gb2312"))  # b'\xce\xd2'
    for i in "我".encode("gb2312"):
        print(i)                    # 206               210
        print(bin(i))               # 0b11001110        0b11010010

    print("#############")
    # print(str("我".encode().decode()))


def tihuan(o):
    import re
    print(o)
    o = o.replace('*-','AA')
    o = o.replace("/-","BB")
    print(o)
    l1 = re.findall('^-?\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|\d+\.?\d*[/|*/\"AA\"|\"BB\"][^+-]+|^-*[^+-]+|[^+-]+',o)
    print(l1)

# tihuan("-10.1/12*-11.112-9 -2*5/3 +7.1 /3*99/4*2998 -10 * 56.8/-14+13")

# 中括号的  -  要么放在最前面，要么放在最后面,才表示  - 要么转义
def z_kuohao():
    import re
    m = "1+1asds,ad*23-.4z"
    l = re.findall('[a\-z]+',m)
    print(l)
z_kuohao()