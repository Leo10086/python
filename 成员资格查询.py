#! usr/bin/python
#_*_ coding:utf-8 _*_
#检查用户名和工号
data = [
    ['zhang_san','0001'],
    ['li_si','0002'],
    ['wang_wu','0003'],
    ['zhao_liu','0004'],
    ['zhou_qi','0005']
]
username = raw_input('user name:')
number = raw_input('number:')

if [username,number] in data: print 'access granted'