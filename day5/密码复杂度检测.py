import  re
'''
接口调用示例：
import 密码复杂度检测 as pc

while True:
    str1 = input("请输入密码> ").strip()
    if pc.check_password_complexity(str1,2):
        print("%s复杂度符合要求"%str1)
        break


密码复杂度检查，包括两种复杂度检查，
level=1时，
    密码不能包含中文，
    长度在10到20个字符之间
    密码必须已字母或下划线开始
    密码必须包含字母、数字、特殊字符
level-2时，
    包含level=1的条件
    不能有一个字符连续出现超过字符长度减8次的情况，比如字符长度是10，则不能有一个字符连续出现2次的情况
'''
def check_password_complexity(p,level):
    """

    :param p: 传递进来的待检测的密码
    :param level: 需要检查的强度
    :return: 如果密码复杂度符合要求则返回True，否则返回False
    """
    # 判断等级是否是1或2
    assert level in (1,2),'level密码强度检查只能是1或2'
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
        # 高级密码复杂度检查，检查字符是否连续出现超过字符串长度减8次,更高级检查待开发
        l = len(p)-8
        # print(l)
        p_temp = p[:9]
        for char in p_temp:
            # chars = re.search(r'[%s]{%d,}'%(char,l),p)
            if char*l in p:
                print("您的密码过于简单")
                print("%s重复出现超过%d次!重复次数不能超过字符长度减8次"%(char,l))
                return False
            else:
                return True

if __name__ == '__main__':
    print("请使用\033[1;31;0mheck_password_complexity\033[0m(\033[1;32;0mpassword,level\033[0m)调用此函数")