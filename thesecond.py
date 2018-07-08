# -*- coding:UTF-8 -*-

# 列表的各个元素通过逗号分隔，写在方括号中，元素列表成为数据库的关键
edward = ['cam jam', 42]
ljj = ['liu jj', 50]
database = [edward,ljj]
print (database)
# 序列中的所有元素都是有编号的，从左到右是从0开始，从右到左是从-1，-2开始
greeting = 'Hello'
print (greeting[0])
print (greeting[-1])
print (greeting[-2])
'Hello'[1] #字符串可以直接索引，可不用变量引用，效果相同

fourth = raw_input('Year: ' )[3] # 一个函数调用返回一个序列，可以直接对返回结果进行索引
print fourth

# 根据给定的年月日以数字的形式打印出日期
months = [
    'January',
    'February',
    'March',
    'April',
    'May',  
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
# 以1～31的数字作为结尾的列表
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']
# 定义用户输入内容
year    = raw_input('Year: ')
month   = raw_input('Month(1-12): ')
day     = raw_input('Day(1-31): ')
# 定义用户输入内容转成整型
month_number = int(month)
day_number = int(day)
# 记得要给月份和天数减1,以获取正确的索引
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]
print (month_name + ' ' + ordinal + '. ' + year)      

# 使用分片函数tag[x:y]
tag = '<a herf="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-1]
print tag[32:-4]

numbers = [1,2,3,4,5,6,7,8,9,10]
print (numbers[3:6]) #分片需要两个索引作为边界，第一个索引的元素包含分片内，第二个则不包含
print (numbers[0:1])
print (numbers[-3:0]) #分片中左边的索引比右边的慢出现在序列中，结果就是一个空的序列
print (numbers[-3:]) #分片包括序列结尾元素，只需要置空最后一个索引即可
print (numbers[:]) #置空两边可以复制的整个序列
print (numbers[0:10:2]) #最后一个的参数为步长，一般默认步长为1,遍历整个序列
print (numbers[8:3:-1]) #步长不可以为0，但是可以为负数，负数时从右往左开始遍历

sequence = [None] * 10 #None 是python的内建值，它的确切含义是“这里什么也没有”
print sequence

#为完成的例子，pg：32/2-3
#定义input的内容变量
sentence = raw_input("Sentence: ")
#大外框的宽度
screen_width = 80
#定义变量设置input进来的数据长度
text_width = len(sentence)
#小框的大小宽度
box_width = text_width + 6
#定义居中的相对
left_margin = (screen_width - box_width) // 2
print 
print (' ' * left_margin + '+'  + '-' * (box_width-2) +  '+')
print (' ' * left_margin + '| ' + ' ' * text_width    + ' |')
print (' ' * left_margin + '| ' +        sentence     + ' |')
print (' ' * left_margin + '| ' + ' ' * text_width    + ' |')
print (' ' * left_margin + '+'  + '-' * (box_width-2) +  '+')
print 

# in成员资格属于布尔类型，
permissions = 'rw'
print ('w' in permissions) #可以作为查看文件可写和可执行权限的脚本
print ('x' in permissions)
users = ['mlh','foo','bar'] #可以用于安全检验，例如登录系统
print raw_input('Enter your user name: ') in users
subject = '$$$ Get rich now!!! $$$'
print ('$$$' in subject) #可以作为垃圾邮件过滤器的一部分

print (list('Hello')) # list()函数或者说它是个类型，可以使用于所有类型的序列，而不只是字符串
# 改变列表的方法：如x[1]=2,通常修改键，键是惟一的
# 改变元素赋值
x = [1,1,1,]
x [1] = 2
print ( x )
# 删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print ( names ) 
# 分片赋值,分片是个很强大的特性，
name = list('Perl')
print ( name )
name[2:] = list('ar')
print ( name ) 
name[2:2] = list('fuck') #可以在不需要替换任何原有元素下插入新的元素，
print ( name )
numbers = [1,2,3,4,5]
numbers[1:4] = []  #也可以删除元素
print ( numbers )

# 列表的方法：
pacer = [1,2,3]
pacer.append(4) #append()在列表的最后加一个元素，修改了原来的表，并返回值
print ( pacer )

print ['bo','to','bo','do','so']. count('bo') #count()可以计算列表中的某个元素出现的次数
x = [[1,2],1,1,[2,1,[1,2]]] 
print (x.count(1))
print (x.count([1,2]))

a = [1,2,3]
b = [4,5,6]
a.extend(b) #可以再列表最后增加另外一个序列的多个值，会修改被扩展的序列
print ( a )  
print (a + b)# + 则不会改变原序列，会返回一个全新的列表
a = [1,2,3]
b = [4,5,6]
a[len(a):] = b #同样在这里也可以使用分片赋值方法，但是可读性没有extend的好
print ( a ) 

kinghts = ['aaa','bbb','aaa','ada','add','bbb']
print (kinghts.index('bbb')) #index()可以找到某个值第一个匹配项的索引位置，若该值不存在会报错，就是没有找到的意思

numbers = [1,2,3,5,6,7]
numbers.insert(3,'four') #insert（）可以再列表中插入元素
print (numbers)
numbers[5:5] = ['fuck'] #同样也可以用分片赋值
print (numbers)

x = [1,2,3]
print x.pop()  #会移除列表的最后一个值，并返回该元素的值
print ( x )
#pop()可以实行栈(入栈(push),出栈(pop))，与append()的意义相反，可以用作入栈
x = [1,2,3]
print x.append(x.pop())  #两个方法同时使用，得到原来的栈
print ( x )

kinghts = ['aaa','bbb','aaa','ada','add','bbb']
kinghts.remove('bbb') #remove() 用于移除某个值的第一个匹配值，不存在该值时会报错，即不存在值，运行之后没有返回值的原位置改变方法，与pop相反
print (kinghts)

x = [1,2,3]
x.reverse() #reverse()将列表中的元素反向存放，同样不返回值，是一个布尔类型，可指明是否要反向排序
print ( x )

x = [4,6,2,1,7,9]
x.sort()  #sort()在原位置对列表进行排序，改变了原来列表，从而让列表按一定顺序排序，python默认升序
print ( x ) 

x = [4,6,2,1,7,9]
y = x[:] #分片x列表的所有元素
y.sort() 
print ( x )
print ( y )

x = [4,6,2,1,7,9]
y = sorted(x) #sorted()获取已排序的元素列表，可以用在任何的序列，总是返回一个列表,cmp,key，reverse，为sorted参数提供键值***
print ( x )
print ( y )
print (sorted('python'))

# cmp(x,y)当x>y,返回正数，x<y,返回负数，x=y，返回0.
print (cmp(42,50))
print (cmp(50,42))
print (cmp(50,50))
numbers = [5,2,9,7]
numbers.sort(cmp) #cmp在这里作为sort的一个参数，同样还有key，reverse，为sort提供键值
print numbers
x = ['aaaa','asd','deded','dedededeff']
x.sort(key=len) #可以将len作为键函数，在后面框架可能会用到***
print ( x )

x = [4,6,2,1,7,9]
x.sort(reverse = True) #是一个布尔类型，可指明是否要反向排序
print ( x )

#元组：不可变序列
print (1,2,3)  # 用逗号分隔一些值，就自动创建了元组
print (3*(40+2)) #输出为126
print (3*(40+2,)) #输出为（42,42,42）为元组
print (tuple([1,2,3])#以一个序列作为参数并把它转换为元组
print (tuple('abc')) # 为解决问题，pge42




