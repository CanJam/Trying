# -*- coding:UTF-8 -*-
"""
format = "Hello,%s,%s enough for ya? " #%字符串格式化操作符 + s（使用str转化为任意python对象），也叫占位符
values =('world','Hot')
print format % values

print ('Price of eggs: $%d') %42 # %d 可以符号（$,...）

print ('With a moo-moo here,and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print title.find('Monty')   #find（）可以在一个较长的字符串中找子串，返回子串所在位置的最左端索引，如果没有就返回-1
print title.find('Python')
print title.find('Flying')
print title.find('fuck')

subject = '$$$ Get rich now!!! $$$'
print subject.find('!!!',1,20) #find(x,a,b)a,b 为其实的索引位置可以为find所选范围
print subject.find('!!!',1,16) #范围内找不到输出-1

seq = ['1','2','3'] 
sep = "+"
print sep.join(seq) #Join()只能接受字符串，用来连接序列中的元素***
print 'FUCK YOU MAMA'.lower() #返回字符串的小写版
name = 'Cam'
names = ['cam','gll','dak']
if name.lower() in names:
    print 'Find the bitch' 

import string #引入了string模块
print string.capwords("that's all, folks,fuck")#capwords()，可以得到正确的首字母大写标题

print "This is a test ".replace('is','ass') # replace(a,b)可以将序列中的a值替换成b，之后得到字符串

print '1+2+3+4+5'.split('+') #split()是join的逆方法，用来将字符串分割成序列,***
print '/usr/bin/theone'.split('/') #其中‘/’为分割符，如果不见任何分割符，默认（空格，制表，换行符）

names = ['cam','gll','dak']
name = 'cam '
if name.strip()in names: print "find it "  #strip()去除两侧空格的字符，用在用户不小心再名字后加了空格
print '***SPAM * for * everyone!!!***'.strip('!*') #可以出去两侧字符，字符串中间则不会

from string import maketrans #使用了string模块里的marktrans函数
table = maketrans('cs', 'kz') # 将table中的cs改成kz
print len(table) #输出talbe的长度
print table[97:123] #分片97到122的字母
print maketrans('','')[97:123] #没有置换这区域的内容
print 'this is an incredible test'.translate(table)#translate()以table为参数，来替换序列中的字母
"""
