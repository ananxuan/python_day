import json
import  collections
import copy
"""
{
    "backend":{"www.oldboy.com":[["server","100.1.7.90"],["server","100.1.7.90"]]}
}
"""
#读取配置文件到有序字典
def read_conf():
    global HA_CONF
    with open('ha.cnf','r') as f:
        head = ''
        body = ''
        for line in  f.readlines():
            if line[0] != " " and line != "\n":
                line = line.strip().split()
                head = line[0]
                body = "    ".join(line[1:])
                HA_BODY = collections.OrderedDict()
                HA_BODY[body] = []
                if HA_CONF.get(head) == None:
                    HA_CONF[head]=copy.copy(HA_BODY)
                else:
                    HA_CONF[head][body]= []
                    # print(head,body)
            else:
                line = line.strip()
                if len(line) != 0:
                    HA_CONF[head][body].append(line)


def print_conf():
    global HA_CONF
    for i in HA_CONF.items():
        print(i)


def deal_conf():
    global LINE_SYMBOL
    while True:
        line_input = input(LINE_SYMBOL," ").strip()
        if

LINE_SYMBOL = ">"
HA_CONF = collections.OrderedDict()
read_conf()
print_conf()