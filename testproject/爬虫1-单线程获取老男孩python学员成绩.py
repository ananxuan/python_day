#!/usr/bin/env python3
__author__ = 'DSOWASP'
#encoding:UTF-8
import urllib
import urllib.parse
import http.cookiejar
import urllib.request
import prettytable
import collections
import logging
import threading
import time

# 初始化logging
# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

starttime = time.time()
# urllib.request.urlopen(url) 返回 http.client.HTTPResponse 对象

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = http.cookiejar.LWPCookieJar()
cookies_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookies_support,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

# get
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
# 获取网站内容
url = "http://crm.oldboyedu.com/crm/grade/single/"

# 打印第一次get日志
# logging.info(r"the 1th time start connect http://crm.oldboyedu.com/")

h = urllib.request.urlopen(url)
# 打印第一次get日志
# logging.info(r"the 1th time end connect http://crm.oldboyedu.com/")
# 获取csrfmiddlewaretoken
data = h.read().decode('UTF-8')
for i in data.split('\n'):
    # <form class="col-xs-12 col-sm-10 col-sm-offset-1" method="post" action="/crm/grade/single/"><input type='hidden' name='csrfmiddlewaretoken' value='QKNMJKS49GvbVBdBzADwFT2HuHxIUUcP' />
    if "csrfmiddlewaretoken" in i:
        i = i.strip().split('value')
        m = i[1].split('\'')
        token = m[1]

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
# header_dict={'User-Agent':\
#            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

# qq列表
qq_list = [
'493513100','813231615','434330017','409966346',
'378777322','295964805','710275039','114648340','1016150581','1205645845',
'307126079','437512689','5272689','776214156','121440150','27206461','763227',
'244131566','33532767','1172861184','642445498','894725902','634086977','1241424377',
'290070744','290528767','178569706','15308403545','2547788','118146449','369545989',
'972102425','610550690','501193747','384526074','676596084','109368424','584641574'
]
# 学号列表
xuehao_list = [
 '1','2','3','4','5',
'6','7','8','9','10','11','13','14','15',
'16','17','18','19','20','21','22','23',
'24','25','26','27','28','29','30','31',
'32','33','34','35','36','37','38','39'
]

chengji_list = collections.OrderedDict()


# 构建线程列表
threeads = []

#构造Post数据，他也是从抓大的包里分析得出的。

for qq in qq_list:
    post = {}
    post['search_str'] = qq
    post['csrfmiddlewaretoken'] = token
    # 成绩列表默认为空
    chengji_list[qq] = []

    #需要给Post数据编码
    post_data = urllib.parse.urlencode(post).encode(encoding="utf-8")
    # post
    # req = urllib.request.Request(url,data=post_data,headers=header_dict)
    req = urllib.request.Request(url,data=post_data)

    # 打印获取成绩前的时间
    # logging.info("start get %s's grade"%qq)
    data2 = urllib.request.urlopen(req,timeout=2)
    # 打印获取成绩前的时间
    # logging.info("end get %s's grade"%qq)

    # print(type(data2)) # <class 'http.client.HTTPResponse'>
    data = data2.read()
    data = data.decode('UTF-8')
    data = data.split('\n')
    # p_chegnji 如果遇到'<td>'则为True，下一行则就成绩。
    p_chengji = False
    for i in data:
        i = i.strip()
        if len(i) != 0:
            if p_chengji == True:
                chengji_list[qq].append(i)
                p_chengji = False
            # 获取成绩的的代码需要根据实际网页放回的源码而定。可以右键查看源代码来分析一种较好的方法获取到想要的值。
            if '<td>' == i:
                p_chengji = True
endtime1  = time.time()
# 上课天数或网页上已展示的成绩列数
l = len(chengji_list[qq_list[0]])
# 打印模块头部
PrettyTlist = ['学号','QQ']
# 根据已展示的天数来扩充打印模块头部
for i in range(l):
    i = i + 1
    PrettyTlist.append('Day%d'%i)
# 添加打印模块头部'总分'
PrettyTlist.append('总分')
# 实例化打印头部
a = prettytable.PrettyTable(PrettyTlist)

# 总成绩列表，qq:总成绩
sumc_chengji_list = {}
for xueyuan,grade in chengji_list.items():
    if grade != []:
        sumc = 0
        for i in grade:
            if i == 'A+':
                sumc += 100
            elif i == 'A':
                sumc += 90
            elif i == 'B+':
                sumc += 85
            elif i == 'B':
                sumc += 80
            elif i == 'B-':
                sumc += 70
            elif i == 'C+':
                sumc += 60
            elif i == 'C':
                sumc += 50
            elif i == 'C-':
                sumc += 40
            else:
                sumc += 0
    else:
        # 如果查不到学员的成绩
        sumc = 0
        for i in range(l):
            chengji_list[xueyuan].append('N/A')
    chengji_list[xueyuan].append(sumc)
    sumc_chengji_list[xueyuan]=sumc
# [(qq,总成绩),()]
# sorted,把items()的值给lamdba,asd[0] 为qq号，asd[1]为总成绩，key表示排序的列，resverse 为True表示降序

# sorted(dic,value,reverse)
# dic为比较函数，value 为排序的对象（这里指键或键值），
# reverse：注明升序还是降序，True--降序，False--升序（默认）

sort_chengji_list = sorted(sumc_chengji_list.items(),key = lambda asd:asd[1],reverse = True)

# 生成打印列表
for xueyuan,grade in sort_chengji_list:
    add_row = [xuehao_list[qq_list.index(xueyuan)],xueyuan]
    for i in chengji_list[xueyuan]:
        add_row.append(i)
    a.add_row(add_row)
print(a)
endtime2 = time.time()
print("程序开始时间",starttime)
print("成绩爬取结束时间",endtime1)
print("程序结束时间",endtime2)
print("持续时间",endtime2-starttime)