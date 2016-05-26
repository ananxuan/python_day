#!/usr/bin/env python3
__author__ = 'DSOWASP'


"""
类：人物、游戏、技能
函数：打印技能、技能id和技能描述转换、打印角色列表
人物：姓名、游戏积分、人物等级、金币、技能
游戏：游戏名、游戏输出、游戏输入、游戏奖励（积分、金币）
技能：购买技能条件（等级和金币）、技能效果、技能描述
"""

import prettytable


# 技能类，技能呢商店，技能描述，技能功能
class Skill(object):
    # 技能商店，技能id,所需的玩家等级和购买金币
    skills = [{"id":"1","level":1,"gold":10},
              {"id":"2","level":3,"gold":50},
              {"id":"3","level":3,"gold":50},
          ]
    # 技能描述
    skills_desc = {"1":"提示","2":"双倍积分奖励","3":"双倍金币奖励"}

    # 技能功能
    def skill_action(ans,point,gold,prompt):
        """

        :param point: 游戏积分
        :param gold: 游戏金币
        :param prompt: 游戏提示
        :return: 使用过技能卡后的游戏积分、游戏金币
        """
        if ans == "1":
            print("\033[1;32;0m%s\033[0m"%prompt)
        elif ans == "2":
            point *= 2
            print("\033[1;32;0m成功使用双倍积分卡，本次关卡游戏胜利可获得\033[1;31;0m%s\033[1;32;0m积分\033[0m"%point)
        elif ans == "3":
            gold *= 2
            print("\033[1;32;0m成功使用双倍金币卡，本次关卡游戏胜利可获得\033[1;31;0m%s\033[1;32;0m金币\033[0m"%gold)
        return point,gold


# 打印技能商店商品
def print_skill_info():
    """

    :return: 技能商店的技能id列表
    """

    pt = prettytable.PrettyTable(["id","技能","所需等级","金币(￥)"])
    for i,s in enumerate(Skill.skills,1):
        pt.add_row([i,Skill.skills_desc[s["id"]],s["level"],s["gold"]])
    print(pt)
    return ["1","2","3"]


# 转换技能id为技能描述
def skills_tr(skill,l):
    """

    :param skill: 技能列表
    :param l: 需转换的方式
    :return: 转换后的字符串
    """
    s_decs = []
    if l == 0:
        for s in skill:
            s_decs.append(Skill.skills_desc[s])
    elif l == 1:
        for s in skill:
            s_decs.append("%s:%s"%(s,Skill.skills_desc[s]))
    return s_decs


# 玩家类
class Player(object):
    # 定义等级和积分的关系
    point_level_tr = {1:100,2:300,3:600,4:1000,5:1500}

    # 定义角色，角色名，初始化金币，初始化技能列表
    pl = [{"name":"电神吊炸天","gold":100,"skill":["1","2"]},
          {"name":"Angelababy","gold":100,"skill":["2"]},
          {"name":"奶茶妹妹","gold":100,"skill":["3"]}]

    # 初始化玩家
    def __init__(self,name):
        for p in Player.pl:
            if p["name"] == name:
                self.name = p["name"]
                self.skill = p["skill"]
                self.gold = p["gold"]
                self.guanqia = 0
                self.level = 1
                self.point = 0

    # 购买技能
    def buy_skill(self):
        """

        :return: None
        """
        # 打印技能商店商品，并返回商品id
        s_l = print_skill_info()
        while True:
            c_in = input("\033[1;34;0m请输入你要购买的技能,default_input is:[quit]>\033[0m ").strip()
            if c_in == "":
                return None
            if c_in in s_l:
                c_in = int(c_in)
                break
            else:
                print("\033[1;31;0m输入错误!\033[0m")
                continue
        # 购买的技能s 为字典
        s = Skill.skills[c_in-1]

        # 判断等级和金币是否足够
        if s["level"] <= self.level and s["gold"] <= self.gold:
            self.gold -= s["gold"]
            self.skill.append(s["id"])
            print("\033[1;32;0m购买成功!\033[0m")
        else:
            print("\033[1;31;0m等级或金币不足，请选择其他购买!\n\033[0m")

    # 更新个人信息
    def upgrade(self,point,gold,skill):
        """

        :param point: 赚钱的积分
        :param gold: 赚钱的金币
        :param skill: 赚钱的技能
        :return: None
        """
        self.point += point
        self.gold += gold
        for s in skill:
            self.skill.append(s)
        self.guanqia += 1
        # 更新玩家等级
        L = 1
        for l,p in Player.point_level_tr.items():
            if self.point > p:
                L = l
                continue
            else:
                self.level = L
                break

    # 打印玩家信息
    def print_info(self):
        """

        :return: None
        """
        s_decs = skills_tr(self.skill,0)
        print("角色名:\033[1;32;0m%s\033[0m,"
              "等级:\033[1;32;0m%s\033[0m,"
              "积分:\033[1;32;0m%s\033[0m,"
              "金币:\033[1;32;0m%s\033[0m,"
              "已闯关卡:\033[1;32;0m%s\033[0m,"
              "技能:\033[1;32;0m%s\033[0m\n"
              %(self.name,self.level,self.point,self.gold,self.guanqia,s_decs))

    # 删除技能
    def del_skills(self,s):
        """

        :param s: 要删除的技能
        :return: None
        """
        self.skill.remove(s)


# 打印玩家列表
def player_list():
    """

    :return: 角色名列表
    """
    print("\033[1;32;0m可供选择的角色：\033[0m")
    p = Player.pl
    pt1 = prettytable.PrettyTable(["角色名","金币","技能"])
    pnl = []
    for p1 in p:
        skill = []
        for s in p1["skill"]:
            skill.append(Skill.skills_desc[s])
        pt1.add_row([p1["name"],p1["gold"],skill])
        pnl.append(p1["name"])
    print(pt1)
    # print(pnl)
    return pnl


# 关卡列表
guanqia_l = [{"id":1,
              "point":100,
              "type":"成语",
              "content":"天衣__","choices":["杨","里","王","适","建","病","无","与","站","缝","匹"],
              "answer":"无缝",
              "gold":100,
              "prompt":"比喻事物周密完善,找不出什么毛病!",
              "skill":[]},
             {"id":2,
              "point":150,
              "type":"成语",
              "content":"八__","choices":["晚","谋","过","眼","七","仙","洋","足","禁","海","含"],
              "answer":"仙过海",
              "gold":100,
              "prompt":"比喻各自拿出本领或办法，互相竞赛",
              "skill":["2"]},
             {"id":3,
              "point":200,
              "type":"数学",
              "content":"啤酒2元一瓶，四个瓶盖可以换一瓶啤酒，两个空瓶可以换一瓶啤酒，请问10元钱可以喝几瓶啤酒？","choices":"请填空_____",
              "answer":"20",
              "gold":100,
              "prompt":"比喻各自拿出本领或办法，互相竞赛",
              "skill":["2"]}

]


# 游戏类
class Game(object):

    def __init__(self):
        print("\033[1;31;0m游戏加载中...\033[0m")

    def role_choice(self):
        """

        :return: 角色实例，返回Player()
        """
        r1 = player_list()
        while True:
            c_p_name = input("\033[1;34;0m请选择角色,输入角色名:\033[0m").strip()
            if c_p_name in r1:
                p1 = Player(c_p_name)
                break
            else:
                print("角色输入错误！")
        return p1

    # 开始游戏
    def begin_game(self,p):
        """

        :param p: 玩家实例
        :return: 回答正确返回Ture,回答错误返回False
        """
        # 获取关卡字典
        guanqia = guanqia_l[p.guanqia]

        point = guanqia["point"]
        gold = guanqia["gold"]
        skill = guanqia["skill"]
        s_desc1 = skills_tr(skill,0)

        print("关卡\033[1;32;0m%d\033[0m"%guanqia["id"])
        print("类型:\033[1;32;0m%s\033[0m"%guanqia["type"])
        print("\033[1;32;0m可赚--->\033[0m 积分：\033[1;32;0m%s\033[0m,"
              " 金币：\033[1;32;0m%s\033[0m,"
              " 技能：\033[1;32;0m%s\033[0m"%(point,gold,s_desc1))
        print("题目：\033[1;32;0m%s\033[0m"%guanqia["content"])
        print("可选项：\033[1;32;0m%s\033[0m"%guanqia["choices"])

        # 记录选择过哪些技能，技能记录列表
        sk_l = []
        while True:
            s_desc2 = skills_tr(p.skill,1)
            ans = input("请输入正确的答案,可使用技能\033[1;32;0m%s\033[0m> "%s_desc2).strip()
            if ans == "":
                continue
            # 如果输入的是技能id
            if ans in p.skill:
                # 如果此技能在当前关卡已使用过
                if ans not in sk_l:
                    # 根据选择进行相应的动作
                    point,gold = Skill.skill_action(ans,point,gold,guanqia["prompt"])
                    # 将使用的仅能id插入已使用技能列表
                    sk_l.append(ans)
                    # 删除玩家一个技能
                    p.del_skills(ans)
                    continue
                else:
                    print("\033[1;31;0m同一种技能在同一关内不能重复使用！\033[0m")
            elif ans == guanqia["answer"]:
                # 回答正确，更新玩家信息
                p.upgrade(point,gold,skill)
                return True
            else:
                return False

# 游戏主入口
if __name__ == "__main__":
    # 游戏加载
    g1 = Game()

    # 角色选择
    p1= g1.role_choice()
    # print(p1.name,p1.skill,p1.gold,p1.level)

    # 开始游戏
    # 关卡关数
    guanqia_len = len(guanqia_l)

    while True:
        # 打印角色信息
        p1.print_info()
        # 根据选择进行相应的动作
        c_in = input("\033[1;34;0m1、开始游戏"
                     "  2、购买技能"
                     "  3、退出游戏"
                     " > \033[0m").strip()
        if c_in == "1":
            if p1.guanqia < guanqia_len:
                if g1.begin_game(p1):
                    print("\033[1;32;0m闯关成功!\033[0m\n\033[1;31;0m%s\033[0m\n"%("="*80))
                else:
                    print("\033[1;31;0m闯关失败！\033[0m\n\033[1;31;0m%s\033[0m\n"%("="*80))
            else:
                print("\033[1;31;0m新关卡还未实现!\033[0m\n\033[1;31;0m%s\033[0m\n"%("="*80))
        elif c_in == "2":
            p1.buy_skill()
        elif c_in == "3":
            exit()
        else:
            print("\033[1;31;0m输入错误!\033[0m")
