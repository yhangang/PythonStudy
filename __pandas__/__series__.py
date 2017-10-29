# encoding:utf-8
import numpy as np
import pandas as pd

'''
series对象的使用示例
'''
# s = pd.Series([1,3,5,np.nan,6,8])       #初始化默认索引的series对象
# s = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])     #初始化带索引的series对象
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}      #通过字典对象初始化series
s = pd.Series(sdata)
print s

#重新定义index
s.index = range(len(s))
print s

print dict(s)       #转换为字典类型


 
print s.dtypes     #使用dtypes来查看各行的数据格式
print s.head(2)        #返回前n行
print s.tail(2)        #返回倒数n行
print s.index      #查看数据框的索引
print s.columns        #查看列名用columns,dataframe属性
print s.values     #查看数据值，用values
print s.describe()     #查看描述性统计，用describe
print s.T      #使用T来转置数据，也就是行列转换
print s.sort(columns = "x")       #columns为dataframe属性

print 'a' in s  #判断在不在index里