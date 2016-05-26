#!/usr/bin/env python3
__author__ = 'DSOWASP'
class person:
    assets = 0
    school_name = None
    Interview = ['360', 'Baidu', 'Ali', 'Tengxun']
    attraction = 0
    skills = []
    love_status = None
    lover = None
    job = None
    company = None

    def __init__(self, name, sex, role):
        self.name = name
        self.sex = sex
        self.role = role
        print('\033[32;1m-\033[0m'*60)
        if self.role == 'rich':
            self.assets += 10000000
            self.attraction += 80
            print('\033[32;1mMy name is %s, I am a %s guy, I have %s money! It is good to be rich..\033[0m'\
            %(self.name, self.role, self.assets))
        elif self.role == 'poor':
            self.assets += 5000
            self.attraction += 40
            print('\033[31;1mMy name is %s, I am a %s guy, I hvae %s money! I hate \
to be poor, but...life is fucking hard..\033[0m' % \
            (self.name, self.role, self.assets))
        elif self.role == 'beauty':
            self.assets += 5000
            self.attraction += 90
            print('\033[32;1mMy name is %s, I am a %s girl, I do not have much money, \
but I am very beautiful,that makes me feel good and confident, but I do \
not want to be poor forever.\033[0m' % (self.name,self.role))


    def talk(self, msg, tone = 'normal'):
        if tone == 'normal':
            print('\033[32;1m%s: %s\033[0m' % (self.name, msg))
        elif tone == 'angry':
            print('\033[31;1m%s: %s\033[0m' % (self.name, msg))

    def assets_balance(self, amount, action):
        if action == 'earn':
            self.assets += amount
            print('\033[32;1m%s just made %sRMB! Current assets is %s \033[0m' % \
            (self.name, amount, self.assets))
        elif action == 'cost':
            self.assets -= amount
            print('\033[32;1m%s just cost %sRMB! Current assets is %s \033[0m' % \
            (self.name, amount, self.assets))

p1 = person('John', 'male', 'poor')
p1.talk('Hello, my guys!')
p1.assets_balance(300, 'earn')

p2 = person('Liz', 'female', 'beauty')
p2.talk('Hi, my dear!')
p2.assets_balance(1500,'earn')

p3 = person('Peter', 'male', 'rich')
p3.talk('Hi guys')
p3.assets_balance(3000, 'cost')

def section(part):
    print('\033[31;1m*\033[0m'*30 + part + '\033[31;1m*\033[0m'*30)

section('Part 1: A love story')

p1.lover = p2
p1.love_status = 'Not_single'
p1.talk('I hvae a girlfriend, her name is %s.I love she very much.' % p1.lover.name)

p2.lover = p1
p1.love_status = 'Not_single'
p2.talk('I have a boy friend, his name is %s.Thout he is poor, he loves me.' % p2.lover.name)

section('Part 2: college entrance examination')

p1.talk('Oh, my god! I can not go to a college.', 'angry')
p2.talk('I can go to a college to change my life.')

section("Part 3: Liz's difficulity")

p2.talk('What should I do?I do not have money to go to the college.')
p1.talk('Do not worry!Though I can not go to the college with you, I still can earn money to support you.')
p2.talk('%s, so thank you for you.I love you!' % p2.lover.name)

section("Part 4: work and college life")

p1.talk('In order to support %s, I must work hard at the net bar.' % p1.lover.name)
p2.talk('I will study hard to enter a good company when I graduate.')