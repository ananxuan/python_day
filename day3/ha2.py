import  json
import collections
import copy

#实现功能编辑修改保存backend（后台配置文件）

#读取ha.cnf的backend配置文件
def read_conf():
    global HA_CONF
    with open('ha.cnf','r') as f:
        head = ""
        body = ""
        is_find_backend = False
        for line in  f.readlines():
            if line.startswith("backend"):
                is_find_backend = True
                line = line.strip().split()
                head = line[0]
                body = "    ".join(line[1:])
                HA_BODY = collections.OrderedDict()
                HA_BODY[body] = []
                if HA_CONF.get(head) == None:
                    HA_CONF[head]=copy.copy(HA_BODY)
                else:
                    HA_CONF[head][body]= []
            elif is_find_backend:
                line = line.strip()
                if len(line) != 0:
                    HA_CONF[head][body].append(line)


#打印字典形式的配置文件
def print_conf():
    global HA_CONF
    for i in HA_CONF.items():
        print(i)


def deal_conf():
    while True:
        print("     \033[1;32;0mgo   来，配置吧; \033[1;31;0mdis 打印当前配; \033[1;33;0mquit 退出; \033[1;34;0msave 保存\033[0m")
        line_input = input(" > ").strip().lower()
        try:
            fun = SWITCH_BACKEND[line_input]
        except(Exception):
            print("\033[1;31;40m输入错误!\033[0m")
            continue
        if fun != None:
            fun()
        else:
            print("\033[1;31;40m输入错误!\033[0m")


def mod_conf():
    global HA_CONF
    print("\033[1;32;40;m请按如下格式输入：\033[0m")
    print("{\"backend\":{\"new.oldboy.org\":[\"server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000\"]}}")
    line_input = input("input your record> ").strip().lower()
    try:
        record = json.loads(line_input)
        if record.get("backend") != None:
            for key in record["backend"]:
                    HA_CONF["backend"][key] = record["backend"][key]
    except(Exception):
        print("\033[1;31;40m输入错误\033[0m")


#退出程序
def back():
    print("\033[5;31;40m已经退出\033[0m")
    exit()


#保存配置文件
def save():
    global HA_CONF
    try:
        with open("new_ha2.cnf","w") as f:
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
            print("\033[1;32;40m文件保存成功\033[0m")
    except(Exception):
        print("\033[1;31;40m保存文件出现错误!\033[0m")


def display():
    global HA_CONF
    for key1,value1 in HA_CONF.items():
        print("%-10s"%(key1),end="")
        head_is_print = False
        for key2,value2 in value1.items():
            if head_is_print ==False:
                print(key2)
                head_is_print = True
            else:
                print("%-10s"%(key1),end="")
                print(key2)
            for value3 in value2:
                print("%s%s"%(10*" ",value3))
    print("#")


#定义全局变量
SWITCH_BACKEND = {"go":mod_conf,"quit":back,"save":save,"dis":display}
HA_CONF = collections.OrderedDict()


if __name__ == "__main__":
    read_conf()
    # print_conf()
    deal_conf()
