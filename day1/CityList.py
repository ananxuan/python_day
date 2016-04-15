
##### 从cities.txt读取省市县区到内存，进行初始化，信息在内存中
##### 用列表+字典方式存储，如下：

"""
[
{
"name":山西省",
"cities":[{
    "name":"太原市",
    "counties":["x县","y县"]
    },
    {
    "name":"阳泉市"
    "counties":["w县","z县"]
    }
    ]
}
,
{
"name":湖南省",
"cities":[{
    "name":"长沙市",
    "counties":["a县","b县"]
    },
    {
    "name":"岳阳市"
    "counties":["c县","d县"]
    }
    ]
}
]
"""

cities = []                     # 存放省市县信息
province_set = 'No'            # 标识此省是否已存在于cities列表中


def init_cities():              # 从cities.txt读取城市信息用来初始化cities

    global province_set
    with open('Cities.txt','r',encoding='utf-8') as f:        # 读取城市信息
        for line in f.readlines():
            line=line.strip()
            l_line = line.split("||")                             # 将cities逐行读取，并转换为列表
            try:
                for i in cities:
                    if l_line[0] == i["name"]:                    # 如果省存在于cities中，则将市和县的信息添加到省后面
                        i["cities"].append({"name":l_line[1],"counties":l_line[2:]})
                        province_set = 'Yes'
                        break
                    else:
                        province_set = 'No'                        # 在cities中没找到省的信息
            except:
                pass

            if province_set == 'No':                               # 新增省市县到cities中
                # count += 1
                province_name = l_line[0]
                city_name = l_line[1]
                cities.append(
                    {"name":province_name,"cities":
                        [{"name":city_name,"counties":l_line[2:]}]
                     }
                )
                province_set = 'Yes'

    return "Ok"


def helpme():                               # 城市之旅帮助信息
    print("""
    list        显示当前级别的省或市或县/区列表
    quit        返回上一级或退出
    n           n是数字,根据list输出的结果，进入此省或市或县/区
    """)


def city_travel():                          # 城市之旅，可以查看省市县信息
    level = 0                                # 0表示可以查看省列表，1表示可以查看市列表,2表示可以查看县/区列表
    pr_n = 0                                 # 省的数字标识，可通过"list"命令查看
    ci_n = 0                                 # 市的数字标识，可通过"list"命令查看
    level_name = ["国家级","省级","市级","县/区级"]
    while True:
        # pr_n = 0
        # ci_n = 0
        #### 显示帮助信息和当前位置
        helpme()
        if level == 0:
            print("您当前位于中国，%s，可以查看%s列表！"%(level_name[level],level_name[level+1]))
        elif level == 1:
            print("你当前位于%s,可以查看%s列表"%(cities[pr_n]["name"],level_name[level+1]))
        elif level == 2:
            print("您当前位于%s%s，可以查看%s列表"%(cities[pr_n]["name"],cities[pr_n]["cities"][ci_n]["name"],level_name[level+1]))
        else:
            print("出现错误，需管理员处理!!!")
            exit()

        #### 输入命令，查看省市县信息
        your_input = input("请输入>> ").strip()

        if your_input == 'list':            # 显示当前视图的列表

            if level ==0:                    # 显示省列表
                num = 0
                for i in cities:
                    print(num,"    ",i["name"])
                    num += 1
            elif level == 1:                # 显示市列表
                num = 0
                for i in cities[pr_n]['cities']:
                    print(num,"     ",i['name'])
                    num += 1
            elif level == 2:                # 显示县/区列表
                num = 0
                for i in cities[pr_n]["cities"][ci_n]["counties"]:
                    print(num,"     ",i)
                    num += 1
            # print("level=%d"%level)
            # print("pr_n=%d"%pr_n)
            # print("ci_n=%d"%ci_n)

        elif your_input == 'quit':           # 返回上一级或退出
            if level == 2:                    # 级别减一
                level -= 1
                print("已退出%s,你处于%s"%(cities[pr_n]['cities'][ci_n]['name'],cities[pr_n]['name']))
                ci_n =0
            elif level == 1:                  # 级别减一
                level -= 1
                print("已退出%s,你处于中国"%(cities[pr_n]['name']))
                pr_n = 0
                ci_n = 0
            else:                               #否则退出
                exit()
        else:
            try:
                your_input = int(your_input)           # 如果输入的是数字，且在正常范围内
                if level == 0:                         # 进入某省
                    print("欢迎进入%s!"%cities[your_input]["name"])
                    level = 1
                    pr_n = your_input
                elif level == 1:                       # 进入某县/区
                    print("欢迎进入%s!"%cities[pr_n]["cities"][your_input]["name"])
                    level = 2
                    ci_n = your_input
                elif level == 2:
                    print("已到最底层，请输入\"list\"或\"quit\"")
            except(ValueError,IndexError):          # 否则提示输入错误
                print("输入错误，请重新输入")


if __name__ == "__main__":
    # 初始化cities
    if "Ok" == init_cities():
        print("cities初始化成功！,开始你的城市之旅吧！")
    else:
        print("cities初始化失败！，程序退出")
        exit()
    # 开始您的城市之旅！
    city_travel()
else:
    print("请使用python CityList.py运行")
