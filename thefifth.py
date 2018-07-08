# -*- coding:UTF-8 -*- 
"""
import math as fuck #在句末加上as子句，给模块取上了别名
print fuck.sqrt(4)
#同时进行多个赋值操作
x,y,z = 1,2,3
print x,y,z
#用来交换两个或多个变量都可以
x,y = y,x
print x,y,z
#以上所做的事情叫做序列解包（sequence unpacking）或递归解包，将多个值的序列解开，然后再放回序列，例：
values = 1,2,3
print values
x,y,z = values
print x
scoundre1 = {'name':'Robin','girlfriend':'Marion'}
key,value = scoundre1.popitem() #可以将键-值作为元组返回
print key
print value

# 运算表达式的格式,#增量赋值
x = 2 
x += 1
x *= 2  
print x

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print fnord

# 链式赋值 x = y = "somefunction()"

#条件和条件语句
# False None 0（） “” [] {} 都会被解析器看作假（false）
print False + True + 42   #False==0, True==1,都可以参加运算

name = raw_input('what is you name?')
if name.endswith('CAM'): #如果条件为真，就会执行print语句块
    print ('Hello,Mr.CAM')
else: #else子句，只能作为if的一部分，在if不为真的情况下，会执行
    print 'Hello,Mr.stranger'

num = input('Enter a number: ')
if num>0:
    print 'The number is positive'
elif num<0: #elif:是else if 的缩写，如果需要检查多个条件，可以用到elif
    print 'The number is negative'
else:
    print 'The number is zero'        

name = raw_input('what is you name?')
if name.endswith('CAM'): 
    if name.startswith('Mr.'): #嵌套语句，if里面嵌套if，在下面的复杂的大程序里，很经常用  
        print ('Hello,Mr.CAM')
    elif name.startswith('Mrs.'):
        print 'Hello,Mrs.CAM'
    else :
        print 'Hello,CAM'    
else: 
    print 'Hello,Mr.stranger'

#比较运算符
x == y  
x < y
x > y
x >= y
x <= y
x != y
x is y 
x is not y
x in y 
x not in y  

x = [1,2,4]
y = [2,4]
print x is not y
del x[2]
y[1] = 1
print y.reverse()
print x is y #判定同一性，而不是相等性
print x == y #使用==运算符来判定两个对象是否相等
print x is y #使用is判定两者是否等同（同一个对象）

name = raw_input('What is your name?')
if 's' in name: #in的例子简单明了
    print 'Your name contains the letter "s"'
else:
    print 'Your name does not contains the letter "s"'    

print 'apha' < 'beta' #字母顺序排列比较
print 'FnOrD'.lower() == 'fnord'.lower() 
print [1,2] < [2,1] #序列元素的比较

#判断输入的数有没有在1到10内：
number = input('Enter a number between 1 and 10: ')
if number <= 10:
    if number >= 1:
        print 'Great!'
    else:
        print 'Wrong!'
else:
    print 'Worng!'            
#更加简洁的方法：
if 1<=number<=10: #同样可以用 number <=10 and number >=1 and要两边条件都为ture才可以执行 
    print 'Great!'
else:
    print 'Worng!'    

x = 1
while x <= 100: #while 循环语句
    print x
    x += 1

name  = ''
while not name or name.isspace(): #.isspace()/strip()如果字符串为空就会重新要求输入名字
    name = raw_input('Please enter your name: ')
    print 'Hello. %s!' % name    

words = ['this','is','an','ex','parrot'] #迭代出words
for word in words:
    print word

print range(0,10) #range()迭代,返回一整个序列，xrange一次值创建一个数，当要迭代巨大序列时xrange更高效

d = {'x':1,'y':2,'z':3} #因为不允许直接迭代字典
for key, value in d.items():
    print key, 'corresponds to', value

names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for i in range(len(names)):
    print names[i],'is' ,ages[i],'years old'
"""






























