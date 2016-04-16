# 定义常用函数

def auth(auth_url):
    args = auth_url.split("@")
    auth_flag = False
    if len(args) == 4:
        username = args[0]
        password = args[1]
        auth_file = args[2]
        auth_type = args[3]
        if auth_type == "file":
            try:
                with open(auth_file,'r',encoding='utf-8') as f:
                    init_char = False
                    split_char = "||"
                    for i in f.readlines():
                        if init_char == True:
                            i = i.split(split_char)
                            if username == i[0] and password == i[1]:
                                auth_flag = True
                                break
                        else:
                            i = i.split("##")
                            split_char = i[0]
                            init_char = True
            except (FileNotFoundError):
                print("No such file or directory: '%s'"%(auth_file))
        elif auth_type == "db":
            print("you should use file auth,the db auth are not complete")
        else:
            print("nonsupport auth type")
    else:
        print("error argv count you give")
    return auth_flag