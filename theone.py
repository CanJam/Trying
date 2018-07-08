# -*- coding:UTF-8 -*-

# 第一章
print ("this is my frsit game")
i=1
if(i<10):
    print("该值于10")
    i=i+1
elif(i>=10): 
    print("该值大于等于10")    
# input语句下的输入，运算
x = input("x: ")
y = input("y: ")
print (x * y) 
#简单的if语句
if 1==2: 
    print ("One equal two")
if 1==1:
    print ("One equal One")
#pow(x,y)x的y次方函数的简单运用
print(2**3)       
print(pow(2,3))
print(abs(-10)) # abs函数可以得到绝对值
print(round(1.0/2.0)) #round函数会把浮点值四舍五入为整数
import math # import导入模块math，按照”模块.函数“的格式使用这个函数
print (math.floor(32.9))
print int(math.floor(32.9))  
from math import sqrt # from...import..
print (sqrt(9)) # sqrt为平方根函数，该函数不能求负数平方根,可以使用cmath()函数，该函数尽量用import
name = raw_input("What is your name? ") # raw_input()会把输入的原始数据（raw data），再放入字符串中/input()假设函数合法用于客户输入
print ('HELLO.' + name + '!')   
print("let\'s go")  #使用\对'进行转义
x = "hello."
y = "world+"
z = 42 
print (x + y + repr(z)) #repr(x)可以将任何数据类型变成python合法的语句，单纯是一个函数方法
print ('''This is a very long string
    It continues here.
    And it's not over yet.
    "Hello.world!"
    Still here.''')  #用'''来打印长字符串



