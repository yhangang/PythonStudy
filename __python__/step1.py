# -*- coding: UTF-8 -*-
from time import sleep
import time
import calendar
import re
import json

'''
数据类型
'''
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
 
print counter, type(counter)
print miles, type(miles)
print name, type(name)

'''
赋值
'''
a = b = c = 1  
a, b, c = 1, 2, "john"  # 多个变量赋值

'''
回收变量
'''
del a  # 删除变量
del b  # 删除变量
del c  # 删除变量

'''
字符串
'''
str1 = 'Hello World!'
 
print str1  # 输出完整字符串
print str1[0]  # 输出字符串中的第一个字符
print str1[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str1[2:]  # 输出从第三个字符开始的字符串
print str1 * 2  # 输出字符串两次
print str1 + "TEST"  # 输出连接的字符串
print str1[-2:]

'''
列表
'''
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list1  # 输出完整列表
print list1[0]  # 输出列表的第一个元素
print list1[1:3]  # 输出第二个至第三个的元素 
print list1[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list1 + tinylist  # 打印组合的列表

'''
元组
'''

tuple1 = ('runoob', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')
 
print tuple1  # 输出完整元组
print tuple1[0]  # 输出元组的第一个元素
print tuple1[1:3]  # 输出第二个至第三个的元素 
print tuple1[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple1 + tinytuple  # 打印组合的元组

'''
字典
'''

dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"
 
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
 
 
print dict1['one']  # 输出键为'one' 的值
print dict1[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值
print tinydict.items()

'''
算术运算符
'''

a = 21
b = 10
c = 0
 
c = a + b
print "1 - c 的值为：", c
 
c = a - b
print "2 - c 的值为：", c 
 
c = a * b
print "3 - c 的值为：", c 
 
c = a / b
print "4 - c 的值为：", c 
 
c = a % b
print "5 - c 的值为：", c
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b 
print "6 - c 的值为：", c
 
a = 10
b = 4.0
c = a // b  # 整数除法，返回不大于结果整数
print "7 - c 的值为：", c


'''
比较运算符
'''
a = 21
b = 10
c = 0
 
if (a == b):
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"
 
if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"
 
if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"
 
if (a < b):
    print "4 - a 小于 b" 
else:
    print "4 - a 大于等于 b"
 
if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"
 
# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"
 
if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"

'''
赋值运算符
'''

a = 21
b = 10
c = 0
 
c = a + b
print "1 - c 的值为：", c
 
c += a
print "2 - c 的值为：", c 
 
c *= a
print "3 - c 的值为：", c 
 
c /= a 
print "4 - c 的值为：", c 
 
c = 2
c %= a
print "5 - c 的值为：", c
 
c **= a
print "6 - c 的值为：", c
 
c //= a
print "7 - c 的值为：", c

'''
位运算符
'''
    
a = 0b00111100

b = 0b00001101

print bin(a & b)

print bin(a | b)

print bin(a ^ b)

print bin(~a)

'''
进制转换
'''
a = 15

print hex(a)  # 16进制
print int(a)  # 10进制
print oct(a)  # 8进制
print bin(a)  # 2进制


'''
逻辑运算符
'''

a = 10
b = 20
 
if (a and b):
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"
 
if (a or b):
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"
 
# 修改变量 a 的值
a = 0
if (a and b):
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"
 
if (a or b):
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"
 
if not(a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"

'''
成员运算符
'''
a = 10
b = 20
lists = [1, 2, 3, 4, 5 ];
 
if (a in lists):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"
 
if (b not in lists):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"
 
# 修改变量 a 的值
a = 2
if (a in lists):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"


'''
身份运算符
'''
a = 20
b = 20
 
if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"
 
if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"
 
# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"
 
if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"

'''
条件语句
'''
# 例1：if 基本用法
flag = False
name = 'luren'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

# 例2：elif用法
num = 5     
if num == 3:  # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'roadman'  # 条件均不成立时输出
    
# 例3：if语句多个条件
num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello
num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine
 
num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

'''
循环语句
'''
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1
 
print "Good bye!"

# continue 和 break 用法
 
i = 1
while i < 10:   
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10
 
i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# while...else..语句用法
count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"

# for语句的用法
for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter
 
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit
 
print "Good bye!"

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]
 
print "Good bye!"

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
        else:  # 循环的 else 部分
            print num, '是一个质数'
           
'''
pass语句
'''  
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母 :', letter

print "Good bye!"

'''
类型转换
'''  
x = 1
int(x)  #  将x转换为一个整数  
long(x)  # 将x转换为一个长整数  
float(x)  # 将x转换到一个浮点数  
complex(x)  # 创建一个复数  
str(x)  # 将对象 x 转换为字符串  
repr(x)  # 将对象 x 转换为表达式字符串  
eval('1')  # 用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple([1, 2, 3])  # 将序列 s 转换为一个元组  
list([1, 2, 3])  # 将序列 s 转换为一个列表  
chr(x)  # 将一个整数转换为一个字符  
unichr(x)  # 将一个整数转换为Unicode字符  
ord('1')  # 将一个字符转换为它的整数值  
hex(x)  # 将一个整数转换为一个十六进制字符串  
oct(x)  # 将一个整数转换为一个八进制字符串  

'''
字符串
'''  
var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

print "更新字符串 :- ", var1[:6] + 'Runoob!'

a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b 
print "a * 2 输出结果：", a * 2 
print "a[1] 输出结果：", a[1] 
print "a[1:4] 输出结果：", a[1:4] 

if("H" in a) :
    print "H 在变量 a 中" 
else :
    print "H 不在变量 a 中" 

if("M" not in a) :
    print "M 不在变量 a 中" 
else :
    print "M 在变量 a 中"

print r'\n'
print R'\n'

# 格式化字符串
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

'''
列表
'''  

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

list1 = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list1[2];
list1[2] = 2001;
print "New value available at index 2 : "
print list1[2];

list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

'''
元组
'''  
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7);

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]


tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;

tup = ('physics', 'chemistry', 1997, 2000);

print tup;
del tup;
print "After deleting tup : "
# print tup;

'''
字典
'''  
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
print "dict['Name']: ", dict1['Name'];
print "dict['Age']: ", dict1['Age'];


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
dict1['Age'] = 8;  # update existing entry
dict1['School'] = "DPS School";  # Add new entry
 
 
print "dict['Age']: ", dict1['Age'];
print "dict['School']: ", dict1['School'];

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
del dict1['Name'];  # 删除键是'Name'的条目
dict1.clear();  # 清空词典所有条目
del dict1 ;  # 删除词典
 
'''
日期和时间
'''  
ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;

'''
函数
'''  
# 定义函数
def printme(string):
    "打印任何传入的字符串"
    print str;
    return;
 
# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

# 传递不可变对象作为参数
def ChangeInt(a):
    a = 10
    return a

b = 2
ChangeInt(b)
print b  # 结果是 2

# 传递可变对象作为参数
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return
 
# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist


# 可写函数说明，关键字参数
def printme2(string):
    "打印任何传入的字符串"
    print string;
    return;
 
# 调用printme函数
printme2(string="My string");


# 可写函数说明，缺省参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;
 
# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");


# 可写函数说明，不定长参数
def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;
 
# 调用printinfo 函数
printinfo2(10);
printinfo2(70, 60, 50, 40);


# 匿名函数
sum1 = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print "相加后的值为 : ", sum1( 10, 20 )
print "相加后的值为 : ", sum1( 20, 20 )


'''
模块
''' 
if __name__ == '__main__':
    print '作为主程序运行'
else:
    print 'package_runoob 初始化'
    
'''
异常
'''    
    
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
finally:
    print '异常结束'

'''
正则表达式
''' 
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

'''
json操作
''' 
#json.dumps 用于将 Python 对象编码成 JSON 字符串
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
jsonstr = json.dumps(data)
print jsonstr

#json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = json.loads(jsonData)
print text









# 获取当前毫秒时间戳，用于计算程序运行时间
# print int(round(time.time() * 1000)) 
# sleep(0.5)
# print int(round(time.time() * 1000)) 
