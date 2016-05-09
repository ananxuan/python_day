import  re
'''
密码复杂度检查，包括两种复杂度检查，
level=1时，
    密码不能包含中文，
    长度在10到20个字符之间
    密码必须已字母或下划线开始
    密码必须包含字母、数字、特殊字符
level-2时，
    包含level=1的条件
    不能有一个字符连续出现超过字符长度减8次的情况，比如字符长度是10，则不能有一个字符出现2次的情况
'''
def check_password_complexity(p,level):
    # 判断是否包含中文
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    if zhPattern.search(p):
        print("\033[1;31;40m密码不能包含中文！\033[0m")
    # 检查密码长度
    elif not 10 <= len(p) <= 20:
        print("\033[1;31;40m长度不符合要求,必须在10到20个字符之间\033[0m")
    # 检查密码是否已字母或下划线开头
    elif not re.match("^[a-zA-Z_]",p):
        print("\033[1;31;40m密码必须以字母或下划线开头\033[0m")
    # 检查是否包含数字字母和特殊字符
    elif not (re.search('[\d]',p) and re.search('[a-zA-Z]',p) and re.search('[\W]',p)):
        print("\033[1;31;40m密码必须包含数字字母和特殊字符\033[0m")
    # 检查密码是否过于简单
    elif level == 1:
        return True
    elif level == 2:
        # 高级密码复杂度检查，检查字符是否连续出现超过字符串长度减8次
        l = len(p)-8
        # print(l)
        p_temp = p[:9]
        for char in p_temp:
            # chars = re.search(r'[%s]{%d,}'%(char,l),p)
            if char*l in p:
                print("您的密码过于简单")
                print("%s重复出现超过%d次!"%(char,l))
                return False
            else:
                return True

while True:
    p = input("请输入密码> ").strip()

    if p == 'quit':
        exit()
    if check_password_complexity(p,2):
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print("密码%s符合密码复杂度要求！"%p)