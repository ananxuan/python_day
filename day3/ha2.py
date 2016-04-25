import  json
import collections
import copy

#实现功能:
# 1、可修改backend配置，如果关键字存在，则会替换原有配置，如果不存在则新增一条配置。
# 2、可查看配置
# 3、可按需要确定是否保存

# 字典中保存格式
# OrderedDict([('backend',
#       OrderedDict([('www.oldboy.org',['server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000']),
#                    ('buy.oldboy.org', ['server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000'])]))])

#读取ha.cnf的backend配置文件
def read_conf():
    global HA_CONF
    with open('ha.cnf','r') as f:
        head = ""
        body = ""
        # 记录"backend"记录是否已在字典中
        the_next_is_belong_to_backend = False
        for line in  f.readlines():
            # 匹配"backend开头的行
            if line.startswith("backend"):
                the_next_is_belong_to_backend = True
                line = line.strip().split()
                head = line[0]
                body = "    ".join(line[1:])
                HA_BODY = collections.OrderedDict()
                HA_BODY[body] = []
                # 如果字典中不存在"backend关键字"
                if HA_CONF.get(head) == None:
                    HA_CONF[head]=copy.copy(HA_BODY)
                else:
                    HA_CONF[head][body]= []
            elif the_next_is_belong_to_backend and line.startswith(" "):
                line = line.strip()
                if len(line) != 0:
                    HA_CONF[head][body].append(line)
            # 如果某行不是"backend"打头，也不是空格或换行打头则将is_find_backend置False
            else:
                the_next_is_belong_to_backend = False


#打印字典形式的配置文件
def print_conf():
    global HA_CONF
    print(HA_CONF)
    for i in HA_CONF.items():
        print(i)


def deal_conf():
    global SWITCH_BACKEND
    while True:
        print("     \033[1;32;0mgo   来，配置吧; \033[1;31;0mdis 打印当前配; \033[1;33;0mquit 退出; \033[1;34;0msave 保存\033[0m")
        line_input = input(" > ").strip().lower()
        try:
            # 将输入转换为函数
            fun = SWITCH_BACKEND.get(line_input)
        except(Exception):
            print("\033[1;31;40m输入错误!\033[0m")
            continue
        # 执行函数
        if fun != None:
            fun()
        else:
            print("\033[1;31;40m输入错误!\033[0m")

# 修改配置
def mod_conf():
    global HA_CONF
    print("\033[1;32;40;m请按如下格式输入：\033[0m")
    print("{\"backend\":{\"new.oldboy.org\":[\"server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000\"]}}")
    line_input = input("input your record> ").strip().lower()
    # 调用json将输入转换为字典
    try:
        record = json.loads(line_input)
        # 如果存在"backend"关键字
        if record.get("backend") != None:
            for key in record["backend"]:
                    # 将记录中的配置加入HA_CONF
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

# 打印配置
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

# 程序入口
if __name__ == "__main__":
    read_conf()
    print_conf()
    deal_conf()
