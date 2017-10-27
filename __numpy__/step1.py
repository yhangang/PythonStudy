# -*- coding: utf-8 -*-  
import copy

import numpy as np


# 输出版本号
print np.version.version


# 初始化numpy数组
arr = np.array([1, 2, 3, 4])
print arr
print type(arr)


# 使用列表或者元组初始化
x = np.array(((1, 2, 3), (4, 5, 6)))  
y = np.array([[1, 2, 3], [4, 5, 6]])  
print x
print y


# numpy数组的类型转换
foo = np.array(['1.23', '2.34', '3.45'], dtype=np.string_)  
print foo
print foo.astype(float)


# 索引
x = np.arange(1, 10).reshape(3, 3)
print x
print x[1]
print x[1][2]


# 切片
x = np.arange(1, 10)
y = x[:]
print y
y = x[2:5]
print y


# 赋值
x = np.arange(1, 10)
y = x  # x与y内存地址完全相同
print y
y[3] = 0
print x  # 对y赋值，但是x的值改变了，说明y只是x的引用
# 总结赋值的原理如下：赋值只是增加了一个引用，相当于起了别名，和原来的对象完全一样


# 浅拷贝
x = [1, 2, [0, 0, 0], 4, 5]
y = x[:]  # 通过切片拷贝
# y = copy.copy(x)    #通过copy函数拷贝
# y = list(x)    #通过工厂函数拷贝
print id(x) 
print id(y)  # x与y的内存地址不同

print id(x[1])
print id(y[1])
print id(x[2])  
print id(y[2])  # 但是x与y中的元素地址相同

x[1] = 9
x[2] = 9
print x
print y  # x并没有被改变,同理，改变x，y值也不会改变
# 总结出浅拷贝的原理如下：被拷贝的元素是新建的对象和内存地址，但是其中元素还是指向之前的（共用）；
# 但是一旦其中一个值改变了，就会新建这个值的对象,开辟新的空间，而原来的值继续指向未改变的那个对象


# 深拷贝
x = [0, [1, 2], 3]  
y = copy.deepcopy(x)
print id(x)
print id(y)
print id(x[0])
print id(y[0])
print id(x[1])
print id(y[1])  # x中所有对象都被重新拷贝一遍，但是不可变对象例外，这是常量


# 多维数组的索引与切片
arr = np.arange(1, 10).reshape(3, 3) 
print arr
print arr[2]
print arr[2][2]
print arr[:2]
print arr == [2]


#特殊矩阵
print np.zeros((3,4))
print np.ones((3,4))
print np.eye(4)


#获取矩阵属性
a = np.zeros((2,2,2))  
print a.ndim   #数组的维数  
print a.shape  #数组每一维的大小  
print a.size   #数组的元素数  
print a.dtype  #元素类型  
print a.itemsize  #每个元素所占的字节数 


#合并数组
a = np.eye(3)
b = np.ones((3,3))
print np.vstack((a,b))
print np.hstack((a,b))

