# -*- coding:UTF-8 -*-
#字典的语法格式{‘a’：‘b’}键对值称为项

names = ['Alice', 'Beth', 'Cecil','Dee-Dee','Earl']
numbers = ['2341','9102','3158','0142','5551']
print numbers[names.index('Cecil')]

items = [('name','Cam'),('age','24')]
d = dict(items)  #通过其他映射或者对的序列建立字典
print d 
print d['name']

x = {}
x[42] = 'Foolbar' #将Foolbar赋值到键42上，则会更新到字典中，列表则不行
print x

#字典以人名为键
people = {
    'Alice':{
        'phone':'2341',
        'addr':'GUANGZHOU'
        } ,
    'Beth':{
        'phone':'9102',
        'addr':'HANGZHOU'
        } ,
    'Cecil':{
        'phone':'3158',
        'addr':'SHENZHEN'
        }
}
#针对电话号码，还有住址使用的描述标签，会在打印时用到
labels = {
    'phone':'phone number',
    'addr':'address'
}
name = raw_input('Name: ')
#查找电话还是地址
request = raw_input('Phone number (p) or address (a) ?' )
#使用正确的键，定义了p，a快捷键
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'
#如果名字是字典中的有效键才打印信息
if name in people: print "%s's %s is %s." %(name, labels[key],people[name][key])

phonebook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3258'}
print "Cecil's phone number is %(Cecil)s." % phonebook #转换说明符的用法%（key）（s....）

#字典方法
d = {}
d['name'] = 'Cam'
d ['age'] = 24
print d
returnd_value = d.clear() #clear()清除字典中所有的项，再原地操作，无返回值（None），想清空字典所有元素必须用clear
print d
print returnd_value

x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy() #copy()返回一个具有相同键-值对的新字典（这个方法实现的是浅复制（shallow copy），因为值本身相同，而不是副本）
y['username'] = 'mlh'
y['machines'].remove('bar') #移除machines中的bar
print y
print x

from copy import deepcopy
d = {}
d['names'] = ['Cam','Jam']
c = d.copy()  #shallow copy 了d上的数据，再后面
dc = deepcopy(d) #deepcopy()了 d上的数据，后面d上的数据修改，dc也会跟着修改
d['names'].append('zheng')
print c
print dc
print d

print {}.fromkeys(['name','age']) #fromkeys()使用给定的键创建新的字典，默认值是None
print dict.fromkeys(['name','age'],'(unknown)') # dict适用于所有的字典类型，返回值可以自己设置

people = {}
d = {}
print d.get('name','fuck') #get()方法，如果找不到值，返回None，也可以自定义返回值
d['name'] = 'Dam'
print d.get('name') #如果键存在，get用起来就像是普通的查字典，之后会很常用***

labels = {
    'phone':'phone number',
    'addr':'address'
}
name = raw_input('Name: ')
#查找电话还是地址
request = raw_input('Phone number (p) or address (a) ?' )
#使用正确的键，定义了p，a快捷键
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'
person = people.get(name,{})  #这里体现了get的优越性，输出未准备的值时，可以作出合理的反应
label = labels.get(key,key)
result = person.get(key,'not available')
print "%s's %s is %s. " % (name, label,result )

d = {'title' : 'Python web site','url':'http://www.python.org','spam':0}
print d.items()  #items()将字典所有的项以列表方式返回，列表中表示为键-值，但是没有遵循顺序
it = d.iteritems() #将字典所有的项以迭代器方式返回，相对较于items跟高效
print it 
print list(it)

d = {'x':1,'y':2}
print d.pop('x') # pop()用来获取对应于给定的键的值，然后将这个键-值从字典中移除
print d

d = {'title' : 'Python web site','url':'http://www.python.org','spam':0}
print d.popitem() #popitem弹出随机的项，因为字典里没有顺序概念，可以用在一个一个移除并处理项的地方，很有效
print d

d = {}
print d.setdefault('name','unknown') # setdefault()跟get方法差不多，能够获得与给定键相关的值
d['name'] = 'Cam'  
print d.setdefault('name','unkvown') #还能给不含有给定键的情况下设定键值
print d

d = {'title' : 'Python web site','url':'http://www.python.org','changed':'Mar 14 22:09:15 MET 2008'}
x = {'title':'Python language website'}
d.update(x) #update()可以利用一个字典项更新另外一个字典,若有相同键就会被覆盖
print d

d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print d.values() #values()以列表的方式返回字典中的值，返回值中可以包含重复数
print d.itervalues() #返回的是迭代器 

