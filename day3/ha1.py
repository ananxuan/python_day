import  collections
import copy


"""
#配置文件在字典中的存储格式：
OrderedDict([
('global', OrderedDict([('', ['log 127.0.0.1 local2', 'daemon', 'maxconn 256', 'log 127.0.0.1 local2 info'])]))
('defaults', OrderedDict([('', ['log global', 'mode http', 'timeout connect 5000ms', 'timeout client 50000ms', 'timeout server 50000ms', 'option  dontlognull'])]))
('listen', OrderedDict([('stats    :8888', ['stats enable', 'stats uri       /admin', 'stats auth      admin:1234'])]))
('frontend', OrderedDict([('oldboy.org', ['bind 0.0.0.0:80', 'option httplog', 'option httpclose', 'option  forwardfor', 'log global', 'acl www hdr_reg(host) -i www.oldboy.org', 'use_backend www.oldboy.org if www'])]))
('backend', OrderedDict([('www.oldboy.org', ['server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000']), ('buy.oldboy.org', ['server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000'])]))
]}
"""

#读取配置文件到有序字典
def read_conf():
    global HA_CONF
    with open('ha.cnf','r') as f:
        head = ''
        body = ''
        for line in  f.readlines():
            # 如果行记录是以字符打头
            if line[0] != " " and line != "\n":
                line = line.strip().split()
                head = line[0]
                body = "    ".join(line[1:])
                HA_BODY = collections.OrderedDict()
                HA_BODY[body] = []
                # 如果关键字不存在入字典中，则加入关键字
                if HA_CONF.get(head) == None:
                    HA_CONF[head]=copy.copy(HA_BODY)
                # 如果存在，则置值为空列表
                else:
                    HA_CONF[head][body]= []
                    # print(head,body)
            # 否则记录行记录到关键字的values中
            else:
                line = line.strip()
                if len(line) != 0:
                    HA_CONF[head][body].append(line)


#打印字典形式的配置文件
def print_conf():
    global HA_CONF
    for i in HA_CONF.items():
        print(i)


#处理配置文件
def deal_conf():
    global CURRENT_INPUT_HEAD
    global LEVEL
    while True:
        line_input = input("[]# ").strip().lower()
        list_input = line_input.split()
        # 根据输入切换到特定的函数
        fun = SWITCH_GLOBAL.get(list_input[0])
        # 执行函数
        if fun != None:
            fun(*list_input)
        else:
            print(line_input)
            print("^ error")


#backend配置处理
def backend(*args):
    # 判断输入是否合法
    if len(args) > 1:
        if args[1] != '?':
            line = " ".join(args)
            print(line)
            print(" ".ljust(len(args[0])),"^ error")
            return
        else:
            print(" <cr>")
            return
    global LEVEL
    global CURRENT_INPUT_HEAD
    global CURRENT_INPUT_BODY
    global SWITCH_BACKEND
    # 设置当前级别和关键字
    LEVEL = 1
    CURRENT_INPUT_HEAD = "backend"
    while True:
        line_input = input("[%s]# "%(CURRENT_INPUT_HEAD)).strip().lower()
        list_input = line_input.split()
        # print("BACKEND")
        # 将输入转换为特定的函数
        fun = SWITCH_BACKEND.get(list_input[0])
        if fun != None:
            fun(*list_input)
            if LEVEL == 0:
                return
        else:
            print(line_input)
            print("^ error")


#撤销配置，
def undo(*args):
    global LEVEL
    global CURRENT_INPUT_HEAD
    global CURRENT_INPUT_BODY
    global HA_CONF
    # 判断输入是否合法
    if len(args) != 2:
        print("命令错误，请用undo xxx")
        return
    elif args[1] == "?":
        print("%s"%args[0])
        print("options:")
        if LEVEL == 0:
            for i in HA_CONF:
                print(" ",i)
        elif LEVEL == 1:
            for i in HA_CONF[CURRENT_INPUT_HEAD]:
                print(" ",i)
        return
    try:
        # 删除记录
        if LEVEL == 0:
            HA_CONF.pop(args[1])
        elif LEVEL == 1:
            HA_CONF[CURRENT_INPUT_HEAD].pop(args[1])
    except(Exception):
        line = " ".join(args)
        print(line)
        print(" ".ljust(len(args[0])),"^ error")
        return

    display(args)

# 帮助信息
def helpme(*args):
    print(LEVEL)
    if LEVEL == 0:
        print("""
        backend     进入backend配置视图
        display     显示当前视图下的配置
        undo        撤销某条配置
        ?           显示帮助信息
        quit        返回上一级或退出
        save        保存配置文件
        """)
    elif LEVEL == 1:
        if CURRENT_INPUT_HEAD == "backend":
            print("""
            dnsname        填写域名，进入域名配置模式
            dispaly     显示当前视图下的配置
            undo        撤销某条配置
            ?           显示帮助信息
            quit        返回上一级或退出
            """)

# 打印配置
def display(*args):
    global LEVEL
    global HA_CONF
    if LEVEL == 0:
        for keys1,values1 in HA_CONF.items():
            print(keys1,sep="   ",end="")
            next_values = values1.items()
            n = len(values1.keys())
            print_head_again = False
            for keys2,values2 in next_values:
                if n != 0:
                    if print_head_again == False:
                        print(" ",keys2)
                        print_head_again = True
                    else:
                        print(keys1,sep="   ",end="")
                        print(" ",keys2)
                elif n == 0:
                    print()
                for values3 in values2:
                    print("     ",values3)
    elif LEVEL == 1:

        for keys1,values1 in HA_CONF[CURRENT_INPUT_HEAD].items():
            print(CURRENT_INPUT_HEAD,sep="  ",end="")
            print(" ",keys1)
            for values2 in values1:
                print("     ",values2)

    elif LEVEL == 2:
        if HA_CONF[CURRENT_INPUT_HEAD].get(CURRENT_INPUT_BODY) != None:
            for values1 in HA_CONF[CURRENT_INPUT_HEAD][CURRENT_INPUT_BODY]:
                print(" ",values1)
        else:
            print()

# 回退到上一级
def back(*args):
    global LEVEL
    global CURRENT_INPUT_BODY
    global CURRENT_INPUT_HEAD
    if LEVEL == 0:
        exit()
    elif LEVEL == 1:
        LEVEL -= 1
        CURRENT_INPUT_BODY = ""
        CURRENT_INPUT_HEAD = ""
        return
    elif LEVEL == 2:
        LEVEL -= 1
        CURRENT_INPUT_BODY = ""
        return
    else:
        print("系统错误！")
        exit()

# backend的后台配置处理函数
def dnsname(*args):
    global LEVEL
    global CURRENT_INPUT_BODY
    global CURRENT_INPUT_HEAD
    global HA_CONF
    # 判断输入是否合法
    if len(args) > 2:
        if args[2] == "?":
            print(" <cr>")
            return
        else:
            line = " ".join(args)
            print(line)
            print(" ".ljust(len(args[0]) + len(args[1])+ 1),"^ error")
            return
    elif len(args) == 1:
        line = " ".join(args)
        print(line)
        print(" ".ljust(len(args[0] )),"^ error")
        return
    elif len(args) == 2:
        if args[1] == "?":
            print("%s"%args[0])
            print("options:")
            for i in HA_CONF[CURRENT_INPUT_HEAD]:
                print(" ",i)
            print("  STRING<1-32>        定义一个新的domain")
            return
        else:
            CURRENT_INPUT_BODY = args[1]
            LEVEL = 2
            while True:
                line_input = input("[%s %s]#"%(CURRENT_INPUT_HEAD,CURRENT_INPUT_BODY)).strip().lower()
                list_input = line_input.split()
                n = len(list_input)
                if n < 1:
                    pass
                elif n == 1:
                    if list_input[0] == "?":
                        print("follow the under format to input:")
                        print("server   domain   forward_addr    weight n   maxconn n,example:")
                        print("server   10.1.1.7    10.1.1.7    weight  20  maxconn 1000")
                    elif line_input == "display":
                        display(*list_input)
                    elif line_input == "quit":
                        back(*list_input)
                        return
                    else:
                        print("输入错误！请输入\"?\"查看帮助")
                elif n == 7:
                    HA_CONF[CURRENT_INPUT_HEAD][CURRENT_INPUT_BODY] = []
                    HA_CONF[CURRENT_INPUT_HEAD][CURRENT_INPUT_BODY].append(line_input)
                    display(*list_input)
                else:
                    print("输入错误！请输入\"?\"查看帮助")


#保存配置文件
def save(*args):
    with open("new_ha.cnf","w") as f:
        for key1,value1 in HA_CONF.items():
            for key2,value2 in value1.items():
                new_line = key1 + " " + key2
                f.write(new_line)
                f.write("\n")
                for value3 in value2:
                    f.write("   %s"%value3)
                    f.write("\n")
        #去掉最后一个回车
        f.truncate(f.tell() - 2 )


SWITCH_GLOBAL = {"backend":backend,"undo":undo,"?":helpme,"display":display,"quit":back,"save":save}
SWITCH_BACKEND = {"dnsname":dnsname,"undo":undo,"?":helpme,"display":display,"quit":back}
LEVEL = 0
HA_CONF = collections.OrderedDict()
CURRENT_INPUT_HEAD = ""
CURRENT_INPUT_BODY = ""

if __name__ == "__main__":
    #读取配置文件
    read_conf()
    #打印配置文件
    # print_conf()
    #处理配置文件
    deal_conf()
else:
    print("文件调用失败!")