def special():
    import re
    a = "dtaabbbbq24124bwdsrwadasd a\n wawfsdf w \n dwf \n jwk"
    # 下面表示表达式表示搜索'a'开始然后再试任意字符或空白字符出现n次，直到能以'w'作为结束且不能再匹配为止。
    # 但是打印时只打印圆括号里的找匹配'w'时的最后一次出现的字符
    # .是表示单个字符不能匹配换行
    b = re.findall('a(.|\s)*w',a)
    c = re.search('a(.|\s)*w',a)
    d = re.findall('(a)(.|\s)*(w)',a)
    e = re.findall('[\w]*',a)
    print(b)
    print(c.group())
    print(d)
    print(e)
    # print(b.group())

# special()

# 分组匹配 m/group(1
#
#
#
# 冒泡排序
def maopao(c):
    for j in range(1,len(c)):
        for i in range(len(c)-j):
            if c[i] > c[i+1]:
                # temp = c[i]
                # c[i] = c[i+1]
                # c[i+1] = temp
                c[i] , c[i+1] = c[i+1] ,c[i]
        print(c)
    return c
b = [2,4,12,4,89,3,100,1]
# print(maopao(b))

import again.page
# from mod.again.page import dis.show
# import page.show
# again.page.show()


class t1:
    def __init__(self):
        pass
    # AttributeError: 'test1' object has no attribute '__t1',不能被实例调用
    def __t1(self):
        print("调用__t1")

    def api(self):
        # print(self.name)
        print("类调用")

class show:
    def __init__(self):
        self.name = "ds"
        pass

    def getapi(self):
        # print(self)
        # t1.api(self)
        t = t1()
        t.api()

# a = show()
# a.getapi()

import random,hashlib
m = hashlib.md5()
m.update(b'a')
print(m.hexdigest())